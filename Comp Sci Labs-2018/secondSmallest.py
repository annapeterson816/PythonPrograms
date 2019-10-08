L=[1,6,8,9,3,4,10,50,7,1,3,2]

def secondSmallest(L):
    smallest=10000000
    second_smallest=99999

    if len(L)==1:
        second_smallest=L[0]
    elif len(L) ==0:
        return "None"
    else:
        for i in L:
            if i<second_smallest and i<smallest:
                smallest=i
            elif i<second_smallest and i>smallest:
                second_smallest=i

    return second_smallest


print secondSmallest(L)


        
