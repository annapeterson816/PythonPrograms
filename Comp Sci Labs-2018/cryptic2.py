encoded_str= raw_input("Enter the encoded string: ")
lower_list=[]

def lower(encoded_str):
    lower_str=encoded_str.lower()

    #turn the string into a list, easier to traverse
    for i in lower_str:
        lower_list.append(i)

    return lower_list


#printing the list as a string (easier for user to see)
lower(encoded_str)

lower_str=""
for i in lower_list:
    lower_str=lower_str+i

print "lowercase string is: " , lower_str


    
#removing special characters (anything but lowercase letters)

removed_list=[]

def strip(lower_list):

    for char in lower_list:

        if ord(char) >96 and ord(char) <123:
            removed_list.append(char)
        
    return removed_list

strip(lower_list)


#printing the coded message without special characters as a string, not as a list

specials_stripped=""
for i in removed_list:
    specials_stripped = specials_stripped + i

print "With the specials stripped out the string is: " , specials_stripped

#entering the code key and determining if it is correct

key_code = raw_input("Enter the code_key: ")

def isCorrectKey():
    if key_code =='crypt':
        print decode(removed_list, offset)
    else:
        print "Sorry! That is the incorrect code key."

    
#offset
offset= int(raw_input("Offset: "))
print "offset = " + str(offset) 

#decoding the string

decoded_string=""

def decode(removed_list, offset):
     
    i=0
    remainder=0
    decoded_string=""
    
    while i<len(removed_list):
        ascii=ord(removed_list[i])


        if ascii+offset < 123: 
            decoded_string= decoded_string + chr(ascii+offset)

        else:
            remainder=123-ascii-offset
            decoded_string=decoded_string +chr(97-remainder)
            
        i=i+1
    
    
    return "Your decoded string is: "+ decoded_string

print isCorrectKey()




    


        
    
