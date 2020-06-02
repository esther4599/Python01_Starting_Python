class Human() :
    # 함수 이름 전에 __가 있음 = 특별한 메소드

    #생성자
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    #문자열화 함수 = 인스턴스를 출력하는 형식을 지정
    def __str__(self):
        return '{} (몸무게 {}kg)'.format(self.name, self.weight)

    def eat(self):
        self.weight += 0.1
        print('{}가 먹어서 {}kg이 되었습니다.'.format(self.name, self.weight))

    def walk(self):
        self.weight -= 0.1
        print('{}가 걸어서 {}kg이 되었습니다.'.format(self.name, self.weight))

    def speak(self, msg):
        print(msg)

person = Human('철수', 60.5) #__init__ 이 실행
print(person)
