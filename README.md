# WebCrawler_Tutorial

## 大綱

- [什麼是網路爬蟲？](#什麼是網路爬蟲？)
- [爬蟲基本原理](#爬蟲基本原理)
- [開發套件介紹](#開發套件介紹)
    - [Requests介紹](#Requests介紹)
    - [Beautiful Soup介紹](#Beautiful-Soup介紹)
- [爬蟲程式介紹](#爬蟲程式介紹)



## 什麼是網路爬蟲？

> 網路爬蟲（英語：web crawler），也叫網路蜘蛛（spider），是一種用來自動瀏覽全球資訊網的網路機器人。  
> --維基百科

### 本著將互聯網(internet)作為資料庫的精神，我們可以考慮通過爬取內容(scraping content)或Web API這兩種方式來獲取資料。爬取內容(scraping content)意味著讓電腦讀取原本要給人類閱讀的資料。Web API(Interfacing with web APIs)意味著資料是以機器可讀的格式(像是JSON)提供。

## 爬蟲基本原理
#### 在正式講爬蟲之前，先來了解平常我們透過瀏覽器上網時，瀏覽器在背後做了哪些事情。當我們在瀏覽器中輸入網址或點某個超連結後，瀏覽器會對目標網站發送一個HTTP Request，正常情況下，網站接收到Request後，會根據Request回傳對應的內容，也就是HTML檔。瀏覽器在收到回傳的HTML檔後，便會將HTML檔渲染成我們所看見的網頁。

#### 有時候為了掌握最新的資訊，我們需要頻繁開啟、刷新網頁（如：查股價），但是我們可能只需要網頁中的一小段文字，甚至是一個數字，為此每次都要使用瀏覽器來查看，非常耗時且不方便，這種情況下就很適合為此寫一隻爬蟲程式。

#### 透過程式向目標網站發送Request，收到回傳的HTML檔後，再用程式將我們所需要的資訊提取出來即可。這樣每當我們想要知道最新資訊時，只要執行這隻程式就好了。為此我將用到兩個Python的套件：[```requests```](https://requests.readthedocs.io/en/master/) 及 [```Beautiful Soup```](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)。我們將在下個章節介紹這兩個套件。


## 開發套件介紹

- ### Requests介紹：
> Requests is an elegant and simple HTTP library for Python, built for human beings.

```Requests```是建構在[```urllib3```](https://github.com/urllib3/urllib3)上。藉由```Requests```，我們可以輕鬆的發送HTTP/1.1 Requests。  
#### 安裝方式：
```bash
pip install requests
```


- ### Beautiful Soup介紹：
```Beautiful Soup```是一個可以從HTML或XML格式中提取資料的Python套件。它可將透過parser來實現在文檔中的導舫、查找等動作。

> 因為HTML及XML都半結構化的資料，因此可以透過這樣的方式選取目標的資料。


#### 安裝方式
```bash
pip install beautifulsoup4
```

## 爬蟲程式介紹
> 參考example/ipynb/Tutorial.ipynb

## Python學習資源
https://github.com/kowilliam03/Free_Python_Resource