list1=[2,8,13,11,4,10,12,7]



def isPrime(var):
    prime=0
    for j in range(2,var):
        if (var%j==0):
            prime= prime+1
            
    if prime>0:
        return False
    else:
        return True

                


def sumPrime(list1):
    prime_list=[]

    for i in list1:
        if (isPrime(i)==True):
            prime_list.append(i)

    prime_sum=0
    for num in prime_list:
        prime_sum= prime_sum + num
        

        
    return "The sum of the prime numbers is: " + str(prime_sum)
    


print sumPrime(list1)
