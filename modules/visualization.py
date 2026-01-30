import plotly.express as px
import pandas as pd

def crear_grafico_real_vs_pred(y_real, y_pred):
    """
    Crea un gráfico interactivo Real vs Predicción
    y lo guarda como PNG.
    """
    df = pd.DataFrame({
        "Valor real": y_real,
        "Predicción": y_pred
    })

    fig = px.scatter(
        df,
        x="Valor real",
        y="Predicción",
        title="Valores reales vs Predicción",
        trendline="ols"
    )

    # Guardar imagen
    fig.write_image("static/images/resultado.png")

    return fig
