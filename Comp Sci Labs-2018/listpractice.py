list1=[1,5,2,3,4]


def onlyEvens(list1):
    i=0
    while (i< len(list1)):
        if(list1[i]%2 != 0):
            list1[i]=0
        i=i+1

    print "Replaced odds in list with 0: " + str(list1)

print onlyEvens(list1)


    

inputList = [[2,3],[4,5],[6,1]]

def larger(inputList):
    larger_list=[]

    for i in inputList :
        largest_num=0
        for j in i:
  
            if(j>largest_num):
                largest_num=j
                
        larger_list.append(largest_num)

    print "This is the largest num in each individual list: " + str(larger_list)


print larger(inputList)        


l=[8,3,2,5,0,-1,100,4,2]

def minMax(l):
    min_max= [100000000, -100000000]
    
    for i in l:
        if(i <min_max[0]):
            min_max[0]=i
        if(i>min_max[1]):
            min_max[1]=i

    print "The minimum and maximum of this list, respectively, is: " +str(min_max)

print minMax(l)



def merge(list1,list2):
    if (len(list2)>=1):
        for i in list2:
            list1.append(i)
        

        print "The sorted list is: " + str(sorted(list1))

    elif (len(list1)>=1):
        for i in list1:
            list2.append(i)
        

        print "The sorted list is: " + str(sorted(list2))

    else:
        print "Neither list has any elements. Retry and make sure one or both lists have values"



print merge([3,6,10],[2,7,18])    
        
        
        

    

        


        

        
