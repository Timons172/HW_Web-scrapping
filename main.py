import requests
import bs4
from fake_headers import Headers


KEYWORDS = {'дизайн', 'фото', 'web', 'python'}

headers = Headers(browser='chrome', os='mac').generate()
response = requests.get('https://habr.com/ru/articles/', headers=headers)
soup = bs4.BeautifulSoup(response.text, features='lxml')
articles_list = soup.findAll('article', class_='tm-articles-list__item')

parsed_data = []

for article in articles_list:
    preview = set(article.find('p').text.strip().split())
    if KEYWORDS & preview:
        time = article.find('time')['title']
        title = article.find('a', class_='tm-title__link').find('span').text.strip()
        link = f"https://habr.com{article.find('a', class_='tm-title__link')['href']}"
        print(f'<{time}> - <{title}> - <{link}>')

# Дополнительное задание по анализу всего текста статьи
# for article in articles_list:
#     link = f"https://habr.com{article.find('a', class_='tm-title__link')['href']}"
#     response = requests.get(link, headers=headers)
#     soup = bs4.BeautifulSoup(response.text, features='lxml')
#     review = set(soup.find('p').text.strip().split())
#     if KEYWORDS & review:
#         time = soup.find('time')['title']
#         title = soup.find('h1', class_='tm-title tm-title_h1').find('span').text.strip()
#         print(f'<{time}> - <{title}> - <{link}>')
