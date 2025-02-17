import string

s = "A man, a plan, a canal: Panama"


def isPalindrome(s):
    validStrings = set(string.ascii_uppercase).union(set(string.digits))
    sanitisedS = list(filter(lambda x: x in validStrings, s.upper()))
    for i in range(0,len(sanitisedS)//2):
        if sanitisedS[i] != sanitisedS[len(sanitisedS) - 1 - i]:
            return False
    return True


print(isPalindrome(s))
