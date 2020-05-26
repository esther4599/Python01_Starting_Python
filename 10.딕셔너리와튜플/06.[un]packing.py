#튜플을 이용해 하나의 변수에 여러개의 변수를 대입할 수 있다
#이를 packing(변수 대입)/unpacking(변수 반환) 이라 한다

a, b = 1, 2 #a와 b로 이루어진 튜플이 만들어진다. a=1, b=2
print(a, b)
#위와 같은 경우 packing 이라는 용어를 사용하지는 않는다.

c = (3, 4)
d, e = c
print(d, e) #c를 unpacking해 d, e에 대입한 경우

f = d,e
print(f) #d, e를 통해 f를 packing
#f[0] = 33 #이때는 error 발생 = packing의 경우 튜플로 인정

#아래는 임시 변수를 사용하지 않고 값을 교환하는 방법
x = 5
y = 10
x, y = y, x
print(x, y)


y = 4 # 이 경우 error가 발생하지 않음.
print(y)

#func의 여러 값을 한번에 return 받는 경우 사용 가능
def tuple_func() :
    return 1, 2

q, w = tuple_func()
print(q, w)
