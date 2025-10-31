# TODO

## Project Board

- <https://github.com/users/vladmandic/projects>

## Internal

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

## Features

- [IPAdapter composition](https://huggingface.co/ostris/ip-composition-adapter)  
- [IPAdapter negative guidance](https://github.com/huggingface/diffusers/discussions/7167)  
- [MagCache](https://github.com/lllyasviel/FramePack/pull/673/files)  
- [SmoothCache](https://github.com/huggingface/diffusers/issues/11135)  
- [STG](https://github.com/huggingface/diffusers/blob/main/examples/community/README.md#spatiotemporal-skip-guidance)  
- [Video Inpaint Pipeline](https://github.com/huggingface/diffusers/pull/12506)

### New models / Pipelines

TODO: *Prioritize*!

- [Bria FIBO](https://huggingface.co/briaai/FIBO)
- [Bytedance Lynx](https://github.com/bytedance/lynx)
- [ByteDance OneReward](https://github.com/bytedance/OneReward)
- [ByteDance USO](https://github.com/bytedance/USO)
- [Chroma1 Radiance](https://huggingface.co/lodestones/Chroma1-Radiance)
- [DiffSynth Studio](https://github.com/modelscope/DiffSynth-Studio)
- [DiffusionForcing](https://github.com/kwsong0113/diffusion-forcing-transformer)  
- [Dream0 guidance](https://huggingface.co/ByteDance/DreamO)  
- [HunyuanAvatar](https://huggingface.co/tencent/HunyuanVideo-Avatar)  
- [HunyuanCustom](https://github.com/Tencent-Hunyuan/HunyuanCustom)  
- [Inf-DiT](https://github.com/zai-org/Inf-DiT)
- [Krea Realtime Video](https://huggingface.co/krea/krea-realtime-video)
- [LanDiff](https://github.com/landiff/landiff)  
- [Liquid](https://github.com/FoundationVision/Liquid)  
- [LongCat-Video](https://huggingface.co/meituan-longcat/LongCat-Video)
- [LucyEdit](https://github.com/huggingface/diffusers/pull/12340)
- [Lumina-DiMOO](https://huggingface.co/Alpha-VLLM/Lumina-DiMOO)
- [Magi](https://github.com/SandAI-org/MAGI-1)(https://github.com/huggingface/diffusers/pull/11713)  
- [Ming](https://github.com/inclusionAI/Ming)  
- [MUG-V 10B](https://huggingface.co/MUG-V/MUG-V-inference)
- [Ovi](https://github.com/character-ai/Ovi)
- [Phantom HuMo](https://github.com/Phantom-video/Phantom)
- [SD3 UltraEdit](https://github.com/HaozheZhao/UltraEdit)  
- [SelfForcing](https://github.com/guandeh17/Self-Forcing)  
- [SEVA](https://github.com/huggingface/diffusers/pull/11440)  
- [Step1X](https://github.com/stepfun-ai/Step1X-Edit)  
- [Wan-2.2 Animate](https://github.com/huggingface/diffusers/pull/12526)
- [Wan-2.2 S2V](https://github.com/huggingface/diffusers/pull/12258)
- [WAN-CausVid-Plus t2v](https://github.com/goatWu/CausVid-Plus/)  
- [WAN-CausVid](https://huggingface.co/lightx2v/Wan2.1-T2V-14B-CausVid)  
- [WAN-StepDistill](https://huggingface.co/lightx2v/Wan2.1-T2V-14B-StepDistill-CfgDistill)  
- [Wan2.2-Animate-14B](https://huggingface.co/Wan-AI/Wan2.2-Animate-14B)
- [WAN2GP](https://github.com/deepbeepmeep/Wan2GP)  

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
