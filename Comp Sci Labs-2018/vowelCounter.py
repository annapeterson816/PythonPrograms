string = raw_input("Enter a string: ")

vowels= ['a','e','i','o','u','y']



def vowelCounter() :
    length=len(string)
    vowel_count=0
    i=0

    while i<length :
        for j in vowels :
            if string[i] == j :
                vowel_count = vowel_count+1
        i=i+1
    print string + " has a vowel count of: " + str(vowel_count)
        

print vowelCounter()
            

        
        
