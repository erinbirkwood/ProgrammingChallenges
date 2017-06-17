import sys

input = []
for line in sys.stdin:
    line = line.replace('\n', '')
    input.append(line)

def addDef(words, nums, word, num): #add a new definition
    words[word] = num
    nums[num] = word

def getCalc(words, nums, function): #perform a calculation
    function_str = ' '.join(function) #portion of result, save
    result = 0
    first = function.pop(0) #get first element
    if first in words:
        result += int(words[first])
    else:
        return function_str + " unknown"
    while (function):
        op = function.pop(0)
        if op == '=': #done
            break
        elif op == '+':
            next = function.pop(0)
            if next in words:
                result += int(words[next])
            else:
                return function_str + " unknown"
        else: #op == '-'
            next = function.pop(0)
            if next in words:
                result -= int(words[next])
            else:
                return function_str + " unknown"

    #check if final result is valid
    if result in nums: 
        return function_str + " " + nums[result]
    else:
        return function_str + " unknown"

word_dict = {} #dictionary of words:nums
num_dict = {} #dictionary of nums:words

while (input):
    code = (input.pop(0)).split(' ')
    instruct = code.pop(0)
    if instruct == 'def':
        addDef(word_dict, num_dict, code[0], int(code[1]))
    elif instruct == 'calc':
        print getCalc(word_dict, num_dict, code)
    else: #is 'clear'
        word_dict = {}
        num_dict = {}