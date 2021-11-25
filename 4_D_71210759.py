print ("tabakangka")

memulai = int (input("Untuk memulai program masukkan (-1) untuk mulai : "))

if memulai == -1:
    print("Apakah 4 ?")
    print("Apakah tebakan anda sudah benar ?")
    print("Lebih kecil (0)")
    print("Lebih besar (1)")
    print("Benar(2)")
    Jawab = int (input(":"))
    if Jawab == 1:
        print("Apakah 6 ?")
        print("Apakah tebakan anda sudah benar ?")
        print("Lebih kecil (0)")
        print("Lebih besar (1)")
        print("Benar(2)")
    Jawaban = int (input(":"))
    if Jawaban == 1:
        print("Hasil penjumlahannya pasti 7 !")
        print("Jumlah tebakkan : 3")
        print("Program Selesai !")
    elif Jawab == 0:
        print("Apakah 2 ?")
        print("Apakah tebakan anda sudah benar ?")
        print("Lebih kecil (0)")
        print("Lebih besar (1)")
        print("Benar(2)")
    Jawaban = int (input(":"))
    if Jawaban == 1:
        print("Hasil penjumlahannya pasti 3 !")
        print("Jumlah tebakkan : 3")
        print("Program Selesai !")
else:
    ("Program tidak berhasil dijalankan")


