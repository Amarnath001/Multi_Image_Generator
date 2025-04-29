import os
from PIL import Image

def preprocess_images(image_paths, output_size=(512, 512)):
    processed_paths = []

    for path in image_paths:
        img = Image.open(path)
        img = img.convert("RGB")  # Ensure 3 color channels
        img = img.resize(output_size)  # Resize to 512x512 or whatever you want

        filename = os.path.basename(path)
        processed_path = os.path.join('uploads', f'processed_{filename}')
        img.save(processed_path)

        processed_paths.append(processed_path)

    return processed_paths
