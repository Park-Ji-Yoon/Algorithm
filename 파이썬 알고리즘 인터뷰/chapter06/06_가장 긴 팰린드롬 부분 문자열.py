def longestPalindrome(s) -> str:
  # 팰린드롬 판별 및 투 포인터 확장
  def expand(left, right) -> str:
    # 0 <= left이고, right < len(s)이며, s[left]와 s[right]가 같으면 양쪽으로 1칸씩 확장
    while 0 <= left and right < len(s) and s[left] == s[right]:
      left -= 1
      right += 1
    return s[left + 1:right] # 확장한 문자열 return
  
  # 해당 사항이 없을 때 빠르게 return
  if len(s) < 2 or s == s[::-1]: # 길이가 2 미만이거나 전체가 팰린드롬인 경우
    return s
  
  result = ''
  # 슬라이딩 윈도우 우측으로 이동
  for i in range(0, len(s) - 1):
    result = max(result, expand(i, i + 1), expand(i, i + 2), key=len)

  return result

print(longestPalindrome("babad"))
print(longestPalindrome("cbbd"))