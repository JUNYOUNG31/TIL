# cm 를 inch 로 변환
T = float(input())
ans = '{:0.2f}'.format(T/2.54)
t = '{:0.2f}'.format(T)
print(f'{t} cm => {ans} inch')


#lb(파운드)를 Kg 으로 바꾸기
T = float(input())
ans = '{:0.2f}'.format(T/.2046)
t = '{:0.2f}'.format(T)
print(f'{t} lb => {ans} kg')