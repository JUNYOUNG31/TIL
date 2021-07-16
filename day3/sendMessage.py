import requests

TOKEN ='1859632049:AAFDrNkZFjxI3t0kSSuiSSBiLOVMomFT1R0'
APP_URL = f'https://api.telegram.org/bot{TOKEN}'


update_url = f'{APP_URL}/getUpdates'
response = requests.get(update_url).json()

print(APP_URL)
#chat_id 뽑아내기

chat_id = response.get('result')[0].get('message').get('chat').get('id')
### 메시지를 보내보자..
#필수 조건
# 1. chat_id
# 2. text

text = '승훈님 별다방 아메리카노 당첨!'

message_url = f'{APP_URL}/sendMessage?chat_id={chat_id}&text={text}'

requests.get(message_url)