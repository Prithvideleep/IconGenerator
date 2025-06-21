from diffusers import StableDiffusionPipeline
import torch

# Load model once when script starts
pipe = StableDiffusionPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5",
    torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32
)
pipe = pipe.to("cuda" if torch.cuda.is_available() else "cpu")

def generate_icon(prompt, style="flat vector icon", negative_prompt=None):
    final_prompt = f"{style} of {prompt}"
    image = pipe(final_prompt, negative_prompt=negative_prompt, guidance_scale=7.5).images[0]
    output_path = "output.png"
    image.save(output_path)
    return output_path