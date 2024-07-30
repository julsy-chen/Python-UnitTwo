def primeCheck(num):
    def helper(num, div):
        if num == div:
            return True
        else:
            if num % div == 0:
                return False
            else:
                return helper(num, div + 2)
    if num < 1:
        return False
    elif num in {2, 3, 5, 7}:
        return True
    elif num % 2 == 0:
        return False
    else:
        return helper(num, 3)
    

def primeCheck2(num, div = 3, tail = True):
    if not tail:
        return False
    elif num == div:
        return tail
    elif num <= 1:
        return False
    elif num in {2,3}:
        return True
    elif num % 2 ==0:
        return False
    else:
        if num % div == 0:
            return primeCheck2(num, div, False)
        else:
            return primeCheck2(num, div+2, True)