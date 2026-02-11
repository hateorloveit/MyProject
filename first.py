def searchMinFromList(L,n):
    minValue = L[0]
    counter = 1
    while (counter < n):
        v = L[counter]
        if( v < minValue):
            minValue = v
            idx = counter
        else:
            pass

    return minValue , idx
    