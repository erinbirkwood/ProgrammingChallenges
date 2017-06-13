import sys
import math

input = []
for line in sys.stdin:
    line = line.replace('\n', '')
    input.append(line)

data = (input.pop(0)).split() #get raw data

#separate data into separate info
bob_age = int(data[0])
bob_ret = int(data[1])
bob_sav = int(data[2])
alice_age = int(data[3])
alice_sav = int(data[4])
alice_ret = alice_age #initialize her retirement age to her current age

alice_bank = 0 #initalize her bank to 0
bob_bank = (bob_ret - bob_age)*bob_sav #find bob's bank amount when he retires
while (alice_bank <= bob_bank):
    alice_ret += 1
    alice_bank = (alice_ret - alice_age)*alice_sav

print alice_ret



