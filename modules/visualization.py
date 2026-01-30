import plotly.express as px

def crear_grafico_real_vs_pred(y_test, y_pred):
    fig = px.scatter(x=y_test, y=y_pred, labels={"x":"Real", "y":"Predicción"})
    fig.write_image("static/images/resultado.png")


