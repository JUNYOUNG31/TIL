
#1-9까지 입력받은 값 T 를 T + TT + TTT + TTTT

T = int(input())
a = T+(T+T*10)+(T+10*T+100*T)+(T+10*T+100*T+1000*T)
print(a)