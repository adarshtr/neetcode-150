nums = [3,3]
target = 6
def twoSum(nums, target):
    for i in nums:
        if (target - i) in nums[nums.index(i)+1:]:
            firstElemIndex = nums.index(i)
            secondElemIndex = nums.index(target - i, firstElemIndex + 1)
            return [firstElemIndex, secondElemIndex]
    return [-1,-1]

print(twoSum(nums, target))
