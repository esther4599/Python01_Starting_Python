list1 = ['가위', '바위', '보'] #자바와 다르게 대괄호를 이용
list2 = [37, 10, 20, 30, 40]

print(list1)
print(list2)

print(list1[0]) #리스트의 시작은 0부터
print(list1[1])

list1[0] = '바위'
print(list1[0])
print(list1)

#print(list1[3]) #오류가 발생. 인덱스보다 큰 수는 입력할 수 없다.
print(list1[-1]) #***자바와 다르게 뒤에서 첫번째 인수를 의미한다.
