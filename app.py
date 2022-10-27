from flask import Flask, render_template, request
from model import img_input
import os

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/process', methods=['POST'])
def process():
    imagefile = request.files.get('image')
    full_name = os.path.join(os.getcwd(), 'files', imagefile.filename)
    imagefile.save(full_name)
    return str(img_input(full_name))