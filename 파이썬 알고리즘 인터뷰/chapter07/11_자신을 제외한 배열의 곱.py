def productExceptSelf(nums):
  out = []
  p = 1
  # 왼쪽 곱셈
  for i in range(0, len(nums)):
    out.append(p)
    p = p * nums[i] # 현재 인덱스의 값과 p를 곱한 것을 누적
  p = 1
  # 왼쪽 곱셈 결과에 오른쪽 값을 차례대로 곱셈
  for i in range(len(nums) - 1, -1, -1):
    out[i] = out[i] * p # 오른쪽 곱셈갑과 왼쪽 곱셈값을 곱셈
    p = p * nums[i] # 현재 인덱스의 값과 p를 곱한 것을 누적
  return out

print(productExceptSelf([1, 2, 3, 4]))