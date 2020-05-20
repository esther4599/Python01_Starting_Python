list2 = [37, 10, 20, 30, 40, 43, 57]
print(list2)

#list2.append(16)
#print(list2)

list3 = list2 + [16]
print(list3)
#=>위의 방법은 여러 변수를 추가할 수 있음

list4 = list3 + list2
print("list4 = ", list4)

n = 12
a = n in list4
print(a)

n = 10
if n in list4 :
    print("{}은 존재".format(n))

print(list4)
del(list4[12])#해당 인덱스에 존재하는 값 삭제. ()는 선택
print(list4)

list4.remove(30) #해당 값을 삭제. 중복이 있을 경우 인덱스가 작은 값을 삭제
print(list4)
