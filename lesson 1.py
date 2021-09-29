import json

from bs4 import BeautifulSoup

with open('index.html') as file:
    src = file.read()

soup = BeautifulSoup(src, 'lxml')

# title = soup.title
# print(title.text)

# page_h1 = soup.find('h1')
# print(page_h1.text)

# page_h1_all = soup.find_all('h1')
# print(page_h1_all)

user_name = soup.find('div', class_='user__name').find('span').text
print(user_name)

# user_info = soup.find('div', class_='user__info').find_all('span')
# print(user_info)
#
# for item in user_info:
#     print(item.text)

social_links = soup.find('div', class_='social__networks').find('ul').find_all('a')
result_json= []
for item in social_links:
    item_text= item.text
    item_url = item.get('href')
    result = {item_text: item_url}
    result_json.append(result)
resp = open('result.json', 'w+', encoding='utf-8')
json.dump(result_json,resp, ensure_ascii=False, indent=4)

