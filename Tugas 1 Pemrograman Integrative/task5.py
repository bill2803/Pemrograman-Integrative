sum = 0
while True:
    numberstring = input("Please enter a number: ")
    if numberstring == "-1":
        break
    number = float(numberstring)
    sum = sum + number
print("The sum of the numbers entered is: ", sum)