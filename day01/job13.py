# Job 1.3 :

def grade(L): 
    l = []
    for i in L: 
        if i < 40:
            l.append(i)
        elif i >= 40:
            if (i + 1) % 5 == 0:
                l.append(i + 1)
            elif (i + 2) % 5 == 0:
                l.append(i + 2)
            else:
                l.append(i)
    return l

# Test : 
T = [38, 42, 83, 57, 92]
NewList = grade(T)
print(NewList)