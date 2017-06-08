import sys
from collections import Counter

input = []
for line in sys.stdin:
    input = line.replace('\n','') #get input
    count = Counter(input) #create counter for input
    odd_letters = [None for num_letters in count.values() if num_letters % 2] #number of letters that appear only once
    if odd_letters: #must remove all but one letter that appears once
        output = len(odd_letters)-1
    else: #has only even number of each letter present
        output = 0
    print output


