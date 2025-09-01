import requests
from bs4 import BeautifulSoup
import csv
import re


URL = "https://webscraper.io/test-sites/e-commerce/static/computers/laptops"


filepath = "C:/Users/user/Downloads/laptops.csv"  # Ganti sesuai lokasi kamu


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}
response = requests.get(URL, headers=headers)
response.raise_for_status()


soup = BeautifulSoup(response.text, 'html.parser')
products = soup.select('div.thumbnail')


data = []

for product in products:
    title = product.select_one('a.title')
    description = product.select_one('p.description')
    price = product.select_one('h4.price')

    
    brand = title.get_text(strip=True).split()[0] if title else ""
    spec = description.get_text(strip=True) if description else ""
    raw_price = price.get_text(strip=True).replace('$', '').replace('.', ',') if price else ""


    hdd = ""
    screen_size = ""


    screen_match = re.match(r'^(\d{1,2}[.,]?\d*)["”]', spec)
    if screen_match:
        screen_size = screen_match.group(1).replace('.', ',')

   
    hdd_match = re.search(r'(\d{3,4})GB', spec)
    if hdd_match:
        hdd = hdd_match.group(1)
    elif '1TB' in spec:
        hdd = '1024'

   
    data.append({
        "Brand": brand,
        "Spec": spec,
        "HDD": hdd,
        "Screen_Size": screen_size,
        "Price": raw_price
    })


with open(filepath, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=["Brand", "Spec", "HDD", "Screen_Size", "Price"])
    writer.writeheader()
    writer.writerows(data)

print(f"✅ CSV berhasil disimpan ke: {filepath}")

