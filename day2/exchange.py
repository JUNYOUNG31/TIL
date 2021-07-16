import requests
from bs4 import BeautifulSoup

url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%ED%99%98%EC%9C%A8'
rsesponce = requests.get(url).text

data = BeautifulSoup(rsesponce, 'html.parser')


money = data.select_one('#_cs_foreigninfo > div > div.api_cs_wrap > div > div.c_rate > div.rate_bx > div.rate_spot._rate_spot > div.rate_tlt > h3 > a > span.spt_con.dw')
result = money.text
print(f'달러 환율은 {result}입니다.')
