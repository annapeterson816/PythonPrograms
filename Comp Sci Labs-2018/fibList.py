n = int(raw_input(" How many numbers do you want? "))

def FibList() :
    i=0
    j=1
    k=1
    fib_list = [1,1]
    while i<n :
        fib_list.append(fib_list[i] +fib_list[j])
        j=j+1
        i=i+1

    print fib_list
    
print FibList()
