
# Detailed Project Explanation

## Backend

FastAPI backend receives prompts from frontend.

Endpoint:
POST /generate

Flow:
1. Receive prompt
2. Send prompt to Stable Diffusion model
3. AI generates image
4. Save image
5. Return image path

---

## Frontend

React frontend:
- Takes prompt input
- Sends API request
- Displays image

---

## AI Model

Model:
runwayml/stable-diffusion-v1-5

This is a pretrained large generative AI model trained on billions of image-text pairs.

It understands:
- Objects
- Colors
- Art styles
- Realistic scenes
- Human language prompts

---

## Viva Questions

Q1. Why Stable Diffusion?
- Open source
- High quality generation
- Industry standard

Q2. Why FastAPI?
- Fast
- Lightweight
- Async support

Q3. Difference between GAN and Diffusion?
- GAN uses generator-discriminator competition
- Diffusion gradually denoises noise

Q4. What are limitations?
- GPU heavy
- Slow on CPU
- Ethical misuse possible

