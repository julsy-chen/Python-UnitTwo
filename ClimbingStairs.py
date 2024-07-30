def stairs(steps):
    if steps in {0,1,2}:
        return steps
    else:
        return stairs(steps-1) + stairs(steps-2)
    
print(stairs(120))