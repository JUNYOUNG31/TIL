import requests

key = '61upsZorxV1745Bu1t5PHGU5JlUDaQ6B8r3GMQcIdz7R4cpGxASJS9mdW8%2Ba5UVSSlkPUljamsRfWur0DDCYXQ%3D%3D'
local ='부산'
url = f'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey={key}&sidoName={local}&returnType=json'

print(url)


response = requests.get(url).json()
dust =response['response']['body']['items'][1]['pm10Value']
print(f'부산 초량동의 미세먼지 농도는 {dust} 입니다.')