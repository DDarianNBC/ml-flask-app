# modules/visualization.py
import plotly.express as px
import os

def crear_grafico_real_vs_pred(y_test, y_pred):
    # Crear DataFrame para gráfico
    import pandas as pd
    df_plot = pd.DataFrame({"Real": y_test, "Predicción": y_pred})

    # Gráfico de dispersión
    fig = px.scatter(df_plot, x="Real", y="Predicción",
                     title="Real vs Predicción",
                     labels={"Real": "Valores Reales", "Predicción": "Predicción del Modelo"})

    # Guardar en static/images
    os.makedirs("static/images", exist_ok=True)
    fig.write_image("static/images/resultado.png")

