from pypdf import PdfWriter
import os
import re

# Carpeta donde están tus PDFs
carpeta_pdfs = r"C:\Users\xxxxxxxx\xxxxxxx\xxxxxxx\xxxxxxx" #Aqui va la ruta de dónde tengas la carpeta con los archivos

# Nombre del archivo final
salida = os.path.join(carpeta_pdfs, "libro_completo.pdf")

# Obtener todos los PDFs de la carpeta
archivos_pdf = [f for f in os.listdir(carpeta_pdfs) if f.lower().endswith(".pdf")]

# Ordenar por número en el nombre (ej: cap1, cap2, cap10)
def extraer_numero(nombre):
    numeros = re.findall(r'\d+', nombre)
    return int(numeros[0]) if numeros else float("inf")

archivos_pdf.sort(key=extraer_numero)

merger = PdfWriter()

for archivo in archivos_pdf:
    ruta_pdf = os.path.join(carpeta_pdfs, archivo)
    merger.append(ruta_pdf)
    print(f"Agregado: {archivo}")

with open(salida, "wb") as f:
    merger.write(f)

merger.close()

print(f"\nPDF final creado en:\n{salida}")
