from flask import Flask, render_template, request, redirect, url_for
import pandas as pd

app = Flask(__name__)

archivo = "votacion.xlsx"  # Archivo de Excel donde están los candidatos y votos

def obtener_candidatos_por_cargo(cargo):
    """Devuelve una lista de candidatos según el cargo seleccionado."""
    df = pd.read_excel(archivo, sheet_name="Candidatos")
    return df[df["Cargo"] == cargo]["Nombre del Candidato"].tolist()

@app.route("/", methods=["GET", "POST"])
def index():
    cargos = ["Presidencia", "Vicepresidencia", "Secretaría", "Tesorería", "Vocal 1", "Vocal 2", "Vocal 3"]
    seleccion_cargo = request.form.get("cargo", "Presidencia")
    candidatos = obtener_candidatos_por_cargo(seleccion_cargo)

    if request.method == "POST" and "candidato" in request.form:
        voto = request.form.get("candidato")
        if voto:
            df_votos = pd.read_excel(archivo, sheet_name="Votos")
            df_votos = df_votos.append({"Cargo": seleccion_cargo, "Candidato": voto}, ignore_index=True)
            df_votos.to_excel(archivo, sheet_name="Votos", index=False)
            return redirect(url_for("index"))

    return render_template("index.html", cargos=cargos, seleccion_cargo=seleccion_cargo, candidatos=candidatos)

if __name__ == "__main__":
    app.run(debug=True)
