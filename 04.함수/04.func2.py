def func(a,b,c) : #사용자 정의 함수
    r1 = (-b + (b**2 - 4*a*c)**0.5) / (2 * a)
    r2 = (-b - (b**2 - 4*a*c)**0.5) / (2 * a)
    return r1, r2 #파이썬에서는 여러 값을 return할 수 있음

r1, r2 = func(1,2,-8) #단 return 받을 때 변수 개수 조심
print(r1, r2)