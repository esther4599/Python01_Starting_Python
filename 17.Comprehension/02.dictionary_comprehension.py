stu = ['태연', '진우', '정현', '하늘', '성진']
for num, name in enumerate(stu):
    print('{}번의 이름은 {}입니다.'.format(num+1, name))

# comprehension 이용 dictionary 만들기
stu_dic = {'{}번'.format(num+1): name for num, name in enumerate(stu)}
print(stu_dic)

# zip() : 갯수가 적은거 기준으로 zip() => 나머지는 잘린다.
scores = [85, 92, 78, 90, 100]
for x,y in zip(stu, scores):
    print(x,y)
'''
위에 예시 출력결과 
태연 85
진우 92
정현 78
하늘 90
성진 100
'''

score_dict = {student : score for student, score in zip(stu,scores)}
print(score_dict) #위와 같은 결과