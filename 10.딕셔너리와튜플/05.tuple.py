list1 = [1, 2, 3, 4]
list1.append(5)
list1.remove(1)
print(list1)

#tuple = 내용 변경이 불가, 순서가 정해져있음 = index 사용
tuple1 = (1,2,3)
print(tuple1)
print(type(tuple1))

tuple2 = 1,2,3 #()를 작성하는게 더 확실히 튜플임을 보여주는 방법
print(tuple2, type(tuple2))

tuple3 = tuple(list1) #list to tuple
print(tuple3)

#index 이용
print(tuple3[0], tuple3[1])

#tuple3[0] = 5 #error 값 변경 불가
#del(tuple3[0]) #error pop()도 불가능
# 튜플은 변수간에 값을 변경하는 경우에 사용함

#+a
a = 19
if 1 <= a <= 20:
    print("편리하군")