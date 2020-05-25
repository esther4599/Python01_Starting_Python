seasons = ['spring', 'summer', 'fall', 'winter']

for s in seasons:
    print(s)

#dictionary + dictionary 는 순서를 갖지 않는다.
ages = {
    'Ron' : 16,
    'Harry' : 18,
    'Hermione' : 28
}
print(ages)

for name in ages.keys(): #we can find value using key
    print(name, "'s age is",ages[name])
# = for name in ages = 같은 결과

for age in ages.values(): #we can't find key this way
    print(age)

for name, age in ages.items():
    print(name, age)
