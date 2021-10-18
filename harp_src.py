import requests as requests
from bs4 import BeautifulSoup
import json


def get_data(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, '
                             'like Gecko) Version/13.1 Safari/605.1.15'}

    req = requests.get(url, headers=headers)

    with open('harp.html', 'w') as file:
        file.write(req.text)

    with open('harp.html') as file:
        src = file.read()

    soup = BeautifulSoup(src, 'lxml')
    news = soup.find_all('div', class_='tm-articles-list')

    KEYWORDS = ['Python', 'web', 'проект', 'программа']

    for item in news:
        articles = item.find_all('article', class_='tm-articles-list__item')
        for i in articles:
            data = i.find('span', class_='tm-article-snippet__datetime-published').text
            title = i.find('a', class_='tm-article-snippet__title-link').text
            art_url = 'https://habr.com' + i.find('a', class_='tm-article-snippet__title-link').get('href')

            for word in KEYWORDS:
                if word in articles:
                    print(f'{data}- {title}- {art_url}')


get_data('https://habr.com/ru/all/')
