list = [1,2,3,4]
dict = {
    'one' : 1,
    'two' : 2,
    'three' : 3,
    'four' : 4
}

#유사한 부분
#get
print(list[0], dict['one'])

#delete
del(list[0])
del(dict['one'])

#len()
print(len(list), len(dict))

#contains()
print(2 in list, 2 in dict.values())
print(2 in dict, 'two' in dict) #dict's default = .keys()

# #to empty
# dict.clear()
# list.clear()
# print(dict, list)

#=================================
#다른 부분
list = [1,2,3,4,5]
dict = {
'one' : 1,
    'two' : 2
}

#pop() => default = 마지막 요소 삭제
print(list[0])
list.pop(0)
print(list[0]) #list = index를 이용, del시 index가 변한다.

print(dict['one'])
dict.pop('one')
#print(dict['one']) #error

# +
big_list = [1,2,3] + [4,5,6]

dict1 = { 1:100, 2:200}
dict2 = {1:1000, 3:300}

#new_dict = dict1 + dict2 #error + 연산으로 dictionary를 합칠 수 없다.
dict1.update(dict2)
print(dict1) #key 1이 1000으로 변경됨. 뒤에 오는 값으로 변경
