while True:
    n = int(input("Enter a positive integer : "))
    if n == 0:
        break
    sum = 0
    for i in range(1, n+1):
        sum += i
        if i < n:
            print(i, end="+")
        else:
            print(i, end="")
    print(" =", sum)