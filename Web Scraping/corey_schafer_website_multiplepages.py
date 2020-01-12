from bs4 import BeautifulSoup
import requests
import csv

file = "corey_schafer_scrape_contextmanager.csv"

with open(file, 'w') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(['headline', 'date_published', 'summary', 'youtube_link'])

    for pagenumber in range(0,11):
        link = f'https://coreyms.com/page/{pagenumber}'
        source = requests.get(link).text

        soup = BeautifulSoup(source, 'lxml')

        for article in soup.find_all('article'):
            headline = article.h2.a.text
            date_published = article.find('time', class_='entry-time').text
            summary = article.find('div', class_='entry-content').p.text.strip()
            try:
                link = article.find('iframe', class_='youtube-player')['src']
                vid_id = link.split('/')[4]
                vid_id = vid_id.split('?')[0]
                youtube_link = f'https://www.youtube.com/watch?v={vid_id}'
            except TypeError:
                youtube_link = None

            csv_writer.writerow([headline, date_published, summary, youtube_link])



