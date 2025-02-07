s = "rat"
t = "tai"

def isAnagram(s,t):
    if len(s) != len(t):
        return False
    for i in set(s):
        if s.count(i) != t.count(i):
            return False
    return True

        
print(isAnagram(s,t))
