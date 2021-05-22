# 리스트의 pop(0)이 O(n)인데 비해 데크의 popleft()는 O(1)이다
# pop(0)이 O(n)인 이유는 리스트를 복사해서 0번째 값을 가져오는 것이기 때문

def isPalindrome(s: str) -> bool: # 매개변수 s를 가지는 함수, return type은 bool
  strs: Deque = collections.deque() # 데크 자료형 사용
  for char in s: # s 문자열에서 하나씩 문자를 가져옴
    if char.isalnum(): # isalnum()는 영문자, 숫자 여부를 판별하는 함수
      strs.append(char.lower()) # 영문자거나 숫자이면 strs에 소문자 형태로 추가
  
  # 팰린드롬 여부 판별
  while len(strs) > 1:
    if strs.popleft() != strs.pop(): # strs의 맨 앞 값과 맨 뒤 값 비교
      return False # 다르면 False return
  return True # 같으면 True return

print(isPalindrome("hello")) # False
print(isPalindrome("arera")) # True
print(isPalindrome("A man, a plan, a canal: Panama")) # True
print(isPalindrome("race a car")) # False