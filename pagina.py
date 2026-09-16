from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/fotos")
def fotos():
    return render_template("fotos.html")

@app.route("/carta")
def carta():
    return render_template("carta.html")

@app.route("/frases")
def frases():
    return render_template("frases.html")

@app.route("/contador")
def contador():
    return render_template("contador.html")

@app.route("/musica")
def musica():
    return render_template("musica.html")

@app.route("/final")
def final():
    return render_template("final.html")

@app.route("/detalles")
def detalles():
    return render_template("detalles.html")

if __name__ == "__main__":
    app.run(debug=True)

