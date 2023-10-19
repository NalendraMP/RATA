total = 0
tampung = 0

while True:
    n = input("Masukkan Kategori Nilai: ").upper()
    
    if n == '':
        break
    elif n in ['A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D', 'E']:
        if n == 'A':
            print("Nilai adalah 4.00")
            total += 4
        elif n == 'A-':
            print("Nilai adalah 3.75")
            total += 3.75
        elif n == 'B+':
            print("Nilai adalah 3.50")
            total += 3.50
        elif n == 'B':
            print("Nilai adalah 3.00")
            total += 3.00
        elif n == 'B-':
            print("Nilai adalah 2.75")
            total += 2.75
        elif n == 'C+':
            print("Nilai adalah 2.50")
            total += 2.50
        elif n == 'C':
            print("Nilai adalah 2.00")
            total += 2.00
        elif n == 'C-':
            print("Nilai adalah 1.75")
            total += 1.75
        elif n == 'D':
            print("Nilai adalah 1.50")
            total += 1.50
        elif n == 'E':
            print("Nilai adalah 1.25")
            total += 1.25
        tampung += 1
    else:
        print("Masukkan nilai dengan benar!")

if tampung == 0:
    print("Tidak ada nilai yang dimasukkan.")
else:
    rerata = total / tampung
    print(f"Rata-rata nilai adalah: {rerata:.2f}")