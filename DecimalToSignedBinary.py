decimal = input("Decimal: ")
decimal_int = int(decimal)

binary= bin(abs(decimal_int))[2:]

def valid_binary(input):
    # check if input is valid binary number
    if not all(char in '01' for char in input):
        return False
    # check if input is integer (either binary or decimal format)
    try:
        int(input, 2)
        return True
    except ValueError:
        try:
            int(input)
            return True
        except ValueError:
            return False

def decToBin(num):
    return bin(abs(num))[2:]

def twosComp(num):
    foundOne = 0 # boolean
    
    for x in reversed(range(len(num))):
        if binary[x] == 1 and foundOne == 0:
            foundOne = 1
        elif binary[x] == 1 and foundOne == 1:
            binary[x] = 0
        elif binary[x] == 0 and foundOne == 1:
            binary[x] = 1

options = {
    "1": (decToBin, "Decimal to binary"),
    "2": (binToDec, "Binary to decimal"),
    "3": (twosComp, "Two's complement")
}

mode = input("Mode (1: Decimal to binary, 2: Binary to decimal, 3: Two's complement): ")

if decimal_int < 0: # input is negative
    decToBin(abs(decimal_int)) # get positive of input
    twosComp(binary)
else: # input is positive
    decToBin(decimal_int)

print(binary)
