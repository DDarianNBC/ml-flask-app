from flask import Flask, render_template
import os
import pandas as pd

from modules.model import entrenar_modelo
from modules.visualization import crear_grafico_real_vs_pred

app = Flask(__name__)

# Carpeta para imágenes
os.makedirs("static/images", exist_ok=True)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict")
def predict():
    try:
        # --- DATOS DE PRUEBA INTERNOS ---
        df = pd.DataFrame({
            "feature1": [1,2,3,4,5],
            "feature2": [2,4,6,8,10],
            "target": [3,6,9,12,15]
        })

        # 1. Modelo
        modelo, X_test, y_test = entrenar_modelo(df)
        y_pred = modelo.predict(X_test)

        # 2. Visualización
        crear_grafico_real_vs_pred(y_test, y_pred)

        return render_template(
            "index.html",
            image="static/images/resultado.png"
        )

    except Exception as e:
        return render_template(
            "index.html",
            error=f"Ocurrió un error inesperado: {e}"
        )

if __name__ == "__main__":
    app.run(debug=True)
