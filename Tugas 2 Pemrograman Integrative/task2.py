def main():
    total = 0
    
    # Read numbers until -1 is entered
    while True:
        try:
            num = float(input("Enter a number (-1 to stop): "))
            if num == -1:
                break
            total += num
        except ValueError:
            print("Invalid input! Please enter a valid number.")

    # Print the sum with two digits after the decimal point
    print("Sum of all numbers entered: {:.2f}".format(total))

if __name__ == "__main__":
    main()
    
