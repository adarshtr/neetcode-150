import heapq

nums = [1,1,1,2,2,3]
k = 2

def topKFrequent(nums, k):
    freqHash = {}
    for i in nums:
        if i in freqHash:
            freqHash[i] += 1
        else:
            freqHash[i] = 0
    return heapq.nlargest(k,freqHash,key=lambda i: freqHash[i])



print(topKFrequent(nums,k))
