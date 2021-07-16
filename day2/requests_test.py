import requests
from bs4 import BeautifulSoup

# response = requests.get("https://www.naver.com")
response = requests.get("https://www.naver.com").text
# response = requests.get("https://www.naver.com").status_code


print(response)

#200 = 요청이 성공적
#404 = 현재 페이지를 찾을수 없다