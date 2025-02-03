import pandas as pd

# Nombre del archivo y hoja de Excel
archivo = "votacion.xlsx"
hoja = "Votación"

def cargar_datos():
    """Carga los datos del archivo Excel."""
    return pd.read_excel(archivo, sheet_name=hoja)

def guardar_datos(df):
    """Guarda los datos actualizados en Excel."""
    df.to_excel(archivo, sheet_name=hoja, index=False)

def votar(codigo, voto):
    """Registra un voto en el archivo Excel."""
    df = cargar_datos()
    
    # Buscar el código en la lista
    for i, row in df.iterrows():
        if row["Código"] == codigo:
            if row["Estado"] == "No votado":
                df.at[i, "Voto"] = voto
                df.at[i, "Estado"] = "Votado"
                guardar_datos(df)
                return "✅ Voto registrado con éxito"
            else:
                return "⚠️ Este código ya ha sido usado"
    
    return "❌ Código inválido"

# Prueba del sistema
if __name__ == "__main__":
    codigo_ingresado = input("Ingrese su código único: ")
    voto_ingresado = input("Ingrese su voto: ")
    print(votar(codigo_ingresado, voto_ingresado))
