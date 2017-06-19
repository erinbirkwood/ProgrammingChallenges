import sys
import math

input = []
for line in sys.stdin:
    line = line.replace('\n', '')
    input.append(line)

data = (input.pop(0)).split() #get info, convert to float
data = map(float, data)
articles = data[0]
factor = data[1]

impact = articles*factor #get rough factor, then see if it can be decreased
cont = True
while (cont):
    if math.ceil((impact-1.0)/articles) == factor: #can decrease num scientists
        impact -= 1
    else:
        cont = False

print int(impact)

