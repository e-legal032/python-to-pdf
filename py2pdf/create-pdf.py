from fpdf import FPDF
from PIL import Image
import os

# -----------------------------
# CONFIGURACIÓN
# -----------------------------

# Carpeta donde están las imágenes
CARPETA_IMAGENES = "images"

# Nombre del PDF de salida
PDF_SALIDA = "carousel.pdf"

# Extensiones permitidas
EXTENSIONES = (".jpg", ".jpeg", ".png")

# -----------------------------
# OBTENER LISTA DE IMÁGENES
# -----------------------------

imagenes = sorted([
    os.path.join(CARPETA_IMAGENES, archivo)
    for archivo in os.listdir(CARPETA_IMAGENES)
    if archivo.lower().endswith(EXTENSIONES)
])

# Validación simple
if not imagenes:
    raise ValueError("No se encontraron imágenes en la carpeta.")

# -----------------------------
# CREAR PDF
# -----------------------------

pdf = FPDF(unit="pt")

for ruta in imagenes:
    img = Image.open(ruta)
    ancho, alto = img.size

    # Cada imagen ocupa una página completa
    pdf.add_page(format=(ancho, alto))
    pdf.image(ruta, 0, 0, ancho, alto)

# -----------------------------
# GUARDAR ARCHIVO
# -----------------------------

pdf.output(PDF_SALIDA)

print(f"PDF generado correctamente: {PDF_SALIDA}")
