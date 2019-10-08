def pizza() :

    cheese_toppings=['Mozzarella', 'Cheddar', 'Provolone', 'Colby']
    other_toppings=['Pepperoni', 'Sausage', 'Veggie', 'Pineapple']
    customized_pizza=[]
    price = 6

    print "Let's make a pizza! First you will pick what cheese(s) you want, then you can add any of the 4 additional toppings after that."

    print "Your cheese options are: " + str(cheese_toppings)

    wantcheese = raw_input("Do you want cheese on your pizza? Type Y or N ")

    if (wantcheese == 'Y'):
        price = price + 1
        cheese = raw_input("Type in what type of cheese you want  ")
        customized_pizza.append(cheese)

    print " \n Now, here are the list of additional toppings: " + str(other_toppings)

    topping = int(raw_input("If you want pepporoni, type 1. If you want cheddar, type 2.. and so on. Type only one number. "))
    customized_pizza.append(other_toppings[topping-1])

     
    while(topping != 5) :
        customized_pizza.append(other_toppings[topping-1])
        price =price +.5
        
        topping=int(raw_input(" \n \n If you want another topping, type in the number of the topping. \n If you are done adding toppings, type 5"))
      
        


    print "\n This is your pizza: " + str(customized_pizza)
    print " The total prize of your pizza is : $ " + str(price)
    print " \n Enjoy!"

print pizza()
    
                            
                           
                           

    

    

    
    
