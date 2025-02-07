
nums = [1,2,3,4]
# [24,12,8,6]

def productExceptSelf(nums):
    result = []
    productLeft = []
    productRight = []
    resL, resR = 1,1
    for i in range(len(nums)):
        if i == 0:
            resL = 1
            resR = 1
        else:
            resL *= nums[i-1]
            resR *= nums[(len(nums) - i)]
        productLeft.append(resL)
        productRight.append(resR)
    for i in range(len(nums)):
        result.append(productRight[len(nums) - 1 - i]*productLeft[i])
    return result
        

print(productExceptSelf(nums))

# TODO: Do this multi threaded
