from bs4 import BeautifulSoup
import requests

url = 'https://www.olx.ro/auto-masini-moto-ambarcatiuni/autoturisme/audi/a6/?search%5Bfilter_float_price%3Ato%5D=8000&search%5Bfilter_enum_petrol%5D%5B0%5D=diesel&search%5Bfilter_enum_gearbox%5D%5B0%5D=automatic&search%5Bfilter_float_year%3Afrom%5D=2010&search%5Bfilter_float_enginesize%3Ato%5D=2001'
content = requests.get(url).text
soup = BeautifulSoup(content, 'lxml')

# car_add = soup.find('div', class_='offer-wrapper')
for car_add in soup.find_all('div', class_='offer-wrapper'):
    title = car_add.find('h3', class_='lheight22 margintop5').a.strong.text
    price = car_add.find('p', class_='price').text
    time_and_location = car_add.find('td', class_='bottom-cell').div.p
    # ad_location = car_add.find('td', class_='bottom-cell').div.p.small.span.text
    time_added = time_and_location.find_all('span')[1].text
    car_location = time_and_location.find_all('span')[0].text
    link = car_add.find('h3', class_='lheight22 margintop5').a['href']
    image = car_add.find('img', class_='fleft')['src']

    print(title.strip())
    print(price.strip())
    print(car_location.strip())
    print(time_added.strip())
    print(link)
    print(image)
    print()