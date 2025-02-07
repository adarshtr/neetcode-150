s="rat"
t="car"
def isAnagram(s,t):
    freqMapOfs = getFreqMap(s)
    freqMapOft = getFreqMap(t)
    if len(freqMapOft) != len(freqMapOfs):
        return False
    for i in freqMapOfs:
        if (i not in freqMapOft) or (freqMapOfs[i] != freqMapOft[i]):
            return False
    return True


def getFreqMap(s):
    freqMap = {}
    for i in s:
        if i in freqMap:
            freqMap[i] += 1
        else:
            freqMap[i] = 1
    return freqMap


print(isAnagram("rat","tar"))
