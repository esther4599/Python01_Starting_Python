def func() : #사용자 정의 함수
    r1 = (-b + (b**2 - 4*a*c)**0.5) / (2 * a)
    r2 = (-b - (b**2 - 4*a*c)**0.5) / (2 * a)
    print('해는 {} 또는 {} 입니다.'.format(r1, r2))

def test(a, b, c) : #사용자 정의 함수
    r1 = (-b + (b**2 - 4*a*c)**0.5) / (2 * a)
    r2 = (-b - (b**2 - 4*a*c)**0.5) / (2 * a)
    print('해는 {} 또는 {} 입니다.'.format(r1, r2))

def hello():
    print('hello') #내장함수

a = 1
b = 2
c = -8
func()

test(3,4,-5)

hello()