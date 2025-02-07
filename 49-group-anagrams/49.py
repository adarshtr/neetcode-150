# strs = ["eat","tea","tan","ate","nat","bat"]
strs = ["a","a"]

def isAnagram(s,t):
    if len(s) != len(t):
        return False
    for i in set(s):
        if s.count(i) != t.count(i):
            return False
    return True

def groupAnagrams(strs):
    isVisited = {}
    result = []
    for i in range(0,len(strs)):
        if i in isVisited:
            continue
        isVisited[i] = True
        group = []
        group.append(strs[i])
        for j in range(0,len(strs)):
            if j not in isVisited and isAnagram(strs[i],strs[j]):
                isVisited[j] = True
                group.append(strs[j])
        result.append(group)
    return result
                
print(groupAnagrams(strs))
