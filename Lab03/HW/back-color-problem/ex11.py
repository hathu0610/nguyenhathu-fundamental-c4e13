
def is_inside(myList=[],otherList=[]):
    x = myList[0]
    y = myList[1]
    x1 = otherList[0]
    y1 = otherList[1]
    width = otherList[2]
    length = otherList[3]
    res = True
    if x >= x1 and x <= x1 + width and y>= y1 and y<=y1+length:
        res = True
    else:
        res = False
    
    return(res)


# result = is_inside(200, 120)

