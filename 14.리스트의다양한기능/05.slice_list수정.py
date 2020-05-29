nums = list(range(10))
print(nums)

del(nums[0])
print(nums)

#slice를 통한 삭제
del(nums[:5])
print(nums) #[6, 7, 8, 9]

#slice를 통한 수정
nums[1:3] = [77, 88]
print(nums) #[6, 77, 88, 9]

nums[1:3] = [77, 88, 99]
print(nums) #[6, 77, 88, 99, 9]

nums[1:4] = [8]
print(nums) #[6, 8, 9]
