import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv


#convertion

load_dotenv()
API_KEY = os.getenv("EXCHANGE_API_KEY")

from_currency = "GBP"  
to_currency = "KES"    

print(f"Fetching exchange rate for {from_currency} to {to_currency}...")
api_url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{from_currency}"

response = requests.get(api_url)

if response.status_code == 200:
    data = response.json()
    
    exchange_rate = data["conversion_rates"][to_currency]
    print(f"Success 1 {from_currency} = {exchange_rate} {to_currency}\n")
else:
    print("Failed to get exchange rate.")
    exchange_rate = 0 



# scrapping books

url = "https://books.toscrape.com/"
response = requests.get(url)
books_list = []
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    books = soup.find_all('article', class_='product_pod')

    for book in books[:10]:
        
        title = book.h3.a['title']
        price = book.find('p', class_='price_color').text
        # print(len(price))
        clean_price = float(price.replace('Â£', '').strip())
        # print(title)
        # print(clean_price)


        books_list.append({
                "Title": title,
                f"price ({from_currency})": clean_price,
                f"price ({to_currency})": round(clean_price * exchange_rate)
            })

else:
    print("I couldn't find any book")

for item in books_list:
    print(item)
