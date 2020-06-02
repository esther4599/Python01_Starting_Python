# Modeling = class로 현실의 정보를 표현하는 것
class Human() :
    '''인간에 관한 클래스'''

# person = Human()
# person.name = '철수'
# person.weight = 60.5

def create_Human(name, weight):
    person = Human()
    person.name = name
    person.weight = weight
    return person

# person = create_Human('철수', 60.5)

Human.create_Human = create_Human
person = Human.create_Human('철수', 60.5)

def eat(person):
    person.weight += 0.1
    print('{}가 먹어서 {}kg이 되었습니다.'.format(person.name, person.weight))

def walk(person):
    person.weight -= 0.1
    print('{}가 걸어서 {}kg이 되었습니다.'.format(person.name, person.weight))

Human.eat = eat
Human.walk = walk

person.walk()
person.eat()
person.walk()