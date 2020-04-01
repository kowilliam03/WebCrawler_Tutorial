import requests
from bs4 import BeautifulSoup

article_id = input("請輸入文章的ID: ")
limit = int(input("要查看前幾層的留言： "))

if limit < 0:
    limit = 30

dcard_api = "https://www.dcard.tw/service/api/v2/posts/{}/comments?limit={}".format(
    article_id, limit)
header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}

resp = requests.get(dcard_api, headers=header)
floors = resp.json()

for floor in floors:
    if "school" not in floor:
        continue
    if "content" not in floor:
        continue
    print(f"{floor['floor']}樓 {floor['school']} {floor['content']}")
