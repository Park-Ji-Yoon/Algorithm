def isPalindrome(s: str) -> bool: # 매개변수 s를 가지는 함수, return type은 bool
  strs = []
  for char in s: # s 문자열에서 하나씩 문자를 가져옴
    if char.isalnum(): # isalnum()는 영문자, 숫자 여부를 판별하는 함수
      strs.append(char.lower()) # 영문자거나 숫자이면 strs에 소문자 형태로 추가
  
  # 팰린드롬 여부 판별
  while len(strs) > 1:
    if strs.pop(0) != strs.pop(): # strs의 맨 앞 값과 맨 뒤 값 비교
      return False # 다르면 False return
  return True # 같으면 True return

print(isPalindrome("hello")) # False
print(isPalindrome("arera")) # True
print(isPalindrome("A man, a plan, a canal: Panama")) # True
print(isPalindrome("race a car")) # False