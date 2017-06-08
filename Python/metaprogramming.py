import sys

input = []
for line in sys.stdin:
    line = line.replace('\n', '')
    input.append(line)

vars = {} #dictionary of variables

#define variable
def define(var, value):
    vars[var] = int(value)

#evaluate variable
def eval(var1, operator, var2):
    if (var1 in vars) and (var2 in vars):
        if operator == '<':
            return vars[var1] < vars[var2]
        elif operator == '>':
            return vars[var1] > vars[var2]
        else: #operator is =
            return vars[var1] == vars[var2]
    else:
        return "undefined"


while (input): #while there is still input
    curr = (input.pop(0)).split()
    if curr[0] == 'define':
        define(curr[2], curr[1])
    else: #it's an eval
        print eval(curr[1], curr[2], curr[3])
