# modules/model.py
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

def entrenar_modelo(df):
    """
    Entrena un modelo de regresión lineal.
    Usa la última columna como variable objetivo (y)
    y todas las demás como features (X)
    """
    if df.shape[1] < 2:
        raise ValueError("El DataFrame debe tener al menos 2 columnas")

    X = df.iloc[:, :-1]
    y = df.iloc[:, -1]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    modelo = LinearRegression()
    modelo.fit(X_train, y_train)

    return modelo, X_test, y_test
