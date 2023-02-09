# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar
wd= ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY']
str = input()

month=int(str[:2])
day=int(str[3:5])
year=int(str[6:])

#print(day,month,year)
print( wd[calendar.weekday(year, month, day)])

#for i in range(1,29):
#    print( i,wd[calendar.weekday(2023, 2, i)])lp