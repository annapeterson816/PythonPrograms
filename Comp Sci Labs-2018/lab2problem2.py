
age = int(raw_input("Please input your age: "))

max_heart_rate = 220-age
print "Your Maximum Heart Rate (MHR) is : " + str(max_heart_rate) + "\n"

objective = float(raw_input("Please indicate your exercise objective as follows \n 1 = weight loss, building endurance \n 2 = weight management, improving cardio fitness \n 3 = interval workouts \n \n input your objective:  "))



def THRzones(max_heart_rate, objective) :

     top_beat= 0
     bottom_beat = 0

     if (objective ==1) :
         bottom_beat = max_heart_rate *.6
         top_beat = max_heart_rate * .7
         return "Your Target Heart Rate zone is: " + str(bottom_beat) + " - " + str(top_beat) + " beats per minute"

     if (objective ==2) :
        bottom_beat = max_heart_rate *.7
        top_beat= max_heart_rate *.8
        return "Your Target Heart Rate zone is: " + str(bottom_beat) + " - " + str(top_beat) + " beats per minute"

     if(objective==3) :
        bottom_beat= max_heart_rate *.8
        return "Your Target Heart Rate zone is: " + str(bottom_beat) + " and beyond beats per minute"
     
     return bottom_beat


print THRzones(max_heart_rate,objective)
         
