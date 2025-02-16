nums = [-6,8,-5,7,-9,-1,-7,-6,-9,-7,5,7,-1,-8,-8,-2,0]
def longestConsecutiveSequence(nums):
    maxSeq, curSeq = 0, 1
    numSet = set(nums)
    for i in numSet:
        if i-1 not in numSet:
            while i+1 in numSet:
                curSeq += 1
                i += 1
            maxSeq = max(maxSeq,curSeq)
            curSeq = 1
    return maxSeq


print(longestConsecutiveSequence(nums))
