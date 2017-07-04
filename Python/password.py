import sys
import operator

input = []
for line in sys.stdin:
    line = line.replace('\n', '')
    input.append(line)

num_pwds = float(input.pop(0))

pwd_dict = {} #store passwords and probability

while(input):
    pwd_info = (input.pop(0)).split()
    word = str(pwd_info[0])
    prob = float(pwd_info[1])
    pwd_dict[word] = prob

sorted_pwds = sorted(pwd_dict.items(), key = operator.itemgetter(1), reverse = True) #sord pwds by probability

attempts = 0.0 #keep track of avg attemps
count = 1.0 #keep track of passowrd likelihood

#add probability that it takes x attempts * attempt number
for pwd in sorted_pwds:
    attempts += count * pwd[1]
    count += 1.0

print attempts
