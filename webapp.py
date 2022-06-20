from flask import (
    Flask,
    jsonify,
    redirect,
    render_template
)

# flask set up
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("homepage.html")


if __name__ == "__main__":
    app.run(debug=True)
