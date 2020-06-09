class Animal(): #부모 클래스용
    def __init__(self, name):
        self.name = name

    def walk(self):
        print('걷는다.')

    def eat(self):
        print('먹는다.')

    def great(self):
        print("{}이 인사한다.".format(self.name))

# () 안에 부모클래스를 적어준다.
class Human(Animal): #자식 클래스
    def __init__(self,name, hand): #init의 super = 필수!!
        super().__init__(name)
        self.hand = hand

    def wave(self):
        print('{}손을 흔들면서 '.format(self.hand))

    def great(self):
        self.wave()
        super().great() #부모의 함수 이

person = Human("사람", '오른')
person.great()