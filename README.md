# Awesome FLUX Resources [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of awesome resources for FLUX, the state-of-the-art text-to-image model by Black Forest Labs, focusing on its growing ecosystem.

[View on GitHub](https://github.com/Eris2025/AwesomeFlux)

## Contents

- [Awesome FLUX Resources ](#awesome-flux-resources-)
  - [Contents](#contents)
  - [Official Resources](#official-resources)
  - [Models](#models)
    - [Fine-tuned Models and Loras](#fine-tuned-models-and-loras)
    - [Quantized Models](#quantized-models)
    - [Base Models API](#base-models-api)
  - [Community Projects](#community-projects)
  - [Demos](#demos)
  - [Contributing](#contributing)

## Official Resources

- [black-forest-labs/flux](https://github.com/black-forest-labs/flux) - This repo contains minimal inference code to run text-to-image and image-to-image with our Flux latent rectified flow transformers. Official repository released by Black Forest Labs.
- [Black Forest Labs](https://blackforestlabs.ai/) - Black Forest Labs official website.
- FLUX.1 [pro] -  the base model, available via API. API available on Replicate, FAL and Mystic.
- [FLUX.1-dev](https://huggingface.co/black-forest-labs/FLUX.1-dev) - Official model repository. guidance-distilled variant.
- [FLUX.1-schnell](https://huggingface.co/black-forest-labs/FLUX.1-schnell) - Official model repository. guidance and step-distilled variant.

## Models

### Fine-tuned Models and Loras

- [XLabs-AI/flux-RealismLora](https://huggingface.co/XLabs-AI/flux-RealismLora) - provides a checkpoint with trained LoRA photorealism for FLUX.1-dev model by Black Forest Labs.
- [XLabs-AI/flux-controlnet-collections](https://huggingface.co/XLabs-AI/flux-controlnet-collections) - This repository provides a collection of ControlNet checkpoints for FLUX.1-dev model by Black Forest Labs.
- [XLabs-AI/flux-controlnet-canny](https://huggingface.co/XLabs-AI/flux-controlnet-canny) - This repository provides a checkpoint with trained ControlNet Canny model for FLUX.1-dev model by Black Forest Labs.
- [alvdansen/frosting_lane_flux](https://huggingface.co/alvdansen/frosting_lane_flux) - Frosting Lane Flux Lora.
- [InstantX/FLUX.1-dev-Controlnet-Canny](https://huggingface.co/InstantX/FLUX.1-dev-Controlnet-Canny) - FLUX.1-dev ControlNet Canny model proposed and maintained by the InstantX team.
- [sayakpaul/FLUX.1-merged](https://huggingface.co/sayakpaul/FLUX.1-merged) - This repository provides the merged params for black-forest-labs/FLUX.1-dev and black-forest-labs/FLUX.1-schnell.

### Quantized Models

- [city96/FLUX.1-dev-gguf](https://huggingface.co/city96/FLUX.1-dev-gguf) - This is a direct GGUF conversion of black-forest-labs/FLUX.1-dev.
- [cocktailpeanut/flux1-merged-q8](https://huggingface.co/cocktailpeanut/flux1-merged-q8)
- [cocktailpeanut/flux1-schnell-q8](https://huggingface.co/cocktailpeanut/flux1-schnell-q8)
- [cocktailpeanut/flux1-schnell-qint8](https://huggingface.co/cocktailpeanut/flux1-schnell-qint8)

### Base Models API

Replicate:

- [flux collection](https://replicate.com/collections/flux)
- [flux pro](https://replicate.com/black-forest-labs/flux-pro)
- [flux dev](https://replicate.com/black-forest-labs/flux-dev)
- [flux schnell](https://replicate.com/black-forest-labs/flux-schnell)

FAL:

- [flux pro](https://fal.ai/models/fal-ai/flux-pro)
- [flux dev](https://fal.ai/models/fal-ai/flux/dev)
- [flux schnell](https://fal.ai/models/fal-ai/flux/schnell)

Mystic:

- [black-forest-labs collection](https://www.mystic.ai/black-forest-labs)
- [flux pro](https://www.mystic.ai/black-forest-labs/flux1-pro)
- [flux dev](https://www.mystic.ai/black-forest-labs/flux1-dev)
- [flux schnell](https://www.mystic.ai/black-forest-labs/flux1-schnell)

## Community Projects

- [XLabs-AI/x-flux](https://github.com/XLabs-AI/x-flux) - This repository provides training scripts for Flux model by Black Forest Labs.
- [filipstrand/mflux](https://github.com/filipstrand/mflux) - MFLUX (MacFLUX) is a line-by-line port of the FLUX implementation in the Huggingface Diffusers library to Apple MLX. Run the powerful FLUX models from Black Forest Labs locally on your Mac.
- [camenduru/flux-jupyter](https://github.com/camenduru/flux-jupyter) - Jupyter Notebooks to run FLUX models.
- [XLabs-AI/x-flux-comfyui](https://github.com/XLabs-AI/x-flux-comfyui) - Flux ComfyUI nodes.
- [ataylorm/FluxAIGridComparisons](https://github.com/ataylorm/FluxAIGridComparisons) - A collection of various image grids created with Flux. Things like hair styles, clothing, nationalities, ages, etc.
- [Ling-APE/ComfyUI-All-in-One-FluxDev-Workflow](https://github.com/Ling-APE/ComfyUI-All-in-One-FluxDev-Workflow) - An FluxDev workflow in ComfyUI that combines various techniques for generating images with the FluxDev model, including img-to-img and text-to-img. .
- [fairy-root/Flux-Prompt-Generator](https://github.com/fairy-root/Flux-Prompt-Generator) -  A ComfyUI node that provides a flexible and customizable prompt generator for generating detailed and creative prompts for image generation models.

## Demos

- [FLUX.1-schnell](https://huggingface.co/spaces/black-forest-labs/FLUX.1-schnell) - Official FLUX.1 [schnell] demo on huggingface, 12B param rectified flow transformer distilled from FLUX.1 [pro] for 4 step generation.
- [FLUX.1-dev](https://huggingface.co/spaces/black-forest-labs/FLUX.1-dev) - Official FLUX.1 [dev] demo on huggingface, 12B param rectified flow transformer guidance-distilled from FLUX.1 [pro].
- [FLUX.1-merged](https://huggingface.co/spaces/multimodalart/FLUX.1-merged) - Merge by Sayak Paul of 2 of the 12B param rectified flow transformers FLUX.1 [dev] and FLUX.1 [schnell] by Black Forest Labs.
- [FLUX.1-inpaint](https://huggingface.co/spaces/SkalskiP/FLUX.1-inpaint)
- [FLUX LoRA the Explorer](https://huggingface.co/spaces/multimodalart/flux-lora-the-explorer)
- [FLUX Prompt Generator](https://huggingface.co/spaces/gokaygokay/FLUX-Prompt-Generator) - Create long prompts from images or simple words. Enhance your short prompts with prompt enhancer.
- [Flux RealismLora Image Generator](https://huggingface.co/spaces/DamarJati/FLUX.1-RealismLora)

## Contributing

Contributions welcome! Read the [contribution guidelines](https://github.com/Eris2025/awesome-flux/blob/main/.github/CONTRIBUTING.md) first.