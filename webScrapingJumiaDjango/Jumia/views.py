import locale
import re

from bs4 import BeautifulSoup
import requests
from django.shortcuts import render
def get_smartphones_data():
    data_list = []
    brands = set()

    for page in range(1, 14):
        url = 'https://www.jumia.com.tn/mlp-telephone-tablette/smartphones/?page=' + str(page) + '#catalog-listing'
        r = requests.get(url)
        soup = BeautifulSoup(r.content, "html.parser")
        Articles = soup.find_all('article', {'class': 'prd _fb col c-prd'})

        for item in Articles:
            data = {
                'name': item.find('h3', {'class': 'name'}).text,
                'price': item.find('div', {'class': 'prc'}).text,
                'image': item.find('div', {'class': 'img-c'}).find('img')['data-src'],
                'brand': item.find('h3', {'class': 'name'}).text.split()[0]
            }
            data_list.append(data)
            brands.add(data['name'].split()[0])  # Get the brand name from the product name and add it to the set
    return data_list, list(brands)
# This function handles HTTP requests to display the list of smartphones
def smartphones(request):
    data_list, brands = get_smartphones_data()

    data_list, brands = get_smartphones_data()

    # Filter data based on the request parameters
    brand = request.GET.get('brand', '')
    max_price = request.GET.get('max_price', '')

    if brand:
        data_list = [data for data in data_list if data['name'].startswith(brand)]

    if max_price:
        max_price_float = float(max_price)
        data_list = [data for data in data_list if float(re.sub(r'[^\d.]', '', data['price'])) <= max_price_float]
    return render(request, 'smartphones.html', {'data_list': data_list, 'brands': brands})

# This function handles HTTP requests to display the details of a specific smartphone
def smartphone_details(request):
    name = request.GET.get('name')
    price = request.GET.get('price')
    brand = request.GET.get('brand')
    image = request.GET.get('image')
    return render(request, 'smartphone_details.html', {'name': name, 'price': price, 'brand': brand, 'image': image})