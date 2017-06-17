import sys

input = []
for line in sys.stdin:
    line = line.replace('\n', '')
    input.append(line)

num_msgs = int(input.pop(0)) #num messages

#number dictionary
dict = {'a':'2', 'b':'22', 'c':'222', 'd':'3', 'e':'33', 'f':'333', 'g':'4', 'h':'44',
        'i':'444', 'j':'5', 'k':'55', 'l':'555', 'm':'6', 'n':'66', 'o':'666', 'p':'7',
        'q':'77', 'r':'777', 's':'7777', 't':'8', 'u':'88', 'v':'888', 'w':'9', 'x':'99',
        'y':'999', 'z':'9999', ' ':'0'}

case = 1
while (input):
    msg = input.pop(0) #get message
    code = ""
    for char in msg: #encode message
        if code != "":
            if code[-1] == (dict[char][0]): #if from same key, pause
                code += " "
        code += dict[char]
    print "Case #" + str(case) + ": " + code
    case += 1
