strs = ["eat","tea","tan","ate","nat","bat"]
# strs = ["a","a"]

def groupAnagrams(strs):
    anagramMap = {}

    for s in strs:
        sorted_s = ''.join(sorted(s))
        if sorted_s not in anagramMap:
            anagramMap[sorted_s] = [s]
        else:
            anagramMap[sorted_s].append(s)
    return list(anagramMap.values())

print(groupAnagrams(strs))
