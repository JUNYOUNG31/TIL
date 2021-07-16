import requests

#미세먼지 농도
key = '61upsZorxV1745Bu1t5PHGU5JlUDaQ6B8r3GMQcIdz7R4cpGxASJS9mdW8%2Ba5UVSSlkPUljamsRfWur0DDCYXQ%3D%3D'
local ='부산'
url = f'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey={key}&sidoName={local}&returnType=json'
response = requests.get(url).json()
dust =response['response']['body']['items'][1]['pm10Value']

#텔레그램 봇
TOKEN ='1859632049:AAFDrNkZFjxI3t0kSSuiSSBiLOVMomFT1R0'
APP_URL = f'https://api.telegram.org/bot{TOKEN}'
update_url = f'{APP_URL}/getUpdates'
response = requests.get(update_url).json()

#chat_id 뽑아내기
chat_id = response.get('result')[0].get('message').get('chat').get('id')

#마지막 메시지 읽기
last_message =response.get('result')[-1].get('message').get('text')

text = '안녕하세요'

#마지막 메세지의 조건
if last_message == '미세먼지':
    text = f'부산 초량동의 미세먼지 농도는 {dust} 입니다.'

message_url = f'{APP_URL}/sendMessage?chat_id={chat_id}&text={text}'

requests.get(message_url)
