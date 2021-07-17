#화씨에서 섭씨로 변환
F = float(input())
C = (F-32)/1.8
f= '{:0.2f}'.format(F)
c= '{:0.2f}'.format(C)
print(f'{f} ℉  =>  {c} ℃')