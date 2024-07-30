def listMerger(a, b):
    if not b:
        return a
    if not a:
        return b
    if b:
        a.insert(len(a) - len(b))
        return(listMerger(a, b))
    
print(listMerger([1,2,3],[4,5,6]))

