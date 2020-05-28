#print(list[0]) #error: indexError
txt = 'abc'
#number = int(txt) #error: valueError

text = '100%'
try :
    number = int(txt)
except ValueError :
    print('{}는 숫자가 아닙니다.'.format(text))


#아래와 같이 둘 다 가능하다면 if
def safe_pop_print(list, index):
    if index < len(list):
        print(list.pop(index))
    else:
        print('{}의 값을 가져올 수 없습니다.'.format(index))

    # try :
    #     print(list.pop(index))
    # except IndexError:
    #     print('{}의 값을 가져올 수 없습니다.'.format(index))

safe_pop_print([1,2,3], 5)

# try except를 사용해야만 해결되는 경우
try :
    import my_module
except ImportError:
    print('모듈이 없습니다.')
