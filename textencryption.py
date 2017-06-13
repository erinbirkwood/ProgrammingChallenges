import sys
import operator

input = []
for line in sys.stdin:
    line = line.replace('\n', '')
    input.append(line)

input.pop() #pop the zero at the end, don't need it

def encrypt(n, old_msg, new_msg): #encryption function
    index = 0
    offset = 0 #how much to shift in array
    while (old_msg): #take all chars of old msg
        curr = old_msg.pop(0)
        if index >= len(new_msg): #if out of bounds, increase offset
            offset += 1
            index = offset
        new_msg[index] = curr      
        index += n #increase by n val
    return new_msg

while (input): #while there are still cases
    n_val = int(input.pop(0))
    phrase = (input.pop(0)).replace(" ", "") #remove spaces
    phrase = list(phrase.upper()) #make uppercase and into list
    if len(phrase) < n_val: #cannot encyrpt
        phrase = "".join(phrase)
        print phrase
    else: #encrypt
        encrypted = [" " for i in range(len(phrase))]
        result = encrypt(n_val, phrase, encrypted)
        result = "".join(result) #create string
        print result