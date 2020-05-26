list = [1,2,3,4,5]
for i, v in enumerate(list):
    print('{}=i, {}=v'.format(i,v))

#enumerate = index, value를 값이 return

for a in enumerate(list):
    #a[0] = 6 #error 여기서 a = tuple
    print('{}=i, {}=v'.format(a[0],a[1]))

for a in enumerate(list):
    # *a = 튜플을 쪼개라는 의미
    print('{}=i, {}=v'.format(*a))
#위의 결과는 다른 방법들과 동일

#dictionary와 tuple
ages = {
    'tod' : 35,
    'jane' : 23,
    'paul' : 62
}

for k, v in ages.items():
    print("{}s' age = {}".format(k,v))

for a in ages.items():
    print("{}s' age = {}".format(*a))