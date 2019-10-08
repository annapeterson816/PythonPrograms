task_list=[[5.5, "Wake Up"], [9, "Class"],[23, "Go to bed"]]

def printList(task_list):
    print "\nTODAY'S TASK LIST\n(Ascending Order)"
    for i in task_list:
        if i[0]<12:
            if i[0]%1==0:
                print str(int(i[0]))+ ":00 A.M " +i[1]
            else:
                stri=str(i[0])
                minutes =int((i[0]%1)*10)
                print str(stri[0:1]) + ":" + str(minutes) + "0 A.M. " + i[1]
        if i[0]>=12 and i[0]<13:
            if i[0]%1==0:
                print str(int(i[0]))+ ":00 P.M " +i[1]
            else:
                stri=str(i[0])
                minutes =int((i[0]%1)*10)
                print stri[0:1] + ":" + str(minutes) + "0 P.M. " + i[1]
        if i[0]>=13:
            if i[0]%1==0:
                print str(int(i[0]-12))+ ":00 P.M " +i[1]
            else:
                stri=str(i[0]-12)
                minutes =int((i[0]%1)*10)
                print stri[0:1] + ":" + str(minutes) + "0 P.M. " + i[1]

#printing the starting task list
printList(task_list)

def addTask():
    activity= raw_input("\nWhat activity would you like to add?")
    time = float(raw_input("What time does this activity start?"))
    print "\n"

    task_list.append([time,activity])
    return task_list

addTask()
addTask()

more_input = raw_input("Do you want to add more specific actvities? Type Y for yes and N for no")
if (more_input=='Y'):
    addTask()

#inserting a task at a certain time 
def insertTask(task_list):
    task_list=sorted(task_list)
    time_insert= float(raw_input("\nWhat time do you want to insert?"))
    activity_insert= raw_input("What activity would you like to add?")
    

    index=0
    while index< len(task_list):
        if (time_insert < task_list[index][0]):
            task_list.insert(index, [time_insert,activity_insert])
            break
        index=index+1

    print "\n After inserting the task:", activity_insert 

    printList(task_list)

#deleting a task at a certain time 
def deleteTask(task_list):
    task_list=sorted(task_list)
    delete_time= float(raw_input("\nWhat time do you want to delete?"))
    for i in task_list:
        if i[0]==delete_time:
            task_list.remove(i)
    
    print "\nAfter removing the activity at the time: " , delete_time
    printList(task_list)

#clearing the schedule
def deleteAll():
    index=0
    while index<len(task_list):
        task_list.remove(task_list[index])
        index=index+1

    return "\nList after removing all:\nTODAY'S TASK LIST\nNo agenda!"

#reversing the schedule with recursion

task_list=sorted(task_list)
def reverse(index):
     if index<0:
         return 0
        
     else:
        return str(task_list[index][0]) + " " + str(task_list[index][1]) + "\n" +  str(reverse(index-1))
    
insertTask(task_list)
deleteTask(task_list)

index=len(task_list)-1 #6
print " \nAfter reversing the list to descending order \nTODAY'S TASK LIST \n(Descending Order) "
print reverse(index)

print deleteAll()






    


    
