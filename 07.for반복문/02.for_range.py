for i in [0,1,2,3,4]:
    print(i)

for i in range(5):
    print(i)
#0부터 시작해서 5미만

names = ['harry', 'lon', 'her']

for i in range(len(names)) :
    name = names[i]
    print('{}번 {}'.format(i, name))

for i, name in enumerate(names):
    print('{}번 {}'.format(i, name))

for i in range(11172):
    print(chr(44032+i), end='')
