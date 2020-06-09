class Animal(): #부모 클래스
    def walk(self):
        print('걷는다.')

    def eat(self):
        print('먹는다.')

# () 안에 부모클래스를 적어준다.
class Human(Animal): #자식 클래스
    def wave(self):
        print('손을 흔든다.')

class Dog(Animal): #자식 클래스
    def wag(self):
        print('꼬리를 흔든다.')

person = Human()
person.walk()
person.eat()
person.wave()

dog = Dog()
dog.walk()
dog.eat()
dog.wag()