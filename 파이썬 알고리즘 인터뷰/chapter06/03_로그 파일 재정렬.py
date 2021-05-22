def reorderLogFiles(logs):
  letters, digits = [], []
  for log in logs: # logs에서 요소를 하나씩 가져옴
    if log.split()[1].isdigit(): # log의 1번째 인덱스가 숫자인지 판별 * isdigit()은 숫자 여부 구분
      digits.append(log) # 숫자면 digits에 append
    else:
      letters.append(log) # 문자면 letters에 append
  
  # 2개의 키를 람다 표현식으로 정렬
  letters.sort(key = lambda x: (x.split()[1:], x.split()[0])) # 문자순으로 정렬, 문자가 동일할 경우 식별자 순으로 정렬
  return letters + digits # 문자 로그 + 숫자 로그 return

print(reorderLogFiles(["dig1 8 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]))