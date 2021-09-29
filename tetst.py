from bs4 import BeautifulSoup
import json

def get_data(url):
    with open('kubgufk.html') as file:
        src = file.read()

    result_json = []
    soup = BeautifulSoup(src, 'lxml')
    faculty_blocks = soup.find_all('div', class_='panel panel-default')
    for faculty_block in faculty_blocks:
        faculty_name = faculty_block.find('h4', class_='panel-title').text.strip()
        faculty_info = faculty_block.find('div' ,class_='panel-body')
        directions = []
        directions_info = faculty_info.find_all('h4')
        scheduleds_info = faculty_info.find_all('ul')
        for i in range(len(directions_info)):
            tmp = scheduleds_info[i].find_all('a')
            scheduleds = []
            for elem in tmp:
                name = elem.text
                url = 'https://kgufkst/ru' + elem.get('href')
                scheduleds.append({name: url})


            directions.append({directions_info[i].text:scheduleds})
        result_json.append({faculty_name: directions})

    resp = open('scheldule_KUBGU.json', 'w+', encoding='utf-8')
    json.dump(result_json, resp, ensure_ascii=False, indent=4)

get_data('https://kgufkst.ru/student/raspisanie-zanyatiy/')

