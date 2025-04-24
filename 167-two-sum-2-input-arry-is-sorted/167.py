# [2,7,11,15] target 9 =>

def findElements(lis, tar):
    for i in range(0,len(lis)):
        if ((tar - lis[i]) in lis):
            return [i+1, lis.index((tar - lis[i]),i+1) + 1]
    return [-1,-1]


print(findElements([2,7,11,15], 9))
print(findElements([2,3,4], 6))
print(findElements([-1,0], -1))
