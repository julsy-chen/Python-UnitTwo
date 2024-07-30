# Factorial
# non tail
def factorial(num):
    if num in {1,2}:
        return num
    elif num == 0:
        return 1
    else:
        return num * factorial(num-1)

# tail
def factorialTail(num, tail = 1):
    if num == 0:
        return tail
    else:
        return factorialTail(num - 1, tail * num)
    
# Exponentation
# non tail
def exp(base, power):
    if power == 0:
        return 1
    elif power == 1:
        return base
    else:
        return base * exp(base, power-1)
    
# tail
def expTail(base, power, tail = 1):
    if power == 0:
        return tail
    else:
        return exp(base, power-1, tail * base)
    
# Palindrome
# not tail
def pal(x):
    if len(x) in {0,1}:
        return True
    elif x[0] != x[-1]:
        return False
    else:
        return pal(x[1:-1])

# tail
def palTail(x, tail = True):
    if len(x) in {0,1}:
        return tail
    elif x[0] != x[-1]:
        return False
    else:
        return palTail(x[1:-1])
    
# Reverse a String
# not tail
def rev(word):
    if len(word) <= 1:
        return word
    else:
        return word[-1] + rev(word[:-1])
    
# tail
def revTail(word, result = ''):
    if not word:
        return result
    else:
        return revTail(word[:-1], result + word[-1])
    
# Max Element
# not tail
def max(lst):
    return None

# tail
def maxTail(lst):
    def helper(a_list, tail):
        if not a_list:
            return tail
        else:
            if a_list[0] > tail:
                return helper(a_list[1:], a_list[0])
            else:
                return helper(a_list[1:], tail)
    # end of helper()
    if not lst:
        return -1 # error
    elif len(lst) == 1:
        return lst[0]
    else:
        return helper(lst[1:], lst[0])

# Merge Sorted Lists
# not tail
def merge(a_list, b_list):
    if not a_list and not b_list:
        # both lists are empty
        return []
    elif not a_list: # a lst is empty
        return b_list
    elif not b_list: # b lst is empty
        return a_list
    else:
        if a_list[0] < b_list[0]: # comparing the first index in a lst in relation to the first index of b lst
            return [a_list[0]] + merge(a_list[1:], b_list) # if the first index of a lst is smaller than the first index of b, then add the first index of a to the merged list and compare the two lists again without the "first" index of a
        else:
            return [b_list[0]] + merge(a_list, b_list[1:]) # vice versa
        
# tail
def mergeTail(list1, list2, a = []):
    if not list1 and not list2:
        # both lists are empty
        return a
    elif not list1: # a lst is empty
        return a + list2
    elif not list2: # b lst is empty
        return a + list1
    else:
        if list1[0] < list2[0]:
            return mergeTail(list1[1:], list2, a + [list1[0]])
        else:
            return mergeTail(list1, list2[1:], a + [list2[0]])
        
# Prime Checker
# tail
def primeCheck(num, f = 3):
    if num == f:
        return True
    elif num < 2:
        return False
    elif num in {2, 3, 5}:
        return True
    elif num % 2 == 0:
        return False
    elif num % f == 0:
        return False
    else:
        return primeCheck(num, f + 1)
    
# not tail
def primeCheckTail(num):
    def helper(dividend, divisor):
        if dividend == divisor:
            return True
        elif dividend % divisor == 0:
            return False
        else:
            return helper(dividend, divisor + 1)
    if num < 2:
        return False
    elif num % 2 == 0:
        return False
    elif num in {2, 3, 5}:
        return True
    else:
        return helper(num, 3)
    
# List of Prime Factors
# tail
def primeListTail(num, f = 3, a = []):
    if int(num) == 1:
        return a
    elif num < 1:
        return -1
    elif num % 2 == 0:
        a.append(2)
        return primeListTail(num / 2, f, a)
    elif num % f == 0:
        a.append(f)
        return primeListTail(num / f, 2, a)
    else:
        return primeListTail(num, f + 2, a)
       
# not tail
def primeList(num, f = 2):
    if num < 1:
        return -1
    elif num == 1:
        return []
    elif num == f:
        return [num]
    else:
        if num % f == 0:
            return [f] + primeList(num//f, f)
        else:
            return primeList(num, f+1)

# Climbing Stairs\
# not tail
def stairs(num):
    if num < 0:
        return -1
    elif num in {0,1,2}:
        return num
    else:
        return stairs(num - 1) + stairs(num-2)
    
# tail
def stairsTail(num, tail = 0):
    if num in {0,1,2}:
        return num
    elif num < 0:
        return -1
    else:
        return stairs(num-1, tail+1) + stairs(num-2, num+2)
    
print(stairsTail(6))