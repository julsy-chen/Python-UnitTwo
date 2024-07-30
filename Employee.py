def goodEmp(lst, t):
    if not lst:
        return 0
    elif t == 0:
        return len(lst)
    else:
        # working towards base case: go towards empty list
        if lst[0] >= t:
            return 1 + goodEmp(lst[1:], t)
        else:
            return goodEmp(lst[1:], t)
        

print(goodEmp([1,2,3,4,5,6],2))