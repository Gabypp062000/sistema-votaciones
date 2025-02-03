import pandas as pd
import random
import string

archivo = "votacion.xlsx"
hoja = "Votación"

def generar_codigo():
    """Genera un código aleatorio único de 6 caracteres."""
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

def asignar_codigos():
    """Asigna un código único a cada persona en el archivo Excel."""
    df = pd.read_excel(archivo, sheet_name=hoja)

    for i in range(len(df)):
        df.at[i, "Código"] = generar_codigo()  # Asigna un código único
    
    df["Voto"] = ""  # Deja el campo de voto vacío
    df["Estado"] = "No votado"  # Marca como "No votado"

    df.to_excel(archivo, sheet_name=hoja, index=False)
    print("✅ Códigos asignados exitosamente.")

if __name__ == "__main__":
    asignar_codigos()
