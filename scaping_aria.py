import json
from bs4 import BeautifulSoup
import requests
from cofig import host, user, password, db_name
import psycopg2

def get_data(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, '
                             'like Gecko) Version/13.1 Safari/605.1.15'}

    # req = requests.get(url, headers=headers)
    #
    # with open('aria_wiki.html', 'w') as file:
    #     file.write(req.text)

    with open('aria_wiki.html',) as file:
        src = file.read()

    soup = BeautifulSoup(src, 'lxml')
    albumn_all = soup.find('table', class_='wikitable').find_all('th')
    result_json = []
    for albumn in albumn_all[3:]:
        albumn_name = albumn.find('a').get('title')


        soup = BeautifulSoup(src, 'lxml')
        release_all= soup.find('table', class_='wikitable').find_all('ul')

        for release in release_all:
            release_date = release.find('li').text
            # print(release_date)
        result = {albumn_name: release_date}
        result_json.append(result)

    resp = open('aria_albumn.json', 'w+', encoding='utf-8')
    json.dump(result_json, resp, ensure_ascii=False, indent=4)

    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )
        connection.autocommit = True


    except Exception as _ex:
        print("[INFO] Error while working with PostgreSQL", _ex)
    finally:
        if connection:
            # cursor.close()
            connection.close()
            print("[INFO] PostgreSQL connection closed")

get_data('https://ru.wikipedia.org/wiki/Дискография_группы_«Ария»#Студийные_альбомы')
