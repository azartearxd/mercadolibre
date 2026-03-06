
import requests
from bs4 import BeautifulSoup
import pandas as pd


url = "https://www.mercadolibre.com.mx/ofertas/novedades-de-temporada"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")


titulos = soup.find_all("a", class_="poly-component__title")


precios = soup.find_all("s", class_="andes-money-amount")


productos = []

for i in range(len(titulos)):

    nombre = titulos[i].text.strip()

    precio = precios[i].text.strip() if i < len(precios) else "No disponible"

    productos.append([nombre, precio])


df = pd.DataFrame(productos, columns=["Producto", "Precio Antes"])

print(df)


df.to_csv("productos_mercadolibre.csv", index=False, encoding="utf-8")


