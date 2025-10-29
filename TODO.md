# TODO

Main ToDo list can be found at [GitHub projects](https://github.com/users/vladmandic/projects)

## Future Candidates

- UI: New inpaint/outpaint interface  
  [Kanvas](https://github.com/vladmandic/kanvas)  
- Deploy: Create executable for SD.Next  
- Feature: Integrate natural language imagesearch  
  [ImageDB](https://github.com/vladmandic/imagedb)  
- Feature: Transformers unified cache handler  
- Feature: Remote Text-Encoder support  
- Refactor: [Modular pipelines and guiders](https://github.com/huggingface/diffusers/issues/11915)  
- Refactor: move sampler options to settings to config  
- Refactor: [GGUF](https://huggingface.co/docs/diffusers/main/en/quantization/gguf)  
- Feature: LoRA add OMI format support for SD35/FLUX.1  
- Refactor: remove `CodeFormer`
- Refactor: remove `GFPGAN`  
- UI: Lite vs Expert mode  
- Video tab: add full API support  
- Control tab: add overrides handling  
- Engine: TensorRT acceleration

### New models / Pipelines

- [Inf-DiT](https://github.com/zai-org/Inf-DiT)
- [DiffSynth Studio](https://github.com/modelscope/DiffSynth-Studio)
- [IPAdapter negative guidance](https://github.com/huggingface/diffusers/discussions/7167)  
- [IPAdapter composition](https://huggingface.co/ostris/ip-composition-adapter)  
- [STG](https://github.com/huggingface/diffusers/blob/main/examples/community/README.md#spatiotemporal-skip-guidance)  
- [SmoothCache](https://github.com/huggingface/diffusers/issues/11135)  
- [MagCache](https://github.com/lllyasviel/FramePack/pull/673/files)  
- [Dream0 guidance](https://huggingface.co/ByteDance/DreamO)  
- [ByteDance OneReward](https://github.com/bytedance/OneReward)
- [ByteDance USO](https://github.com/bytedance/USO)
- [Video Inpaint Pipeline](https://github.com/huggingface/diffusers/pull/12506)
- [Krea Realtime Video](https://huggingface.co/krea/krea-realtime-video)
- [Wan-2.2 Animate](https://github.com/huggingface/diffusers/pull/12526)
- [Wan-2.2 S2V](https://github.com/huggingface/diffusers/pull/12258)
- [LongCat-Video](https://huggingface.co/meituan-longcat/LongCat-Video)
- [MUG-V 10B](https://huggingface.co/MUG-V/MUG-V-inference)
- [Chroma1 Radiance](https://huggingface.co/lodestones/Chroma1-Radiance)
- [Ovi](https://github.com/character-ai/Ovi)
- [Bytedance Lynx](https://github.com/bytedance/lynx)
- [Phantom HuMo](https://github.com/Phantom-video/Phantom)
- [Lumina-DiMOO](https://huggingface.co/Alpha-VLLM/Lumina-DiMOO)
- [Wan2.2-Animate-14B](https://huggingface.co/Wan-AI/Wan2.2-Animate-14B)
- [Magi](https://github.com/SandAI-org/MAGI-1)(https://github.com/huggingface/diffusers/pull/11713)  
- [SEVA](https://github.com/huggingface/diffusers/pull/11440)  
- [Ming](https://github.com/inclusionAI/Ming)  
- [Liquid](https://github.com/FoundationVision/Liquid)  
- [Step1X](https://github.com/stepfun-ai/Step1X-Edit)  
- [LucyEdit](https://github.com/huggingface/diffusers/pull/12340)
- [SD3 UltraEdit](https://github.com/HaozheZhao/UltraEdit)  
- [WAN2GP](https://github.com/deepbeepmeep/Wan2GP)  
- [SelfForcing](https://github.com/guandeh17/Self-Forcing)  
- [DiffusionForcing](https://github.com/kwsong0113/diffusion-forcing-transformer)  
- [LanDiff](https://github.com/landiff/landiff)  
- [HunyuanCustom](https://github.com/Tencent-Hunyuan/HunyuanCustom)  
- [HunyuanAvatar](https://huggingface.co/tencent/HunyuanVideo-Avatar)  
- [WAN-CausVid](https://huggingface.co/lightx2v/Wan2.1-T2V-14B-CausVid)  
- [WAN-CausVid-Plus t2v](https://github.com/goatWu/CausVid-Plus/)  
- [WAN-StepDistill](https://huggingface.co/lightx2v/Wan2.1-T2V-14B-StepDistill-CfgDistill)  

## Code TODO

> npm run todo
 
- control: support scripts via api
- fc: autodetect distilled based on model
- fc: autodetect tensor format based on model
- hypertile: vae breaks when using non-standard sizes
- install: switch to pytorch source when it becomes available
- loader: load receipe
- loader: save receipe
- lora: add other quantization types
- lora: add t5 key support for sd35/f1
- lora: maybe force imediate quantization
- model load: force-reloading entire model as loading transformers only leads to massive memory usage
- model load: implement model in-memory caching
- modernui: monkey-patch for missing tabs.select event
- modules/lora/lora_extract.py:188:9: W0511: TODO: lora: support pre-quantized flux
- modules/modular_guiders.py:65:58: W0511: TODO: guiders
- processing: remove duplicate mask params
- resize image: enable full VAE mode for resize-latent
