def prime2(number) :

    

    for num in range(2,number):
        prime=True
        for i in range(2,num):
            if (num%i==0):
                prime= False

        if(prime==False) :
            print str(num)+ " is not a prime number."

        else:
            print str(num) + " is a prime number."
