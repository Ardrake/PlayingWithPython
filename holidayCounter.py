#!/usr/bin/env python3

'''You go on a wonderful holiday leaving on day number 3 (a Wednesday). 
You return home after 137 nights. 
Write a general version of the program which asks for the starting day number, 
and the length of your stay, and it will tell you the number of day of the week 
you will return on.'''

startDay = int(input('Enter the number of the weekday when holiday started: '))

numDays = int(input('Enter number of days spent on holidays: '))

numWeeks = numDays // 7 # number of weeks spent

endDay = (numDays % 7)
endWeekday = endDay + startDay    # week day 

print('You spent', numWeeks,'weeks and', endDay,'days on your holidays. \n \
Day of the week that you return back is', endWeekday)




