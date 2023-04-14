from flask import Flask, render_template, request
from compatibility import calculate_compatibility

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    compatibility = None
    if request.method == "POST":
        mbti1 = request.form["mbti1"].upper()
        mbti2 = request.form["mbti2"].upper()
        compatibility = calculate_compatibility(mbti1, mbti2)
    return render_template("index.html", compatibility=compatibility)

if __name__ == "__main__":
    app.run(debug=True)
