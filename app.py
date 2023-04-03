import os

import numpy
import pandas as pd
from flask import Flask, render_template, request

from pkgs.Model import Model

app = Flask(__name__)

@app.route('/')
def home():
    # Delete old files
    dir_name = "static/images/upload/"
    fuul_path = os.listdir(dir_name)
    for item in fuul_path:
        if item.endswith(".jpg"):
            os.remove(os.path.join(dir_name, item))

    return render_template("index.html", res="None")


@app.route('/predictcovid', methods=['POST'])
def predictcovid():
    # Delete old files
    dir_name = "static/images/upload/"
    fuul_path = os.listdir(dir_name)
    for item in fuul_path:
        if item.endswith(".jpg"):
            os.remove(os.path.join(dir_name, item))

    app_root = request.host_url

    file = request.files['img']
    filename = file.filename
    save_path = "{0}{1}".format("static/images/upload/", filename)
    file.save(save_path)

    model = Model()
    predict_covid = model.predict_covid(filename)

    return render_template("index.html", res="res", app_root=app_root)


if __name__ == '__main__':
    app.run()
