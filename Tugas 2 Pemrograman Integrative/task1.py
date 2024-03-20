from datetime import datetime, timedelta
# Membaca input dari pengguna
try:
    days = int(input("Enter number of days: "))
# Mendapatkan tanggal hari ini
    current_date = datetime.now()
# Menambahkan jumlah hari ke tanggal hari ini
    future_date = current_date + timedelta(days=days)
# Formatkan dan cetak tanggal
    formatted_date = future_date.strftime("%A, %B %d, %Y")
    print("The date {} days from now is: {}".format(days, formatted_date))

except ValueError:
    print("Invalid day value! Please enter")


