nums = [1,2,3,4]
# [24,12,8,6]

def productExceptSelf(nums):
    result = [0] * len(nums)
    prd = 1
    for i in range(0,len(nums)):
        result[i] = prd
        prd *= nums[i]
    prd = 1
    for i in range(len(nums) - 1, -1, -1):
        result[i] = result[i] * prd
        prd *= nums[i]
    return result
        

print(productExceptSelf(nums))

# TODO: Do this multi threaded
