# =============================================================================
# 1️⃣ LIBRERÍAS
# =============================================================================
import requests
from bs4 import BeautifulSoup
import pandas as pd

# =============================================================================
# 2️⃣ OBTENER HTML
# =============================================================================
url = "https://www.mercadolibre.com.mx/ofertas/novedades-de-temporada"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# =============================================================================
# 3️⃣ EXTRAER DATOS
# =============================================================================
titulos = soup.find_all("a", class_="poly-component__title")

# 👇 precio original (ANTES)
precios = soup.find_all("s", class_="andes-money-amount")

# =============================================================================
# 4️⃣ GUARDAR EN ARREGLO
# =============================================================================
productos = []

for i in range(len(titulos)):

    nombre = titulos[i].text.strip()

    precio = precios[i].text.strip() if i < len(precios) else "No disponible"

    productos.append([nombre, precio])

# =============================================================================
# 5️⃣ CONVERTIR A DATAFRAME
# =============================================================================
df = pd.DataFrame(productos, columns=["Producto", "Precio Antes"])

print(df)

# =============================================================================
# 6️⃣ GUARDAR CSV
# =============================================================================
df.to_csv("productos_mercadolibre.csv", index=False, encoding="utf-8")

print("✅ CSV creado: productos_mercadolibre.csv")