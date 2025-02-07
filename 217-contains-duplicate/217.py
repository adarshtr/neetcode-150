nums = [1,2,3,4,6,2]

def isContainingDuplicate(nums):
    ansSet = set()
    for num in nums:
        if num in ansSet:
            return True
        else:
            ansSet.add(num)
    return False
    
print(isContainingDuplicate(nums))
