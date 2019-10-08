total_apples = raw_input("How many apples did you collect?")
total_apples = int(total_apples)

remaining_apples = total_apples % 3

each_person = (total_apples - remaining_apples) / 3
 
moms_apples = remaining_apples

each_person = str(each_person)

moms_apples = str(moms_apples)
 
print "How many apples can each person take: " + each_person + "\n" + "How many are left over for Mom: " + moms_apples

 

