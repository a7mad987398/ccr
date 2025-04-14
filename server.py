from flask import Flask, request, send_file, redirect
import os
from datetime import datetime
from werkzeug.utils import secure_filename

app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    return send_file('index.html')

@app.route('/capture', methods=['POST'])
def capture():
    if 'image' not in request.files:
        return "No image", 400

    image = request.files['image']
    if image.filename == '':
        return "No selected file", 400

    # Save image with secure filename and timestamp
    filename = f"consent_capture_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
    filename = secure_filename(filename)

    # Ensure the directory exists
    save_dir = os.path.join(app.static_folder, 'captures')
    os.makedirs(save_dir, exist_ok=True)
    image.save(os.path.join(save_dir, filename))
    return "Capture saved", 200

if __name__ == '__main__':
    app.run(port=8000, ssl_context='adhoc')
