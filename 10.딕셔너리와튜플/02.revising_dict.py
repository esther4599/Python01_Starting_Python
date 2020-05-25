#list
list = [1,2,3,4,5]
print(list)

list[2] = 33

#list[5] = 6 #error 범위 아웃
list.append(6)
del(list[0]) # list.pop(0) = 지우는 값을 return
print(list)

#dictionary
dict = {
    'one' : 1,
    'two' : 2,
    'three' : 3
}
print(dict)

dict['one'] = 11
dict['four'] = 4 #값을 추가하는 방식이 다르다.
del(dict['one']) #dict.pop('one') = 지우는 값을 return
print(dict)
