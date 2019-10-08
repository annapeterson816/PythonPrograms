string = raw_input("Enter the DNA strand  ")


def analyzeDNA(string) :
    bases=['A', 'C', 'T','G']
    count=[0,0,0,0]
    

    for i in string :
        trace=0
        for j in bases :
            if i == j :
                count[trace] =count[trace]+1
            trace=trace+1
    
    print "A:" + str(count[0]) + "  C:" + str(count[1]) + "  T:" + str(count[2]) + "  G:" + str(count[3])
    

print analyzeDNA(string)
