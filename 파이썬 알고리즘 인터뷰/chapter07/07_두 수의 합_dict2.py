def twoSum(nums, target):
  nums_map = {}
  # 하나의 for 문으로 통합
  for i, num in enumerate(nums):
    if target - num in nums_map: # target - num 키값이 nums_map에 있다면
      return [nums_map[target - num], i]
    nums_map[num] = i 

print(twoSum([2, 7, 11, 15], 9))