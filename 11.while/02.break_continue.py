list = [1,2,3,5,7,2,5,237,55]

for val in list:
    if val%3 == 0:
        print(val)
        break #반복문 종료

# for i in range(10):
#     if i%2 != 0:
#         print(i)
#         print(i)
#         print(i)
#         print(i)

for i in range(10):
    if i%2 == 0:
        continue #핵심 코드가 깊은 블록으로 들어가지 않도록 하기
    print(i)
    print(i)
    print(i)
    print(i)
