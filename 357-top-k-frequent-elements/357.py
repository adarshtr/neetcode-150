nums = [1,1,1,2,2,3]
k = 2
# nums = [1,1,1,2,2,3]
# k = 3
# nums = [-1,-1]
# k = 1
# nums = [1,2]
# k = 2

def topKFrequent(nums, k):
    freqTuplesSet = set()
    for i in nums:
        freqTuplesSet.add((i,nums.count(i)))
    freqTuplesList = sorted(list(freqTuplesSet), key=lambda i: i[1], reverse= True)
    return list(map(lambda i: i[0],freqTuplesList[:k]))

    


print(topKFrequent(nums,k))
