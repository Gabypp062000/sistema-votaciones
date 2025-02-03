import tkinter as tk
from tkinter import ttk
import pandas as pd

archivo = "votacion.xlsx"  # Nombre del archivo Excel

def obtener_candidatos_por_cargo(cargo):
    """Devuelve una lista de candidatos según el cargo seleccionado."""
    try:
        df_candidatos = pd.read_excel(archivo, sheet_name="Candidatos")
        return df_candidatos[df_candidatos["Cargo"] == cargo]["Nombre del Candidato"].tolist()
    except Exception as e:
        print(f"❌ Error al cargar candidatos: {e}")
        return ["Error al cargar candidatos"]

def actualizar_lista_candidatos(event):
    """Actualiza la lista de candidatos según el cargo seleccionado."""
    cargo_seleccionado = cargo_var.get()
    lista_candidatos = obtener_candidatos_por_cargo(cargo_seleccionado)
    voto_combo["values"] = lista_candidatos
    voto_combo.current(0) if lista_candidatos else voto_combo.set("No hay candidatos")

# Crear ventana principal
root = tk.Tk()
root.title("Sistema de Votación")
root.geometry("400x250")

# Cargos disponibles
cargos_disponibles = ["Presidencia", "Vicepresidencia", "Secretaría", "Tesorería", "Vocal 1", "Vocal 2", "Vocal 3"]

# Selección de cargo
tk.Label(root, text="Seleccione el cargo:").grid(row=0, column=0, padx=10, pady=5)
cargo_var = tk.StringVar(value=cargos_disponibles[0])
cargo_combo = ttk.Combobox(root, textvariable=cargo_var, values=cargos_disponibles)
cargo_combo.grid(row=0, column=1, padx=10, pady=5)
cargo_combo.bind("<<ComboboxSelected>>", actualizar_lista_candidatos)

# Selección de candidato
tk.Label(root, text="Seleccione su voto:").grid(row=1, column=0, padx=10, pady=5)
voto_var = tk.StringVar()
voto_combo = ttk.Combobox(root, textvariable=voto_var, values=obtener_candidatos_por_cargo(cargos_disponibles[0]))
voto_combo.grid(row=1, column=1, padx=10, pady=5)
voto_combo.current(0)

# Botón para registrar voto
def registrar_voto():
    cargo = cargo_var.get()
    candidato = voto_var.get()
    if candidato and candidato != "No hay candidatos":
        print(f"✅ Voto registrado para {candidato} en {cargo}")
    else:
        print("⚠️ Seleccione un candidato válido.")

tk.Button(root, text="Registrar Voto", command=registrar_voto).grid(row=2, column=0, columnspan=2, pady=10)

root.mainloop()
