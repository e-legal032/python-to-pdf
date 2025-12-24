from fpdf import FPDF
from PIL import Image
import os

# -----------------------------
# CONFIGURACIÓN
# -----------------------------

CARPETA_IMAGENES = "images"
PDF_SALIDA = "carousel-v02.pdf"
EXTENSIONES = (".jpg", ".jpeg", ".png")

# Espacio de corte visual (en puntos)
MARGEN_SUPERIOR = 40
MARGEN_INFERIOR = 40

# -----------------------------
# OBTENER LISTA DE IMÁGENES
# -----------------------------

imagenes = sorted([
    os.path.join(CARPETA_IMAGENES, archivo)
    for archivo in os.listdir(CARPETA_IMAGENES)
    if archivo.lower().endswith(EXTENSIONES)
])

if not imagenes:
    raise ValueError("No se encontraron imágenes en la carpeta.")

# -----------------------------
# CREAR PDF
# -----------------------------

pdf = FPDF(unit="pt")

for ruta in imagenes:
    with Image.open(ruta) as img:
        ancho, alto = img.size

    # Página un poco más alta que la imagen
    alto_pagina = alto + MARGEN_SUPERIOR + MARGEN_INFERIOR

    pdf.add_page(format=(ancho, alto_pagina))

    # (opcional) color de fondo neutro
    pdf.set_fill_color(245, 245, 245)
    pdf.rect(0, 0, ancho, alto_pagina, style="F")

    # Imagen centrada verticalmente
    pdf.image(
        ruta,
        x=0,
        y=MARGEN_SUPERIOR,
        w=ancho,
        h=alto
    )

# -----------------------------
# GUARDAR ARCHIVO
# -----------------------------

pdf.output(PDF_SALIDA)
print(f"PDF generado correctamente: {PDF_SALIDA}")
