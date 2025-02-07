nums = [3,3]
target = 6
def twoSum(nums, target):
    dict = {}
    for i,n in enumerate(nums):
        diff = target - n
        if diff in dict:
            return [dict[diff], i]
        dict[diff] = i
    return [-1,-1]

print(twoSum(nums,target))
