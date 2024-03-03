import torch
from diffusers import StableDiffusionXLPipeline, UNet2DConditionModel, EulerDiscreteScheduler
from safetensors.torch import load_file

MODEL_PIPELINE = None

def load_models():
    global MODEL_PIPELINE
    if not MODEL_PIPELINE:
        unet = UNet2DConditionModel.from_config("/models/diffusion", subfolder="unet").to("cuda", torch.float16)
        unet.load_state_dict(load_file("/models/sdxl_lightning_4step_unet.safetensors", device="cuda"))
        pipe = StableDiffusionXLPipeline.from_pretrained("/models/diffusion", unet=unet, torch_dtype=torch.float16, variant="fp16").to("cuda")
        pipe.scheduler = EulerDiscreteScheduler.from_config(pipe.scheduler.config, timestep_spacing="trailing")
        MODEL_PIPELINE = pipe
        print("Loaded model.")
