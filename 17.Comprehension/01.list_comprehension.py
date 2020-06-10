areas = []
for i in range(1,11):
    #areas.append(i*i)
    areas = areas + [i*i]
print(areas) #[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# comprehension 이용
areas2 = [i*i for i in range(1,11)]
print('using comprehension',areas2) # areas와 같은 결과를 출력

# comprehension : if 활용
areas = []
for i in range(1,11):
    if i%2 == 0:
        areas = areas + [i*i]
print(areas) #[4, 16, 36, 64, 100]

areas2 = [i*i for i in range(1,11) if i%2 == 0]
print('using comprehension',areas2) #[4, 16, 36, 64, 100]

# comprehension : for문 중첩
# 예시 = 15*15 바둑판 만들기
board = [(x,y) for x in range(15) for y in range(15)]
print(board) # 각 지점을 표시하는 튜플 생성 (0,0) ~ (14,14)까지
