number = int(raw_input("Pick a number: "))

import math

def prime(number) :

    i= 2
    j=0
    array = range(1,number+1)
   
    for j in array :
        num_of_factors =0
        value = array[j]
        while i<= value/2:
            
            if value % i == 0 :
                num_of_factors=num_of_factors+1
                
            i=i+1
            
        if(num_of_factors> 0) :
            print str(value) + " is not a prime number"
        elif (num_of_factors ==0) :
            print str(value) + " is a prime number"


    print prime(number)
                



        

    

            


        
                
                
            
                
            
        

 
