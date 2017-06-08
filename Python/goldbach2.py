import sys

input = []
for line in sys.stdin:
    line = line.replace('\n', '')
    input.append(int(line))

input.pop(0)

not_prime = [] #store numbers we know are not prime
prime = [2] #store numbers we know are prime

def check_prime(num):
    if (num%2 == 0): #not prime
        return False
    else: 
        for i in range(3, num/2+1, 2): #don't check even numbers
            if (num%i == 0):
                not_prime.append(num)
                return False        
        prime.append(num)
        return True

answer = [[] for i in range(len(input))]
for i in range(len(input)):
    temp = input[i] - 2
    if temp in prime:
        answer[i].append ("2+" + str(temp))
    elif temp in not_prime:
        pass
    else:
        if check_prime(temp) == True:
            answer[i].append ("2+" + str(temp))
    for j in range (3, input[i]/2+1, 2):
        if j in prime:
            temp = input[i] - j
            if temp in prime:
                answer[i].append (str(j) + "+" + str(temp))
            elif temp in not_prime:
                pass
            else: 
                if check_prime(temp) == True:
                    answer[i].append (str(j) + "+" + str(temp))
        elif j in not_prime:
            pass
        else:
            if (check_prime(j) == True):
                temp = input[i] - j
                if temp in prime:
                    answer[i].append (str(j) + "+" + str(temp))
                elif temp in not_prime:
                    pass
                else: 
                    if check_prime(temp) == True:
                        answer[i].append (str(j) + "+" + str(temp))

for i in range (len(input)):
    if i != 0:
        print ""
    print str(input[i]) + " has " + str(len(answer[i])) + " representation(s)"
    for j in range(len(answer[i])):
        print answer[i][j]

