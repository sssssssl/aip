# demeonstrate iterator behaviors

L = [1, 2, 3, 4]

def never_end(L):
    for x in L:
        L.append(10-x)

def end_early(L):
    for x in L:
        L.pop(0)
