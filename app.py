# Autor: Jonathan Hernández
# Fecha: 12 Septiembre 2024
# Descripción: Código para procesamiento de imagenes con Sobel ( plantilla).
# GitHub: https://github.com/Jona163

from flask import Flask, render_template, request, redirect, url_for
import cv2
import numpy as np
import os
from werkzeug.utils import secure_filename
