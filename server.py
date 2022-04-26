from random import randint
from flask import Flask, render_template, request, url_for
from pathlib import Path
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route("/", methods=["POST","GET"])
def multiply():
    if request.method == "GET":
        x = randint(1, 100)
        y = randint(1, 100)
        return {"randint": x * y,
                "start processing": "make a POST request with an image of a suspected deer to /",
                "list images": "/list-images"}
    elif request.method == "POST":
        f = request.files["the_file"]
        f.save(f"/var/www/viltkamera.lugash.se/static/images/{secure_filename(f.filename)}")
        return {"filename": f.filename, "status": "uploaded"}

@app.route("/list-images")
def listImages():
    imageHandle = Path("static/images")
    tmpList = ["images/" + image.name for image in imageHandle.iterdir()]
    print(tmpList[0])
    return render_template("imageList.html", imageList=tmpList)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
