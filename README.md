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

