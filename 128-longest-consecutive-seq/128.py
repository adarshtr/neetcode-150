nums = [1,0,1,2]
def longestConsecutiveSequence(nums):
    if len(nums) < 1:
        return 0
    nums = sorted(set(nums))
    maxConsecutive = 1
    currentConsecutive = 1
    for i in range(1,len(nums)):
        if nums[i]-nums[i-1] == 1:
            currentConsecutive += 1
        else:
            currentConsecutive = 1
        if maxConsecutive < currentConsecutive:
            maxConsecutive = currentConsecutive
    return maxConsecutive

print(longestConsecutiveSequence(nums))

