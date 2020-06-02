class Human():
    '''사람에 관한 클래스. 호출이 가능'''

#하나의 Human class로 2개의 다른 instance 만들어서 사용하기
person1 = Human()
person2 = Human()

person1.language = '한국어'
person2.language = 'English'
print(person1.language, person2.language) # 한국어 English

person1.name = '서울시민'
person2.name = '인도인'
print(person1.name, person2.name) # 서울시민 인도인

#class와 instance를 사용하는 이유는 데이터 코드를 사람이 이해하기 편하게 표현할 수 있기 때문이다.
#행동을 클래스 안에 넣을 수 있다.

def speak (person):
    print('{}이 {}로 말을 합니다.'.format(person.name, person.language))

Human.speak = speak
person1.speak() # 서울시민이 한국어로 말을 합니다.
person2.speak() #인도인이 English로 말을 합니다.

# 아래는 list class 관련
#a = list()
#print(isinstance(a, list))
# append() 등의 함수가 list class 에 구현되어 있음