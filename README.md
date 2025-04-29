# Multi-Image Fusion Generator 🚀

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-3.0%2B-brightgreen?logo=flask)
![OpenAI API](https://img.shields.io/badge/OpenAI-API-blueviolet?logo=openai)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

---

## 🖼️ Project Overview

**Multi-Image Fusion Generator** is a Flask-based web application that allows users to upload 3–5 reference images and an instruction prompt to generate a **single composite AI image**.

It uses **OpenAI's GPT-4 Vision** to describe uploaded images, and **DALL·E 3** to generate a creative and coherent fused output.

Built with a focus on modularity, clean architecture, and secure API usage.

---

## ✨ Features

- Upload 3–5 images via a simple web interface
- Input a custom prompt to guide the image fusion
- Vision-based captioning of uploaded images (GPT-4 Turbo / GPT-4o)
- Composite image generation (DALL·E 3 HD)
- Automatic image preprocessing (resize, format correction)
- Error handling for upload limits, API issues, and file validation
- Secure API key management using `.env` files
- Easy setup with clean modular codebase

---

## 📸 Demo

Example:  
> Upload 3–5 images → Enter prompt → View AI-generated fusion!

---

## 🚀 Tech Stack

- **Backend:** Python 3.8+, Flask 3.x
- **AI Services:** OpenAI GPT-4 Turbo (Vision), DALL·E 3
- **Image Processing:** Pillow
- **Environment Management:** python-dotenv
- **HTTP Requests:** requests

---

## 🛠️ Installation & Setup

Clone the repository:

```bash
git clone https://github.com/Amarnath001/Multi_Image_Generator.git
cd Multi_Image_Generator

# Windows
python -m venv venv
venv\\Scripts\\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate

Install the dependencies:

pip install -r req.txt

Create a .env file in the project root:

API_KEY=your-openai-api-key-here

Make sure the folders uploads/ and outputs/ exist (or will be created automatically).

Run the application:

python app.py

Open http://localhost:5000 in your browser.
⚠️ Important Note

    OpenAI API usage requires a paid account with billing enabled.

    Without GPT-4 Vision or DALL·E 3 access, full testing may not work.

    The code is structured for production-grade quality following OpenAI's API documentation.

📁 Project Structure

├── app.py                # Main Flask server
├── get_api.py             # OpenAI API interaction (GPT-4 Vision + DALL·E 3)
├── image_utils.py         # Image preprocessing helper
├── req.txt                # Python package requirements
├── templates/             # HTML pages (upload form + result page)
│   ├── index.html
│   └── result.html
├── uploads/               # Uploaded images (runtime)
├── outputs/               # Generated output images
├── README.md              # Project documentation
├── .env.example           # Example environment config

🧠 Future Improvements (Ideas)

    Integrate CLIP/BLIP to auto-generate image descriptions.

    Add user-selectable style fusion (choose style/background separately).

    Support Stable Diffusion as an alternative backend.

    Enable batch generation for multiple fused outputs.

