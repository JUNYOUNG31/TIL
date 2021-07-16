#각 자릿수의 합을 출력하기

T = int(input())
print(sum(map(int, str(T)))) 


#입력한 숫자까지 1부터 더하기 
T=int(input())
sumi = 0
for i in range(1, T+1):
        sumi += i
print(sumi)

#입력한 값만큼 가로로 반복하기
T=int(input())
for i in range(T):
    print('#',end='')

#입력한 값만큼 세로로 반복하기
T=int(input())
for i in range(T):
    print('#')    