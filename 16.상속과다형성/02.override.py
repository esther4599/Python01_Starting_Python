class Animal(): #부모 클래스
    def walk(self):
        print('걷는다.')

    def eat(self):
        print('먹는다.')

    def great(self):
        print("인사한다.")

# () 안에 부모클래스를 적어준다.
class Human(Animal): #자식 클래스
    def wave(self):
        print('손을 흔든다.')

    def great(self):
        self.wave()

class Dog(Animal): #자식 클래스
    def wag(self):
        print('꼬리를 흔든다.')

    def great(self):
        self.wag()

class Cow(Animal):
    '''소'''

# person = Human()
# person.great() # 손을 흔든다.
#
# dog = Dog()
# dog.great() # 꼬리를 흔든다.

cow = Cow()
cow.great() # 인사한다.