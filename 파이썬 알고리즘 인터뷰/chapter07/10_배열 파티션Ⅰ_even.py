def arrayPairSum(nums):
  sum = 0
  nums.sort() # 오름차순 정렬

  for i, n in enumerate(nums):
    # 짝수 번째 값의 합 계산
    if i % 2 == 0: sum += n
  
  return sum

print(arrayPairSum([1, 4, 3, 2]))