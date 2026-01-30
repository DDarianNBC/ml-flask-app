# modules/preprocessing.py
import pandas as pd

class ArchivoInvalidoError(Exception):
    """Excepción personalizada para archivos incorrectos"""
    pass

def cargar_y_preprocesar_csv(file):
    try:
        file.seek(0)
        df = pd.read_csv(file, encoding='utf-8', header=0)

        if df.empty:
            raise ArchivoInvalidoError("El archivo CSV está vacío")

        # Detectar columnas numéricas originales
        numeric_cols = df.select_dtypes(include='number').columns.tolist()

        # Intentar convertir a numérico cualquier otra columna, sin eliminar filas aún
        for col in df.columns:
            if col not in numeric_cols:
                df[col] = pd.to_numeric(df[col], errors='coerce')

        # Ahora seleccionar solo columnas numéricas
        df = df.select_dtypes(include='number')

        if df.shape[1] < 2:
            raise ArchivoInvalidoError("El CSV debe tener al menos dos columnas numéricas")

        # Eliminar filas con NaN solo al final
        df = df.dropna()

        return df

    except ArchivoInvalidoError as e:
        raise e
    except Exception as e:
        raise ArchivoInvalidoError(f"Error al procesar el archivo: {e}") from e

