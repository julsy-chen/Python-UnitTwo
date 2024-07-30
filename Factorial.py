def factorial(num):
    if num in {0,1}:
        return 1
    else:
        return num * factorial(num-1)


def f2(num, tail=1):
    if num in {0,1}:
        return tail
    else:
        return f2(num-1, tail*num)
    
def isPalindrome(word):
        # base case
    if not word:
        return True
    elif len(word) == 1:
        return True
    elif len(word) == 2 or len(word) == 3:
        return word[0] == word[-1]
    else:
        return word[0] == word[-1] and isPalindrome(word[1:-1])