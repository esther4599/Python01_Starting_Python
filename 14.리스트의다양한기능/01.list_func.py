list1 = [135, 462, 27, 2753, 234, 27]

print(list1.index(27)) #해당 값이 있는 index 출력(중복시 처음 값의 index)

#print(list1.index(1)) #error
if 1 in list1:
    print(list1.index(1))

list2 = [1,2,3] + [4,5,6]
print(list2)

#list2.append(7, 8, 9) #error : append() = 단일값 추가
list2.extend([7, 8, 9])
print(list2)

#list2.append([10, 11, 12])
# #print() = [1, 2, 3, 4, 5, 6, 7, 8, 9, [10, 11, 12]]

list1.insert(2, 999) #원하는 index 에 값 추가
print(list1)

list1.insert(-1, 999) #현재 리스트의 마지막 위치에 999추가.
print(list1) #[135, 462, 999, 27, 2753, 234, 999, 27]

list1.insert(1000000000, 999) #index 범위 초과시 제일 마지막에 추가
print(list1) #[135, 462, 999, 27, 2753, 234, 999, 27, 999]

list1.sort()
print(list1)

list1.reverse()
print(list1)