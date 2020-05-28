list = []
#print(list[0]) #error
txt = 'qwerty'

try :
    print(list[0])
except :
    print('error 발생')

try :
    #print(list[0])
    i = int(txt)
except Exception as ex:
    print('{} 발생'.format(ex))
    #list index out of range 발생
    #invalid literal for int() with base 10: 'qwerty' 발생