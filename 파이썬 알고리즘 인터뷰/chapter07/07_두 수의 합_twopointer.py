def twoSum(nums, target):
  nums = sorted(nums)
  left, right = 0, len(nums) - 1
  while not left == right:
    # 합이 타겟보다 작으면 왼쪽 포인터를 오른쪽으로
    if nums[left] + nums[right] < target:
      left += 1
    elif target < nums[left] + nums[right]:
      right -= 1
    else:
      return [left, right]

print(twoSum([2, 7, 11, 15], 9))

# 풀이 불가