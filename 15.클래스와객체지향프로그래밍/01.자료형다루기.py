s = 'Hello World'
print(type(s)) # <class 'str'> 자료형 출력

f = 3.14
print(type(f)) # <class 'float'> 부동소수점

i = 42
print(type(i)) # <class 'int'>

print(type(42.0)) # <class 'float'>

print(42 == 42.0) #True

print(isinstance(42, float)) #False
print(isinstance(42, int)) #True

# 모든 파이썬의 변수는 자료형을 갖으며 type()함수로 알아낼 수 있다. 능
# Isinstance()로 확인가능