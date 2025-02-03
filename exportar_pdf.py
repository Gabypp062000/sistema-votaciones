import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

archivo = "votacion.xlsx"
hoja = "Votación"
pdf_output = "reporte_votos.pdf"

def generar_reporte_pdf():
    df = pd.read_excel(archivo, sheet_name=hoja)
    conteo = df["Voto"].value_counts()

    c = canvas.Canvas(pdf_output, pagesize=letter)
    c.setFont("Helvetica", 14)
    c.drawString(100, 750, "📊 Resumen de Votos")
    
    y = 720
    for candidato, votos in conteo.items():
        c.drawString(100, y, f"{candidato}: {votos} votos")
        y -= 20
    
    c.save()
    print(f"✅ Reporte exportado como {pdf_output}")

if __name__ == "__main__":
    generar_reporte_pdf()
