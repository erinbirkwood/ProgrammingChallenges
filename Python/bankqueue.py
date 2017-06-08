import sys

input = [] #get user input
for line in sys.stdin:
    line = line.replace('\n','')
    input.append(line)

raw_instruc = (input.pop(0)).split() #get first line
num_people = int(raw_instruc[0]) #find num of people
time_left = int(raw_instruc[1]) #find amount of time left

cust_list = [] #create list of customers, $ and waiting times
for line in input:
    temp = line.split()
    temp = [int(x) for x in temp] #turn list elements into ints
    cust_list.append(temp)

cust_list.sort(key = lambda x:x[0], reverse=True) #sort by amount of money of customer

time_passed = 0 #how long it's been since customers have waited in line
final_cust = []
restrict_index = []
restrict_list = [0 for x in range(0, time_left+1)] #store taken positions of queue for customers who may leave before closing

while ((time_passed < time_left) and (len(cust_list) > 0)): #while there are still time and customers left
    curr_cust = cust_list.pop(0)
    if (curr_cust[1] <= time_left): #if this customer may leave before closing
        i = curr_cust[1]
        while (i >= 0): #check if there is a timeslot open that would suit this customer
            if restrict_list[i] == 0: #this means there is a spot open, so add the customer
                restrict_list[i] = 1
                final_cust.append(curr_cust)
                time_passed += 1
                break
            i -= 1

    else: #otherwise, this customer is not going to leave before closing, so accept them
        final_cust.append(curr_cust)
        time_passed += 1

total_money = 0 #find the total money
for cust in final_cust:
    total_money += cust[0]

print total_money

