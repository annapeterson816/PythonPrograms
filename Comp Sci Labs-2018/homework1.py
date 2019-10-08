
def moLoan() :

    print "This program screens for couples seeking low cost mortgage loans"
    print "Couples need 5 points to Points to qualify \n \n"
    print "For the applicants: "

    age1 = int(raw_input("Person one, Enter your age: "))
    age2 = int(raw_input("Person two, Enter your age: "))
    print "For the loan officer: \n"
    median_print =int(raw_input("Enter median print of homes in this area during past 12 months: "))

    print " \n For the applicants: "
    relationship_length = int(raw_input("Enter years you have been legally connectected in marriage or a civil union: "))
    employed = raw_input("Both gainfully employed for 48 weeks, Y or N? ")
    price_of_home = int(raw_input("Enter the price of home, in USD: "))

    print " \n Enter credit scores. Both person's must be in berween 300 and 850"

    credit1 = int(raw_input("Enter person one's credit score: "))
    credit2 = int(raw_input("Enter person two's credit score: "))

    points=0

    #age requirement
    if((age1>=25 and age1<=30) and (age2>=23 and age2<=35)):
       points = points+1
       
    elif((age2>=25 and age2<=30) and (age1>=23 and age1<=35)) :
       points = points+1

    #marriage
    if(relationship_length >=1 and relationship_length<=5) :
         points=points+1

    #employed
    if(employed == 'Y'):
         points=points+1
         
    #price of home
    if(median_print -5000 >= price_of_home):
         points=points+1

    #credit score
    if(credit1>=700 and credit2>=700) :
         points= points+1


    if(points>=5) :
        print " \n Congratulations! You have qualified: " + str(points) + " points"
        print "\n \n For the loan officer"
        interest = float(raw_input("Please enter the present interest rate: "))
        new_rate=float(interest)

        avg_cred_score = float(credit1+credit2) /2
        if(avg_cred_score >= 800):
            new_rate=interest-(3.0/8)
        elif(avg_cred_score >= 775 and avg_cred_score <=799):
            new_rate=interest -(1.0/4)
        elif(avg_cred_score >=750 and avg_cred_score <=774):
            new_rate=interest-(1.0/8)
        else:
            new_rate=interest

        print "Your interest rate is: " + str(new_rate) +"%"
                              

    else :

        print "Sorry, you needed at least 5 points to qualify and you have : " + str(points) + " points. Seek assistance with your loan officer." 




print moLoan()



    
                        
                             
                     

                     
