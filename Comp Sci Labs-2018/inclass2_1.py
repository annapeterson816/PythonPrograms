
number = int(raw_input("How many numbers do you want?"))

def fib(number) :
    i=0
    j=1
    k=1
    while i<number :
        print j
        num = k
        k= j+k
        j=num
        i=i+1

        
print fib(number)
