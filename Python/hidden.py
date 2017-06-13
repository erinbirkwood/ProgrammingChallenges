import sys

input = []
for line in sys.stdin:
    line = line.replace('\n', '')
    input.append(line)

input = (input.pop(0)).split() #store in list
pwd = list(input[0]) #the password
msg = list(input[1]) #the message

accept = True
while (pwd and accept): #while there are remaining chars in pwd, and is acceptable
    pwd_nxt = pwd.pop(0)
    if (msg):
        while (msg):
            msg_nxt = msg.pop(0)
            if msg_nxt == pwd_nxt: #correct ordering
                accept = True
                break
            elif msg_nxt in pwd: #incorrect ordering
                accept = False
                break
            else:
                accept = False
    

if (accept): #acceptable, and checked entire pwd
    print "PASS"
else:
    print "FAIL"
        

