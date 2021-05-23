def arrayPairSum(nums):
  sum = 0
  pair = []
  nums.sort() # 오름차순 정렬

  for n in nums:
    # 앞에서부터 오름차순으로 페어를 만들어서 합 계산
    pair.append(n)
    if len(pair) == 2:
      sum += min(pair) # pair 배열에서 가장 작은 값
      pair = [] # pair 비움

  return sum

print(arrayPairSum([1, 4, 3, 2]))