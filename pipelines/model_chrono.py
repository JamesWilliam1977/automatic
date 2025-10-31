import sys
import transformers
from modules import shared, devices, sd_models, model_quant, sd_hijack_te, sd_hijack_vae
from pipelines import generic


def postprocess(p, result): # pylint: disable=unused-argument
    shared.log.debug('Postprocess: model=ChronoEdit')
    if result is not None and hasattr(result, 'images'):
        result.images = result.images[-1]
    return result


def load_chrono(checkpoint_info, diffusers_load_config=None):
    if diffusers_load_config is None:
        diffusers_load_config = {}
    repo_id = sd_models.path_to_repo(checkpoint_info)
    sd_models.hf_auth_check(checkpoint_info)

    load_args, _quant_args = model_quant.get_dit_args(diffusers_load_config, allow_quant=False)
    shared.log.debug(f'Load model: type=ChronoEdit repo="{repo_id}" config={diffusers_load_config} offload={shared.opts.diffusers_offload_mode} dtype={devices.dtype} args={load_args}')

    from pipelines.chrono import pipeline_chronoedit
    from pipelines.chrono import transformer_chronoedit

    # monkey patch for <https://huggingface.co/Disty0/ChronoEdit-14B-SDNQ-uint4-svd-r32/blob/main/model_index.json>
    import pipelines.chrono
    sys.modules['chronoedit_diffusers'] = pipelines.chrono
    from diffusers.pipelines import pipeline_loading_utils
    pipeline_loading_utils.LOADABLE_CLASSES['chronoedit_diffusers.transformer_chronoedit'] = {}

    transformer = generic.load_transformer(repo_id, cls_name=transformer_chronoedit.ChronoEditTransformer3DModel, load_config=diffusers_load_config, subfolder="transformer")
    text_encoder = generic.load_text_encoder(repo_id, cls_name=transformers.UMT5EncoderModel, load_config=diffusers_load_config, subfolder="text_encoder")

    try:
        pipe = pipeline_chronoedit.ChronoEditPipeline.from_pretrained(
            repo_id,
            transformer=transformer,
            text_encoder=text_encoder,
            cache_dir=shared.opts.diffusers_dir,
            **load_args,
        )
    except Exception as e:
        import os
        from modules import errors
        errors.display(e, 'Chrono')
        os._exit(1)
    pipe.postprocess = postprocess
    pipe.task_args = {
        'num_temporal_reasoning_steps': shared.opts.model_chrono_temporal_steps,
        'output_type': 'np',
    }
    # reference: <https://github.com/nv-tlabs/ChronoEdit/blob/main/scripts/run_inference_diffusers.py>
    if shared.opts.model_chrono_temporal_steps > 0:
        pipe.task_args['num_frames'] = 29
        pipe.task_args['enable_temporal_reasoning'] = True
    else:
        pipe.task_args['num_frames'] = 5
        pipe.task_args['enable_temporal_reasoning'] = False

    del text_encoder
    del transformer

    sd_hijack_te.init_hijack(pipe)
    sd_hijack_vae.init_hijack(pipe)

    devices.torch_gc()
    return pipe
