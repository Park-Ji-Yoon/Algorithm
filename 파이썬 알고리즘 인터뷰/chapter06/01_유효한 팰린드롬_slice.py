import re

def isPalindrome(s: str) -> bool:
  s = s.lower()
  s = re.sub('[^a-z0-9]', '', s) # 정규식으로 영문자와 숫자 외의 것 제외
  return s == s[::-1] # 원래 리스트와 뒤집은 리스트 비교값 return

print(isPalindrome("hello")) # False
print(isPalindrome("arera")) # True
print(isPalindrome("A man, a plan, a canal: Panama")) # True
print(isPalindrome("race a car")) # False