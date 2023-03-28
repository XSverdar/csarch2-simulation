decimal = int(input("Decimal: "))

binary = [0] # initialize list

def decToBin(num):
    if num >= 1: # to not exceed maximum recursion depth
        decToBin(num//2)
        binary.append(num%2)

def twosComp(num):
    foundOne = 0 # boolean
    
    for x in reversed(range(len(num))):
        if binary[x] == 1 and foundOne == 0:
            foundOne = 1
        elif binary[x] == 1 and foundOne == 1:
            binary[x] = 0
        elif binary[x] == 0 and foundOne == 1:
            binary[x] = 1
        
if decimal < 0: # input is negative
    decToBin(abs(decimal)) # get positive of input
    twosComp(binary)
else: # input is positive
    decToBin(decimal)
    
print(binary)
