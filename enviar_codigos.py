import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_USER = "TU_CORREO@gmail.com"
EMAIL_PASS = "TU_CONTRASEÑA"

archivo = "votacion.xlsx"
hoja = "Votación"

def enviar_codigo(destinatario, nombre, codigo):
    """Envía un correo con el código de votación."""
    asunto = "Tu Código de Votación"
    cuerpo = f"Hola {nombre},\n\nTu código único para votar es: {codigo}\n\nPor favor, guárdalo y úsalo una sola vez.\n\nGracias por participar."

    msg = MIMEMultipart()
    msg["From"] = EMAIL_USER
    msg["To"] = destinatario
    msg["Subject"] = asunto
    msg.attach(MIMEText(cuerpo, "plain"))

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_USER, EMAIL_PASS)
        server.sendmail(EMAIL_USER, destinatario, msg.as_string())
        server.quit()
        print(f"✅ Código enviado a {destinatario}")
    except Exception as e:
        print(f"❌ Error enviando código a {destinatario}: {e}")

def enviar_codigos():
    """Envía códigos a todos los votantes registrados."""
    df = pd.read_excel(archivo, sheet_name=hoja)
    
    for _, row in df.iterrows():
        if pd.notna(row["Correo"]) and pd.notna(row["Código"]):
            enviar_codigo(row["Correo"], row["Nombre"], row["Código"])

if __name__ == "__main__":
    enviar_codigos()
