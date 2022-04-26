from random import randint
from flask import Flask, render_template, request
from pathlib import Path

app = Flask(__name__)

@app.route("/", methods=["POST","GET"])
def multiply():
    if request.method == "GET":
        # Show the default
        x = randint(1, 100)
        y = randint(1, 100)
        return render_template("index.html", integer=str(x * y))
    elif request.method == "POST":
        # An image was uploaded
        return {"filename": "exampleName.jpg", "status": "uploaded"}

@app.route("/list-images")
def listImages():
    imageHandle = Path("images")
    return render_template("imageList.html", imageList=imageHandle.iterdir())

if __name__ == "__main__":
    app.run(host="0.0.0.0")
