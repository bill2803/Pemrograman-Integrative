def read_numbers(file_name):
    with open(file_name, 'r') as file:
        numbers = [int(line.strip()) for line in file.readlines()]
    return numbers

def format_number(number):
    return f"{number:,.2f}"

numbers = read_numbers("D:/Materi Kuliah/Pemrograman Integrative/Tugas 3 Pemrograman Integrative/indata.txt")
total = sum(numbers)
print(format_number(total))