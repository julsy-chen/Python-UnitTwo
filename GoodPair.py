def ez(lst, t):
    if len(lst) in {0,1}:
        return 0
    else:
        if lst[0] == t:
            return 1 + ez(lst[1:], t)
        else:
            return ez(lst[1:], t)
        
def goodPair(lst):
    if not lst:
        return 0
    else:
        return ez(lst[1:], lst[0]) + goodPair(lst[1:])
        
