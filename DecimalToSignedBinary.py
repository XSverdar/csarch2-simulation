#current running code w/auds' function. still working on negative binToDec

def decToBin(num):
    return bin(abs(num))[2:]

def binToDec(binary):
    decimal = 0
    power = len(binary) - 1
    for digit in binary:
        if digit == '1':
            decimal += 2 ** power
        power -= 1
    return decimal

def twosComp(num):
    # convert binary string to list of integers
    binary_list = list(map(int, num))
    
    foundOne = False # boolean
    # iterate through binary digits in reverse order
    for x in reversed(range(len(binary_list))):
        if binary_list[x] == 1 and not foundOne:
            foundOne = True
        elif binary_list[x] == 1 and foundOne:
            binary_list[x] = 0
        elif binary_list[x] == 0 and foundOne:
            binary_list[x] = 1
            
    # convert list of integers back to binary string
    return ''.join(map(str, binary_list))

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

options = {
    "1": (decToBin, "Decimal to binary"),
    "2": (binToDec, "Binary to decimal"),
    "3": (twosComp, "Two's complement")
}

def inputs():
    decimal = int(input("Decimal: "))
    if decimal < 0:  # input is negative
        binary = decToBin(abs(decimal))  # get positive of input
        binary = twosComp(binary)
    else:  # input is positive
        binary = decToBin(decimal)
    return binary

mode = input("Mode (1: Decimal to binary, 2: Binary to decimal, 3: Two's complement): ")

if mode == "1":  # decimal to binary
    print(inputs())
elif mode == "2":  # binary to decimal
    binary = input("Binary: ")
    if not valid_binary(binary):
        print("Invalid binary input")
    else:
        decimal = int(binary, 2)
        print(decimal)
elif mode == "3":  # two's complement
    binary = input("Binary: ")
    if not valid_binary(binary):
        print("Invalid binary input")
    else:
        complement = twosComp(binary)
        print(complement)
else:
    print("Invalid mode selected")
