from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/fotos")
def fotos():
    return render_template("fotos.html")

@app.route("/frases")
def frases():
    return render_template("frases.html")

if __name__ == "__main__":
    app.run(debug=True)
