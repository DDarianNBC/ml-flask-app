# modules/preprocessing.py
import pandas as pd

class ArchivoInvalidoError(Exception):
    """Excepción personalizada para archivos incorrectos"""
    pass

def cargar_y_preprocesar_csv(file):
    try:
        df = pd.read_csv(file)

        if df.empty:
            raise ArchivoInvalidoError("El archivo CSV está vacío")

        # Forzar todo a numérico, ignorando errores
        df = df.apply(pd.to_numeric, errors='coerce')

        # Eliminar filas con NaN
        df = df.dropna()

        # Solo columnas numéricas
        df = df.select_dtypes(include=["number"])

        if df.shape[1] < 2:
            raise ArchivoInvalidoError("El CSV debe tener al menos dos columnas numéricas")

        return df

    except ArchivoInvalidoError as e:
        raise e
    except Exception as e:
        raise ArchivoInvalidoError("Error al procesar el archivo") from e
