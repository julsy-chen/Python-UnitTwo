def exp(base, power):
    # non-tail version
    if power == 0:
        return 1
    elif power == 1:
        return base
    elif power < 0:
        return 1 / (base * exp(base, power-1))
    else:
        return base * exp(base, power-1)
    
def exp1(base, power, tail=1):
    # tail version
    if power == 0:
        return tail
    elif power < 0:
        return exp1(base, power+1, 1/(tail*base))
    else:
        return exp1(base, power-1, tail*base)
    
[print(exp1(2,-1))]