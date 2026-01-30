def cargar_y_preprocesar_csv(file):
    try:
        df = pd.read_csv(file)

        if df.empty:
            raise ArchivoInvalidoError("El archivo CSV está vacío")

        # Limpieza básica
        df = df.dropna()

        # Forzar todo a numérico (opcional)
        df = df.apply(pd.to_numeric, errors='coerce')
        df = df.dropna()

        df = df.select_dtypes(include=["number"])

        if df.shape[1] < 2:
            raise ArchivoInvalidoError(
                "El CSV debe tener al menos dos columnas numéricas"
            )

        return df

    except ArchivoInvalidoError as e:
        raise e
    except Exception as e:
        raise ArchivoInvalidoError("Error al procesar el archivo") from e

