import openai
import base64
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("API_KEY"))

def describe_images(image_paths):
    """Analyzes images using GPT-4 Turbo with Vision"""
    descriptions = []
    for path in image_paths:
        with open(path, "rb") as img_file:
            base64_image = base64.b64encode(img_file.read()).decode("utf-8")
        
        response = client.chat.completions.create(
            model="gpt-4-turbo-preview",  # Updated model name (or "gpt-4o")
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": "Describe this image in detail for an AI image generator."},
                        {"type": "image_url", "image_url": f"data:image/jpeg;base64,{base64_image}"},
                    ],
                }
            ],
            max_tokens=300,
        )
        descriptions.append(response.choices[0].message.content)
    return "\n".join(descriptions)

def generate_composite_image(image_paths, user_prompt, output_path):
    """Generates composite image using DALL·E 3"""
    try:
        image_descriptions = describe_images(image_paths)
        
        composite_prompt = f"""
        Create a SINGLE composite image that combines:
        {user_prompt}
        
        Image References:
        {image_descriptions}
        """
        
        response = client.images.generate(
            model="dall-e-3",
            prompt=composite_prompt,
            size="1024x1024",
            quality="hd",
            response_format="b64_json",
            n=1,
        )
        
        with open(output_path, "wb") as f:
            f.write(base64.b64decode(response.data[0].b64_json))
            
    except Exception as e:
        raise RuntimeError(f"API Error: {str(e)}")
