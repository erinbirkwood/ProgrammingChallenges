import sys

input = []
for line in sys.stdin:
    line = line.replace('\n', '')
    input.append(line)

def jumpRoo(kangaroos, num_moves):
    move1 = kangaroos[1] - kangaroos[0] #move 3rd roo
    move2 = kangaroos[2] - kangaroos[1] #move 1st roo
    if move1 == 1 and move2 == 1:
        return num_moves
    else:
        if move1 > move2: #move 3rd roo
            kangaroos = [kangaroos[0], kangaroos[1]-1, kangaroos[1]]
            num_moves += 1
            return jumpRoo(kangaroos, num_moves)
        else: #move 1st roo
            kangaroos = [kangaroos[1], kangaroos[1]+1, kangaroos[2]]
            num_moves += 1
            return jumpRoo(kangaroos, num_moves)

roos = (input.pop(0)).split(' ') #get kangaroo positions
roos = map(int, roos) #change to integer
print jumpRoo(roos, 0)


