import requests
import os
import re
from flask import Flask, redirect, url_for, render_template, request
from werkzeug.utils import secure_filename           # Used to store filename

app = Flask(__name__)


@app.route("/")
def uploader():
    path = 'static/uploads/'
    uploads = sorted(os.listdir(path), key=lambda x: os.path.getctime(
        path+x))        # Sorting as per image upload date and time
    print(uploads)
    #uploads = os.listdir('static/uploads')
    uploads = ['uploads/' + file for file in uploads]
    uploads.reverse()
    # Pass filenames to front end for display in 'uploads' variable
    return render_template("alzheimer.html", uploads=uploads)


app.config['UPLOAD_PATH'] = 'static/uploads'             # Storage path


@app.route("/upload", methods=['GET', 'POST'])
def upload_file():                                       # This method is used to upload files
    if request.method == 'POST':
        f = request.files['file']
        print(f.filename)
        # f.save(secure_filename(f.filename))
        filename = secure_filename(f.filename)
        f.save(os.path.join(app.config['UPLOAD_PATH'], filename))
        # Redirect to route '/' for displaying images on fromt end
        return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
