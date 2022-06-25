from flask import Flask, jsonify, send_file, redirect, render_template, current_app
import os
# flask set up
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = "/static/resources"


@app.route("/")
def home():
    return render_template("homepage.html")


@app.route("/download/<file>")
def download(file):
    return send_file(f"{current_app.root_path + app.config['UPLOAD_FOLDER']}/{file}")


if __name__ == "__main__":
    app.run(debug=True)
