from flask import Flask
from flask import Blueprint, render_template, request

import os

web_app = Flask(__name__)

web_app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(web_app.config['UPLOAD_FOLDER'], exist_ok=True)

routes = Blueprint("routes", __name__)

@routes.route("/", methods = ["GET", "POST"])
def home_page():
    return render_template("my_patients.html")

@routes.route('/uploader', methods=['POST'])
def uploader():
    if request.method == 'POST':
        f = request.files['file']
        if f and (f.filename.endswith('.nii') or f.filename.endswith('.nii.gz')):
            filepath = os.path.join(web_app.config['UPLOAD_FOLDER'], f.filename)
            f.save(filepath)

            #TODO: on success case, we will not move to the new folder. We have to call our model to perform segmentation

            return f"File {f.filename} uploaded successfully!"
        else:
            return "Please upload a valid NIFTI file (.nii or .nii.gz)."