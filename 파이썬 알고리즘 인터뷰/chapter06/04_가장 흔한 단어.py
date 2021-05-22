import re
import collections

def mostCommonWord(paragraph, banned) -> str:
  # paragraph배열에서 banned가 아닌 것들 -> 단어가 아닌 건 공백으로 치환 -> 소문자로 바꿈 -> 리스트로 바꿈
  words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() if word not in banned]
  counts = collections.Counter(words) # 단어 등장 횟수를 구함
  # print(counts) # 테스트용
  return counts.most_common(1)[0][0] # 가장 흔하게 등장하는 단어의 첫 번째 인덱스 return 

print(mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]))