a = 10
if a < 10 and 2**a > 1000 and a%5 == 2 and round(a) == a :
    print('복잡한 식')
# and = 모두 true 실행. or = 하나라도 true면 실행

def rf():
    print('return false')
    return False

def rt():
    print('return true')
    return True

print('test 01')
a = rf()
b = rt()

if a and b:
    print(True)
else :
    print(False)
''' 
결과
test 01
return false
return true
False
'''

print('test 02')
if rf() and rt():
    print(True)
else:
    print(False)
'''
결과
test 02
return false
False
'''

dict = {'key01':'value01'}
#아래의 경우 조건 순서가 변경되면 존재하지 않는 key값으로 조회가 이루어져 error 발생
if 'key02' in dict and dict['key02'] == 'value01':
    print('존재')
else:
    print('없음')