import pandas as pd

class ArchivoInvalidoError(Exception):
    pass

def cargar_y_preprocesar_csv(file):
    try:
        # Leer CSV correctamente, usando la primera fila como encabezado
        df = pd.read_csv(file, header=0)

        if df.empty:
            raise ArchivoInvalidoError("El archivo CSV está vacío")

        # Convertir solo las columnas existentes (sin tocar encabezado)
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
        raise ArchivoInvalidoError("Error al procesar el archivo") from e
