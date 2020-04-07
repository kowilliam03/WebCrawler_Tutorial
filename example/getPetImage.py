import requests
import os

from bs4 import BeautifulSoup


def get_img_tag(id):
    url = "https://www.dcard.tw/f/pet/p/" + id
    resp = requests.get(url)

    html = resp.text
    html = BeautifulSoup(html, 'lxml')

    imgs = html.find_all('img', class_="sc-1wz6w4a-0 XWDjG")
    return imgs


def save_img(url, dest):
    file_name = url.split("/")[-1]
    file_name = dest + '/' + file_name

    resp = requests.get(url)
    img = resp.content

    with open(file_name, "wb") as f:
        f.write(img)


if __name__ == "__main__":
    url = "https://www.dcard.tw/service/api/v2/forums/pet/posts?popular=true&limit=10"
    resp = requests.get(url)

    articles = resp.json()
    article_id = [str(i['id']) for i in articles]

    if not os.path.isdir('./img'):
        os.mkdir('img')

    dest = './img/'
    for id in article_id:
        tags = get_img_tag(id)

        for tag in tags:
            src = dest + id
            if not os.path.isdir(src):
                os.mkdir(src)

            url = tag.get('src')
            save_img(url, src)
