nums = [1,1,1,2,2,2,3,3,3]
k = 3


def topKFrequent(nums, k):
    freqHash = {}
    for i in nums:
        count = nums.count(i)
        if (count in freqHash):
            if i not in freqHash[count]:
                freqHash[count] += [i]
        else:
            freqHash[count] = [i]
    sorted_keys = sorted(freqHash.keys(),reverse= True)
    result = []
    remaining = 0
    print(freqHash)
    for i in sorted_keys:
        remaining = (k - len(result))
        if remaining < 1:
            break
        values = freqHash[i]
        result += values[:remaining]
    return result

print(topKFrequent(nums,k))
