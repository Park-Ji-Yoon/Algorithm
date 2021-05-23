def threeSum(nums):
  result = []
  nums.sort() # 오름차순 정렬

  for i in range(len(nums) - 2):
    # 중복된 값 건너뛰기
    if 0 < i and nums[i] == nums[i-1]:
      continue
    for j in range(i+1, len(nums) - 1):
      if i + 1 < j and nums[j] == nums[j-1]:
        continue
      for k in range(j+1, len(nums)):
        if j + 1 < k and nums[k] == nums[k-1]:
          continue
        if nums[i] + nums[j] + nums[k] == 0:
          result.append([nums[i], nums[j], nums[k]])
  return result

print(threeSum([-1, 0, 1, 2, -1, -4]))