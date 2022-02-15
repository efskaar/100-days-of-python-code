def are_anagrams(s1,s2):
  letters1 = sorted(s1.lower().strip())
  letters2 = sorted(s2.lower().strip())
  for l1,l2 in zip(letters1,letters2):
    if l1 != l2:
      return False
  return True

def are_anagrams_freq_dict(s1,s2):
  freqDict1 = freq_dict(s1.lower().strip())
  freqDict2 = freq_dict(s2.lower().strip())
  for key in freqDict1.keys():
    if key not in freqDict2 or freqDict1[key] != freqDict2[key]:
      return False
  return True

def freq_dict(s1):
  freqDict = {}
  for char in s1:
    if char in freqDict.keys():
      freqDict[char] += 1
    else:
      freqDict[char] = 1
  return freqDict

if __name__ == '__main__':
  print(are_anagrams('qw','YtReWq'))
  print(are_anagrams_freq_dict('qwerty','YtReWq'))