# bool 은 0 = false 나머지는 true
# list 의 len 이 0, 빈문자열 = false
print(bool(0), bool([]), bool(''))
print(bool(1), bool(-1), bool(1024), bool([1]), bool('hello'))

#입력이 없으면 false가 된다. => 단락평가
#input()은 입력받은 값을 return. 이때 ''은 false 취급
value = input('입력>') or 'nothing'
print(value)