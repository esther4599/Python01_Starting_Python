f1 = 5
f2 = 5.0
f3 = 5.000

print(f1)
print(f2)
print(f3)
#f2와 f3는 같은 값으로 출력 5.0

f4 = 5 * 1
f5 = 5 * 1.0

print(f4)
print(f5) #실숙 계산식에 들어가면 해당 변수를 실수로 인식한다.

print(6/5)
print(6//5) #//는 몫만 출력
print(7%5) #%는 나머지 출력
print(10/5) #/은 정수만 있어도 실수로 인식 => 이유는 나머지

print(0.1 + 0.1 + 0.1 == 0.3) #=> false가 출력됨 = 정확하지 않음
print(int(0.5))
print(float(5))