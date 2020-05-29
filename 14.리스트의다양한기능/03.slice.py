list = [1,2,3,4,5]
print(list[1])

txt = 'hello world'
print(txt[1])

#slicing = list 나 string 에서 여러 값을 가져오는 방법
print(txt[1:5]) #slicing. 포함, 포함X

list = ['영', '일', '이', '삼', '사', '오']
print(list[0:2])
print(list[:2])

print(list[2:len(list)])
print(list[2:])

print(list[:]) #조거에 맞는 새로운 리스트를 만들어서 return
