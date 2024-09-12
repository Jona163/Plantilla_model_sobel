# Autor: Jonathan Hernández
# Fecha: 12 Septiembre 2024
# Descripción: Código para procesamiento de imagenes con Sobel ( plantilla).
# GitHub: https://github.com/Jona163

from flask import Flask, render_template, request, redirect, url_for
import cv2
import numpy as np
import os
from werkzeug.utils import secure_filename


app = Flask(__name__)

# Carpeta donde se almacenan las imágenes subidas y procesadas
UPLOAD_FOLDER = 'static/img/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Rutas permitidas para cargar
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'txt'}

@app.route('/')
def index():
    """ Página principal con el formulario para subir imágenes o archivos .txt """
    return render_template('index.html')

    return render_template('index.html', original_file=filename, result_image=result_image_path, file_content=file_content, result_type=result_type, error_message=error_message)

if __name__ == '__main__':
    app.run(debug=True)

