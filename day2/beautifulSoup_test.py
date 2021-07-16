import requests
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/sise/'
rsesponce = requests.get(url).text

data = BeautifulSoup(rsesponce, 'html.parser')


kospi = data.select_one('#KOSPI_now')
result = kospi.text
#print(result)

print(f'현재의 코스피 지수는 {result}입니다.')

