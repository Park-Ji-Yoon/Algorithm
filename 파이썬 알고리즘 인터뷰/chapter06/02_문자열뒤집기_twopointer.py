def reverseString(s) -> None:
  left, right = 0, len(s) - 1 # left는 0, right는 s의 마지막 인덱스값
  while left < right:
    s[left], s[right] = s[right], s[left] # s[right], s[left] 서로 교체
    left += 1 # left에 1 더함
    right -= 1 # right에서 1뺌
  print(s)

reverseString(["h", "e", "l", "l", "o"])
reverseString(["j", "i", "y", "o", "o", "n"])