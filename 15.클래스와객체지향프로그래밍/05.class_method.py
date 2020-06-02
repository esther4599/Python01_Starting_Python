# 앞에서는 빈 클래스에 함수와 속성을 추가
# 여기에는 class 안에 바로 메소드와 속성을 추가
# this 대신에 self를 사용한다.
class Human() :
    def create(name, weight):
        person = Human()
        person.name = name
        person.weight = weight
        return person

    def eat(self):
        self.weight += 0.1
        print('{}가 먹어서 {}kg이 되었습니다.'.format(self.name, self.weight))

    def walk(self):
        self.weight -= 0.1
        print('{}가 걸어서 {}kg이 되었습니다.'.format(self.name, self.weight))

    def speak(self, msg):
        print(msg)

person = Human.create('철수', 60.5)
person.walk()
person.eat()
person.walk()
person.speak('안녕하세요.') #self는 .을 통해서 인스턴스 전달. 그 외의 파라메터만 전달
