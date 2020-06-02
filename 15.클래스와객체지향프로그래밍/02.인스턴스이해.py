#클래스와 인스턴스?
print(type(5)) # <class 'int'>
print(isinstance(5, int))

num1 = []
print(type(num1))

num2 = list(range(10))
print(num2)

chr = list('Hello')
print(chr)

print(type(num1), type(num2), type(chr)) # 모두 <class 'list'>

print(isinstance(num1, list)) # True
print(num1 == list) # False

''' 
위와 같은 결과? class = 분류 (사람 = 강사, 학생 / 강사 != 학생)
사람 = class
강사, 학생 = instance
'''

#실습추가
# + is = 변수의 포인터를 비교하는 연산자. 파이썬의 변수는 모두 포인터를 가리킨다.
str1 = 'Hello'
str2 = 'Hello'
print(str1 == str2) # True
print(str1 is str2) # True. 왜...?

str1 = list('Hello')
str2 = list('Hello')
print(str1 == str2) # True
print(str1 is str2) # False
