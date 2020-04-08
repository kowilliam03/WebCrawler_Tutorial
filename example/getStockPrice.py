import requests

from bs4 import BeautifulSoup


def get_stock_price(stock):
    url = f"https://query1.finance.yahoo.com/v8/finance/chart/{stock}.TW?period1=0&period2=1549258857&interval=1d&events=history&=hP2rOschxO0"

    resp = requests.get(url)
    data = resp.json()

    stock_price = data['chart']['result'][0]['meta']['regularMarketPrice']
    return stock_price

if __name__ == "__main__":
    stock = int(input("請輸入股票代號: "))
    stock_price = get_stock_price(stock)
    print(stock_price)