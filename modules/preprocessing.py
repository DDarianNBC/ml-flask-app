# modules/preprocessing.py
import pandas as pd

class ArchivoInvalidoError(Exception):
    """Excepción personalizada para archivos incorrectos"""
    pass

def cargar_y_preprocesar_csv(file):
    try:
        # Leer CSV como texto (utf-8) desde Flask
        file.seek(0)  # Asegurarse de empezar desde el inicio del archivo
        df = pd.read_csv(file, encoding='utf-8', header=0)

        if df.empty:
            raise ArchivoInvalidoError("El archivo CSV está vacío")

        # Convertir todas las columnas a numérico, ignorando errores
        for col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')

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
        raise ArchivoInvalidoError(f"Error al procesar el archivo: {e}") from e
