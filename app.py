from flask import Flask, render_template, request
import os

from modules.preprocessing import cargar_y_preprocesar_csv, ArchivoInvalidoError
from modules.model import entrenar_modelo
from modules.visualization import crear_grafico_real_vs_pred

app = Flask(__name__)

os.makedirs("static/images", exist_ok=True)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        if "file" not in request.files:
            raise ArchivoInvalidoError("No se envió ningún archivo")

        file = request.files["file"]

        if file.filename == "":
            raise ArchivoInvalidoError("Nombre de archivo vacío")

        df = cargar_y_preprocesar_csv(file)

        modelo, X_test, y_test = entrenar_modelo(df)
        y_pred = modelo.predict(X_test)

        crear_grafico_real_vs_pred(y_test, y_pred)

        return render_template("index.html", image="static/images/resultado.png")

    except ArchivoInvalidoError as e:
        return render_template("index.html", error=str(e))
    except Exception:
        return render_template("index.html", error="Ocurrió un error inesperado")
    finally:
        print("Proceso de predicción finalizado")

if __name__ == "__main__":
    app.run(debug=True)

