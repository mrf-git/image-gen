image-gen
=========

Hosts a server to take a text prompt and generate an image.

## Local setup/build instructions

**Prerequisites**
* Docker
* GPU hardware
* Python
* VSCode

First create a directory under `base_image/` called `models/`.

Within this directory download the [ByteDance/SDXL-Lightning](https://huggingface.co/ByteDance/SDXL-Lightning/blob/main/sdxl_lightning_4step_unet.safetensors) model file.

Next create a directory under `models/` called `diffusion/` and download the
[stabilityai/stable-diffusion-xl-base-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0/tree/main) model files for fp16 pytorch safetensors.

Build the base_image container with the VSCode task, and then build and run the main docker image using the VSCode task.

