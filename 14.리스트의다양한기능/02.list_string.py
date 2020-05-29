my_list = [1,2,3,4,5,6]
print(my_list[0], my_list[1])

#String과 List는 비슷하다
str = 'Hello World'
print(str[0], str[1])

print(3 in my_list, 9 in my_list)
print('H' in str, 'Z' in str)

print(my_list.index(5))
print(str.index('d'))

#String -> List
characters = list('hello joker')
print(characters)

words = "hello Harry Poter"
toList = words.split() #공백을 기준으로 문자열 나누기
print(toList)

toList = words.split('l')
#split() 안에 파라메타를 주면 그걸 기준으로 문자열을 나눈다
print(toList) #['he', '', 'o Harry Poter']

#List -> String
toList = list(words)
print(toList)
s = ''.join(toList)
print(s)