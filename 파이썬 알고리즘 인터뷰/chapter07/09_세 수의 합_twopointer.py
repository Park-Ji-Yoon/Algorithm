def threeSum(nums):
  result = []
  nums.sort()

  for i in range(len(nums) - 1):
    # 중복된 값 건너뛰기
    if 0 < i and nums[i] == nums[i - 1]:
      continue

    # 간격을 좁혀가며 합 sum 계산
    left, right = i + 1, len(nums) - 1
    while left < right:
      sum = nums[i] + nums[left] + nums[right]
      if sum < 0:
        left += 1
      elif 0 < sum:
        right -= 1
      else:
        # sum = 0인 경우이므로 정답 및 스킵처리
        result.append([nums[i], nums[left], nums[right]])

        while left < right and nums[left] == nums[left + 1]:
          left += 1
        while left < right and nums[right] == nums[right - 1]:
          right -= 1

        left += 1
        right -= 1

  return result

print(threeSum([-1, 0, 1, 2, -1, -4]))