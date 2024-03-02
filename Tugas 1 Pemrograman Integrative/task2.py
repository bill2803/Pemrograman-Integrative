whole_number = int(input("Masukkan Bilangan Bulat : "))
number_divide = 3

result = whole_number/3
result2 = float(result)

if result2.is_integer():
    print(f"The result is : {result2:.1f}")

else:
    print(f"The result is : {result2:.3f}")



