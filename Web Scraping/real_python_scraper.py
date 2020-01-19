from bs4 import BeautifulSoup
import csv
import requests

link = 'https://realpython.com/'
source = requests.get(link).text
soup = BeautifulSoup(source, 'lxml')
# article = soup.find('div', class_='col-12 col-md-6 col-lg-4 mb-5')

filename = 'real_python_scraped.csv'

with open(filename, 'a') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(['article_title', 'date_published', 'link'])

    for article in soup.find_all('div', class_='col-12 col-md-6 col-lg-4 mb-5'):
        article_title = article.find('img', class_="card-img-top m-0 p-0 embed-responsive-item rounded")['alt']
        date_published = article.find('small', class_='text-muted').span.text
        href = article.find('div', class_='card-body m-0 p-0 mt-2').a['href']
        link = f'http://www.realpython.com{href}'
        print(link)
        print(date_published)
        print(article_title)
        print()
        csv_writer.writerow([article_title, date_published, link])