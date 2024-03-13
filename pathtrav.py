from flask import Flask, render_template
from flask import request, Response
import os

PEOPLE_FOLDER = os.path.join('static', '')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER

@app.route('/')
@app.route('/index')
def show_index():
    return render_template("index.html")

@app.route('/image')
def show_image():
    filename = request.args.get('filename')
    
    with open(filename, "rb") as f:
        content = f.read()

    return Response(content, mimetype='image/png')