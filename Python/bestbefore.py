import sys
import itertools

input = []
for line in sys.stdin:
    line = line.replace('\n', '')
    input.append(line)

#months that can have 31 days
months_31 = ["01", "03", "05", "07", "08", "10", "12"]

def leapYear(int_year): #check leap year
    if (int_year % 4 == 0):
        if (int_year % 100 == 0) and ((int_year % 400) != 0):
            return False
        return True
    return False

def makeDate(year, month, day):
    #format year
    if len(year) == 4:
        if int(year) < 2000 or int(year) > 2999:
            return -1
    if len(year) == 3:
        year = "2" + year
    if len(year) == 2:
        year = "20" + year
    if len(year) == 1:
        year = "200" + year
    #format month
    if (int(month) > 12) or (int(month) == 0): #cannot be a month
        return -1
    else:
        if len(month) != 2: #zero padding, else, fine
            month = "0" + month
    #format day
    if (int(day) > 31) or (int(day) == 0): #cannot be a day
        return -1
    else:
        if len(day) != 2: #zero padding, else, fine
            day = "0" + day
    #SPECIAL CASES
    #1. check leap year special case (feb 29 + not leap year)
    if leapYear(int(year)) == False:
        if month == "02" and day == "29":
            return -1
    #2. check february case if not leap year
    if month == "02" and int(day) > 29:
            return -1
    #3. check for conflicting months and days
    if month not in months_31 and day == "31":
        return -1
    return year+month+day
    
original = (input.pop(0)) #save original date  
ambiguous = original.split('/') #ambiguous date
dates = [] #list of possible dates

#create all permutations of ambiguous date
possible_dates = list(itertools.permutations(ambiguous))
#iterate through all possible dates
for i in range(len(possible_dates)):
    current = possible_dates[i]
    if makeDate(current[0], current[1], current[2]) != -1:
        dates.append(makeDate(current[0], current[1], current[2]))

dates.sort() #find earliest date

if len(dates) == 0: #impossible
    print original + " is illegal"
else: #print best before date
    year = dates[0][:4]
    month = dates[0][4:6]
    day = dates[0][6:]
    print year + "-" + month + "-" + day

