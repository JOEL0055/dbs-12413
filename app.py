from flask import Flask, render_template, request

app = Flask(__name__, template_folder="/Users/joelaiweithai/Downloads/BC3411/html/html_script")

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("finance.html")

if __name__ == "__main__":
    # Specify a different port
    app.run(port=5001)
