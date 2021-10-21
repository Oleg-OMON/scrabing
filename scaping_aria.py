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

    with open('aria_wiki.html', ) as file:
        src = file.read()

    result_json = []
    soup = BeautifulSoup(src, 'lxml')
    albumn_all = soup.find_all('table', class_='wikitable plainrowheaders')

    for albumn in albumn_all:
        albumn_name = albumn.find_all('i')
        release_date = albumn.find_all('ul')

        for i in range(len(release_date)):
            name = albumn_name[i].text
            data = release_date[i].find('li').text

            result = {name: data}
            result_json.append(result)

            # resp = open('aria_albumn.json', 'w+', encoding='utf-8')
            # json.dump(result_json, resp, ensure_ascii=False, indent=4)
            try:
                connection = psycopg2.connect(
                    host=host,
                    user=user,
                    password=password,
                    database=db_name
                )
                connection.autocommit = True

                with connection.cursor() as cursor:
                    cursor.execute(
                        """CREATE TABLE albumn_aria(
                        id serial PRIMARY KEY,
                        albumn_name varchar(50) NOT NULL,
                        release_date varchar(50) NOT NULL);"""
                    )

                    print("[INFO] Table created successfully")

                with connection.cursor() as cursor:
                    cursor.executemany(

                    )
                # f"""INSERT INTO albumn_aria(albumn_name%, release_date%) VALUES
                #                         ('{name}', '{data}');"""
                print("[INFO] Data was succefully inserted")


            except Exception as _ex:
                print("[INFO] Error while working with PostgreSQL", _ex)
            finally:
                if connection:
                    # cursor.close()
                    connection.close()
                    print("[INFO] PostgreSQL connection closed")


get_data('https://ru.wikipedia.org/wiki/Дискография_группы_«Ария»#Студийные_альбомы')
