# 애너그램이란 일종의 언어유희로 문자를 재배열하여 다른 뜻을 가진 단어로 바꾸는 것이다

import collections 

def groupAnagrams(strs):
  # 존재하지 않는 키를 삽입해도 가능하도록 항상 디폴트를 생성해주는 defaultdict()사용
  anagrams = collections.defaultdict(list) 
  for word in strs: # strs에서 단어를 하나씩 가져옴
    # 정렬하여 딕셔너리에 추가
    anagrams[''.join(sorted(word))].append(word) # 정렬된 단어를 key로 하고 value는 word인 dict요소 추가
  return list(anagrams.values()) # anagrams의 values들만들 list형태로 return

print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))