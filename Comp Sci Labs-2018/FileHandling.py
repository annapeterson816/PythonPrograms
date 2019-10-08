fhandle = open("familybday.txt" , "w")
fhandle.write("Anna P: 7/15/1999 \n")
fhandle.write("Mom: 10/13/1967")
fhandle.close()

fhandle = open ("familybday.txt","r")
count=0

for line in fhandle:
   line=line.rstrip() #gets rid of the gap in between 
   print line
   count+=1

   #if line.startswith("Anna"):
     # print "^That is you! \n"


print "Number of people:" , count
fhandle.close()


#other family members:
family=["Chris", "Kerry","Zoe", "Kevin", "Nick", "Anna", "Jake"]
fhandle=open("familybday.txt", "w")
fhandle.write("\n")
for name in family:
   fhandle.write(name + "\n")

fhandle.close

fhandle=open("familybday.txt","r")
for line in fhandle:
   line=line.rstrip()
   print line

fhandle.close()


