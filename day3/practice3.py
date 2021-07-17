#섭씨에서 화씨 로 변환
C = float(input())
F = (C* 1.8) + 32
c= '{:0.2f}'.format(C)
f = '{:0.2f}'.format(F)
print(f'{c} ℃ =>  {f} ℉')