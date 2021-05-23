def trap(height):
  # height가 없다면 0 리턴
  if not height:
    return 0
  
  volume = 0
  left, right = 0, len(height) - 1
  left_max, right_max = height[left], height[right]

  while left < right:
    left_max, right_max = max(left_max, height[left]), max(right_max, height[right])

    # 더 높은 쪽을 향해 투 포인터 이동
    if left_max <= right_max: # right_max가 left_max보다 크면 오른쪽으로 이동
      volume += left_max - height[left]
      left += 1
    else: # left_max가 right_max보다 크면 왼쪽으로 이동
      volume += right_max - height[right]
      right -= 1

  return volume

print(trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))