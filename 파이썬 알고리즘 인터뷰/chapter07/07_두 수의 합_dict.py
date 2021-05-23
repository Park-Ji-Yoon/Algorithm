def twoSum(nums, target):
  nums_map = {}
  # 키와 값을 바꿔서 딕셔너리로 저장
  for i, num in enumerate(nums):
    nums_map[num] = i
  
  # 타겟에서 첫 번째 수를 뺀 결과를 키로 조회
  for i, num in enumerate(nums):
    # 두 번째 수가 키로 딕셔너리에 있고 인덱스가 다른지 확인
    if target - num in nums_map and i != nums_map[target - num]: 
      return [i, nums_map[target - num]]

print(twoSum([2, 7, 11, 15], 9))