
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from diffusers import StableDiffusionPipeline
import torch
import uuid
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

os.makedirs("generated", exist_ok=True)

print("Loading Stable Diffusion model...")

pipe = StableDiffusionPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5",
    torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32
)

if torch.cuda.is_available():
    pipe = pipe.to("cuda")

class PromptRequest(BaseModel):
    prompt: str

@app.get("/")
def home():
    return {"message": "Artify Backend Running"}

@app.post("/generate")
async def generate_image(data: PromptRequest):
    prompt = data.prompt

    image = pipe(prompt).images[0]

    filename = f"{uuid.uuid4()}.png"
    path = f"generated/{filename}"

    image.save(path)

    return {
        "message": "Image generated successfully",
        "image_path": path
    }
