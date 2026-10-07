#1a) How many minutes until the due date at 8am September 10th, from 11:08am on September 3rd.  
SixDays=(6*24)*60    #The 3rd to the 9th is 6 days, and given the time we just subtract a few minutes.
MinusMinutes=(60*3)+8   #8am and 11:08am are 3 hours and 8 minutes apart
MinsUntilDue=SixDays-MinusMinutes
print(MinsUntilDue)

#1b) Using total minutes, how many hours and mins until due?
FullHours=MinsUntilDue//60
MinsLeft=MinsUntilDue%60
print(FullHours, "hours and",MinsLeft, "minutes until the due date")

#1c) How many days, hours, and mins until due?
DaysUntil=FullHours//24
LeftOverHours=FullHours%24
print("There are",DaysUntil,"days",LeftOverHours,"hours, and",MinsLeft,"minutes until the due date")

#2a)Find the date and time given the stop watch reading 92 hours and 23 minutes. 
Hours=92
Minutes=23
DaysPassed=Hours//24
HoursLeft=Hours%24
print(DaysPassed,"days",HoursLeft,"hours","and",Minutes,"minutes have passed")

#2b) Need to now add the minutes, hours, and days to our intial date and time
Addmins=8+Minutes #8 because we started at 11:08
Addhours=11+HoursLeft
print(Addmins)
print(Addhours)

#because adding the hours is greater than 24 we need to start a new day

Newday=Addhours//24
print(Newday)
NewDayHours=Addhours%24
print(NewDayHours)

#Now we know we have to go 7 more hours past 3 days because 20 hours added to 11:08 goes into the next day

TotalDaysPassed=Newday+DaysPassed
print(TotalDaysPassed)

print("Since the outage",TotalDaysPassed,"days",NewDayHours,"hours, and",Minutes,"minutes have passed, making it Monday Septmber 7th at 7:23am")

