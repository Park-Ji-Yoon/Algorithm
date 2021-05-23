def arrayPairSum(nums):
  return sum(sorted(nums)[::2]) # 오름차순 정렬 후 2개 단위로 slicing

print(arrayPairSum([1, 4, 3, 2]))