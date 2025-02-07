s = "rat"
t = "tar"

def isAnagram(s,t):
    freqMapOfs = getFreqMap(s)
    freqMapOft = getFreqMap(t)
    return freqMapOfs == freqMapOft

def getFreqMap(s):
    freqMap = {}
    for i in s:
        if i in freqMap:
            freqMap[i] += 1
        else:
            freqMap[i] = 1
    return freqMap
        
print(isAnagram(s,t))
