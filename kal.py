def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def kali(a, b):
    return a * b

def bagi(a, b):
    if b == 0:
        return "Error! pembagian dengan nol tak diperbolehkan."
    return a / b

while True:
    print("=====================================")
    print("   program kalkulator panz08 ganz"    )
    print("=====================================")
    print("    Pilih operasi matematika nya     ")
    print("        1. Penjumblahan (+)          ")
    print("        2. pengurangan (-)           ")
    print("        3. Perkalian (*)             ")
    print("        4. Pembagian (/)             ")
    print("        5. Keluar                    ")
    print("=====================================")
    
    pilihan = input("masukkan pilihan anda (1/2/3/4/5): ")

    if pilihan == '5':
        print("Terimakasih telah gunain kal ini ")
        break

    if pilihan in ('1', '2', '3', '4'):
        try:
            angka1 = float(input("masukkan angka pertama: "))
            angka2 = float(input("masukkan angka kedua: "))
        except ValueError:
            print("input nya salah! harap masukkan angka yg valid.")
            continue
        
        if pilihan == '1':
            hasil = tambah(angka1, angka2)
            print(f"\nHasil: {angka1} + {angka2} = {hasil}")
        elif pilihan == '2':
            hasil = kurang(angka1, angka2)
            print(f"\nHasil: {angka1} - {angka2} = {hasil}")
        elif pilihan == '3':
            hasil = kali(angka1, angka2)
            print(f"\nHasil: {angka1} * {angka2} = {hasil}")
        elif pilihan == '4':
            hasil = bagi(angka1, angka2)
            print(f"\nHasil: {angka1} / {angka2} = {hasil}")
            
    else:
        print("pilihan tak valid! silahkan pilih menu antara 1 sampai 5.")
