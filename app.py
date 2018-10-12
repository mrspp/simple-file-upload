from flask import Flask, render_template, request, flash
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads/img'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = "fjsadf"
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
      flash('File uploaded!')
      return render_template('index.html')

if __name__ == '__main__':
   app.run(debug = True)