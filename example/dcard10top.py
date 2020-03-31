import requests
from bs4 import BeautifulSoup

url = 'https://www.dcard.tw/f'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}

resp = requests.get(url, headers=headers)
html = resp.text

html = BeautifulSoup(html, "lxml")

titles = html.find_all('a', class_='sc-1v1d5rx-4 cJzlcl')
for i in range(10):
    print(titles[i].string)
    print(f"文章網址： https://www.dcard.tw{titles[i].get('href')}")
