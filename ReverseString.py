def rev(w):
    if len(w) in {0,1}:
        return w
    else:
        return w[-1] + rev(w[:-1])        

print(rev("String"))

def rev1(w, r = ""):
    if not w:
        return r
    else:
        return rev1(w[:-1], r + w[-1])
    
print(rev1("String"))
    