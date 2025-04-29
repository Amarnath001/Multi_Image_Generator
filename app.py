from flask import Flask, request, jsonify, render_template, redirect, url_for
import os
from image_utils import preprocess_images
from get_api import generate_composite_image
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
OUTPUT_FOLDER = 'outputs'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['OUTPUT_FOLDER'] = OUTPUT_FOLDER

# Home page route
@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

# Generate route
@app.route('/generate', methods=['POST'])
def generate():
    images = request.files.getlist('images')
    prompt = request.form.get('prompt')

    if not images or len(images) < 3:
        return "Upload at least 3 images.", 400

    # Save images
    image_paths = []
    for img in images:
        path = os.path.join(app.config['UPLOAD_FOLDER'], img.filename)
        img.save(path)
        image_paths.append(path)

    try:
        output_path = os.path.join(app.config['OUTPUT_FOLDER'], 'composite.png')
        generate_composite_image(image_paths, prompt, output_path)
        return redirect(url_for('result', filename='composite.png'))
    except Exception as e:
        return f"Generation Error: {str(e)}", 500

# Result page route
@app.route('/result/<filename>')
def result(filename):
    return render_template('result.html', filename=filename)

# Serving outputs folder for images
from flask import send_from_directory

@app.route('/outputs/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['OUTPUT_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)
