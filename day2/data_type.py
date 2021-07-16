# 숫자
number1 = 3      #정수
number2 = 3.14   #실수
number3 = 3 + 4j #복소수

print(type(number1))
print(type(number2))
print(type(number3))

##################################

#문자열
string1 = '문자열1'
string2 = "문자열2"
print(type(string1))
print(type(string2))

###################################

# 참/거짓 (Boolean)
boolean1 = True
boolean2 = False
print(type(boolean1))
print(type(boolean2))

###################################

# 형변환
num1 = 3
num2 = 4.5

# 1. 묵시적 형변환 (자동 형변환)
result1 = num1 + num2
print(result1, type(result1))
# 2. 명시적 형변환
result2 = num1 + int(num2)
print(result2, type(result2))


#실수의 연산을 할때는 항상 주의하자.
#이거 실행 안됨. 
if 0.1 + 0.1 + 0.1 == 0.3:
    print("이거 실행되나?")

#######################################
#문자열 숫자

string_number = "6"
# print(string_number + 5)
print(int(string_number) + 5)
print(string_number + str(5))
########################################

#f-string  python 3.6v 이상에서만 사용가능
# print("황보창님 안녕하세요.!")
# print("홍지범님 안녕하세요.!")
# print("박신영님 안녕하세요.!")
# print("박수아님 안녕하세요.!")

name = "황보창"
money = 1000
hello = f'{name}님 축하드립니다. {money}만원 당첨!'

print(hello)

names = ['황보창', '홍지범', '박신영', '박수아']
for n in names:
    print(f'{n}님 반갑습니다.')

###############################################
# 리스트 사용법

print(names[3])
names.append('강동욱')
print(names[4])
names[4] = '강동옥'
print(names[4])

#가장 마지막 원소를 가지고 오고 싶다.... 
print(names[len(names)-1])
print(names[-1])

#  0  1  2  3  4
# -5 -4 -3 -2 -1  단 이 방법은 권장하지 않음.

############ 실습
# 1.어제 먹은 음식들로 채워진 리스트를 만들어보시오. (적어도 3개 이상)
food = ['밀면','컵라면','닭가슴살','커피']
# 2.첫번째 음식을 출력하시오.
print(food[0])
# 3.두번째 음식을 초밥으로 바꾸시오... 
food[1]='초밥' 
print(food[1])

#########################################
#딕셔너리 

my_dict = {
    '조성현': '하늘색',
    '박준영': '초록',
    '황보창': '파랑'
}

# print(my_dict['조성현'])
# print(my_dict['박신영'])
# print(my_dict.get('조성현'))
# print(my_dict.get('박신영','navy')) #값이 없으면 defualt값은 None 을 반환한다.
                                    #두번째 전달인자를 적게 되면 해당 값을 반환한다.

my_dict['박상준'] = '빨강'
print(my_dict)

my_dict['박상준'] = 'pink'
print(my_dict)

#실습

coin = {
    'BTC': {
        'opening_price': '44405000',
        'closing_price': '38806000',
        'min_price': '36640000',
        'max_price': '44999000',
        'prev_closing_price': '44404000',
        'fluctate_24H': '-7463000',
        'fluctate_rate_24H': '-16.13',
    },
    'ETH': {
        'opening_price': '1458000',
        'closing_price': '1229000',
        'min_price': '1100000',
        'max_price': '1490000',
        'prev_closing_price': '1458000',
        'fluctate_24H': '-275000',
        'fluctate_rate_24H': '-18.28',
    },
    'XRP': {
        'opening_price': '364.5',
        'closing_price': '311.9',
        'min_price': '284.2',
        'max_price': '372.7',
        'prev_closing_price': '364.2',
        'fluctate_24H': '-90.6',
        'fluctate_rate_24H': '-22.51',
    },
}
# 1. 코인의 정보에서 BTC의 최대 가격을 출력하세요.
print(coin['BTC']['max_price'])
# 2. BTC의 시가와 (opening price) XRP의 시가를 더한 결과를 출력하시오.
result = int(coin['BTC']['opening_price']) + float(coin['XRP']['opening_price'])
print(result, type(result))

movie = {
    'movieInfo': {
        'movieNm': '광해, 왕이 된 남자',
        'movieNmEn': 'Masquerade',
        'showTm': '131',
        'prdtYear': '2012',
        'openDt': '20120913',
        'typeNm': '장편',
        'nations': [{'nationNm': '한국'}],
        'genres': [{'genreNm': '사극'}, {'genreNm': '드라마'}],
        'directors': [{'peopleNm': '추창민', 'peopleNmEn': 'CHOO Chang-min'}],
        'actors': [
            {'peopleNm': '이병헌', 'peopleNmEn': 'LEE Byung-hun', 'cast': '광해/하선'},
            {'peopleNm': '류승룡', 'peopleNmEn': 'RYU Seung-ryong', 'cast': '허균'},
            {'peopleNm': '한효주', 'peopleNmEn': 'HAN Hyo-joo', 'cast': '중전'},
        ],
    }
}

#1. 영화의 제목을 출력하시오.
print(movie['movieInfo']['movieNm'])
#2. 다음 movie의 감독의 영어 이름을 출력하시오.
print(movie['movieInfo']['directors'][0]['peopleNmEn'])
#3. 다음 movive의 배우의 인원을 출력하시오.
print(len(movie['movieInfo']['actors']))