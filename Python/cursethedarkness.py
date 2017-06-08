import sys
import math

#distance helper function
def findDistance(book_x, book_y, candle_x, candle_y):
    #find hypotenuse, pythagorean thm - c^2 = a^2 + b^2
    a = abs(float(book_y) - float(candle_y))
    b = abs(float(book_x) - float(candle_x))
    c = math.sqrt(a*a + b*b)
    return c

input = []
for line in sys.stdin:
    line = line.replace('\n', '')
    input.append(line)

#pop num test cases
num_cases = input.pop(0)

#MAIN
while (input): #while input not empty
    book = input.pop(0).split() #save coordinates of book
    num_candles = int(input.pop(0))
    candles = [] #store all coordinates of candles, store as floats
    for i in range(num_candles):
        candle = input.pop(0).split()
        candles.append(candle)

    #calculate distance between book and each candles, stop if we reach 8 or less
    result = "curse the darkness" #remains as this if no candles found
    while (candles): #while there are still candles
        candle = candles.pop(0)
        if (findDistance(book[0], book[1], candle[0], candle[1])) <= 8.0:
            result = "light a candle"
            break
    print result

            


