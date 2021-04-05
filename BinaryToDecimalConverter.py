def bin2Dec():
    b = [0] * (8)
    
    newNum = ""
    num = 128
    dec = 0
    print("Enter in a binary number: ")
    binaryNum = input()
    while len(binaryNum) != 8:
        print("Invalid input! Please enter a binary number 8 bits(digits) long: ")
        binaryNum = input()
    for i in range(0, len(binaryNum) - 1 + 1, 1):
        index = binaryNum[i]
        codeNum = ord(index)
        while codeNum < 48 or codeNum > 49:
            print("Invalid input for index " + str(i) + "! Please enter a new value, 0 or 1, to take its place: ")
            newNum = input()
            codeNum = ord(newNum)
        charNum = chr(codeNum)
        intNum = int(charNum)
        b[i] = intNum
        if intNum == 1:
            dec = num + dec
            num = float(num) / 2
        else:
            num = float(num) / 2
        if i == 7:
            print(str(b[i - 7]) + str(b[i - 6]) + str(b[i - 5]) + str(b[i - 4]) + str(b[i - 3]) + str(b[i - 2]) + str(b[i - 1]) + str(b[i - 0]), end='', flush=True)
    print(" converts to " + str(dec) + " in decimal.")

def dec2Bin():
    num = 128
    dec = 0
    print("Enter in a number between 0 and 255: ")
    decNum = int(input())
    while decNum < 0 or decNum > 255:
        print("Invalid input! Please enter a number between 0 and 255: ")
        decNum = int(input())
    print(str(decNum) + " converted to binary is ", end='', flush=True)
    for i in range(0, 7 + 1, 1):
        if decNum >= num:
            decNum = decNum - num
            num = float(num) / 2
            print("1", end='', flush=True)
        else:
            num = float(num) / 2
            print("0", end='', flush=True)
    print("")

# Main
print("Welcome to Binary Number! I will convert any 8 bit binary number of your choosing into decimal format!")
while True:    #This simulates a Do Loop
    print("Which would you like to do?")
    print("1. Decimal to binary")
    print("2. Binary to decimal")
    print("3. End the program")
    choice = int(input())
    if choice == 1:
        dec2Bin()
    else:
        if choice == 2:
            bin2Dec()
    if not(choice != 3): break   #Exit loop
print("You have chosen to end the program. Goodbye!")
