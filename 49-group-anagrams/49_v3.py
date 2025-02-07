strs = ["eat","tea","tan","ate","nat","bat"]

def groupAnagrams(strs):
    hashMap = {}
    for s in strs:
        hashKey = getHashKeyForStr(s)
        if hashKey in hashMap:
            hashMap[hashKey].append(s)
        else:
            hashMap[hashKey] = [s]
    return list(hashMap.values())

def getHashKeyForStr(s):
    hashKey = [0] * 26
    for i in s:
        hashKey[ord(i) - 97] += 1
    return tuple(hashKey)

print(groupAnagrams(strs))
