from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/saludar", methods=["POST"])
def saludar():
    nombre = request.form["nombre"]
    # getlist captura múltiples casillas seleccionadas con el mismo 'name'
    pasatiempos = request.form.getlist("pasatiempos") 
    descripcion = request.form.get("descripcion", "")
    
    return render_template(
        "saludar.html",
        nombre=nombre,
        pasatiempos=pasatiempos,
        descripcion=descripcion
    )

if __name__ == "__main__":
    app.run(debug=True)