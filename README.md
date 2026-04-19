# Unir múltiples PDFs (Herramienta Oscilandoo)

Esto te permite unir todos los archivos PDF de una carpeta en un solo documento, sin límites de cantidad ni tamaño.  
Ideal si tienes libros separados por capítulos o muchos archivos que necesitas juntar en uno solo.

---

## Previamente necesitas

- Tener Python instalado  
- Instalar la librería `pypdf`  

Esto lo haces en el terminal (el cuadrito de abajo en VS Code), escribiendo: pip install pypdf

---

## Paso 1: Preparar tus archivos

1. Crea una carpeta en tu computador  
2. Guarda TODOS los PDFs dentro de esa carpeta  
3. Asegúrate de que estén ordenados correctamente  

### IMPORTANTE: nombres de archivos

Para evitar errores en el orden, nómbralos así:

- 01_capitulo.pdf
- 02_capitulo.pdf
- 03_capitulo.pdf
...

❌ Evita esto:
- 1.pdf
- 2.pdf
- 10.pdf
(porque se ordenan mal)

---

## Paso 2: Configurar el código

1. Abre el archivo `libro_final.py`  
2. Busca esta línea:

```python
carpeta_pdfs = r"C:\Users\xxxxxxxxx\xxxxxx\xxxxxxx\xxxxxxx"
```
Reemplázala con la ruta de tu carpeta

## Paso 3: Ejecutar el script

Ejecuta:

- python libro_final.py

## Resultado

Se generará automáticamente un archivo:

- libro_completo.pdf

en la misma carpeta donde están tus PDFs.

## Tips
- Si el orden no queda bien, revisa los nombres de los archivos (usa 01, 02, 03...)
- Puedes agregar una portada como 00_portada.pdf para que aparezca al inicio
- Asegúrate de que todos los archivos sean realmente .pdf (a veces están mal renombrados)
- Si el código no hace nada, revisa que la ruta esté bien escrita y que los PDFs estén dentro de esa carpeta
- Evita usar carpetas vacías o sin PDFs
- Puedes usarlo para libros, guías, apuntes, etc.
- Si tienes muchos archivos, el proceso puede tardar unos segundos (es normal)

Creado por @oscilandoo 💖
