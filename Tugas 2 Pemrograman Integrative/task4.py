def main():
    grades = []

    # Read grades until -1 is entered
    while True:
        grade = input("Enter a grade (-1 to stop): ")
        if grade == '-1':
            break
        grades.append(int(grade))

    # Calculate average
    if grades:
        average = sum(grades) // len(grades)
    else:
        average = 0

    # Print the average
    print("Average grade:", average)

    # Print grades in the order they were entered
    for grade in grades:
        print(grade)

if __name__ == "__main__":
    main()
