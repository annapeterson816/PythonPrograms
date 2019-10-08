n = int(raw_input("Enter a number to create the multiplication table: "))


def printMultTable(n) :
    top_row = range(1,n+1)
    side_column = range(1, n+1)
    mult_table=[]

    for i in top_row :
        mult_string = ""
        for j in side_column :
            mult_string= mult_string + str(i*j) + " "
            
        print mult_string
            

    
            
print printMultTable(n)
