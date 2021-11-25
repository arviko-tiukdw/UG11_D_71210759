option = input("Masukkan tipe yang anda ingin coba : ")

def penjumlahan():
    print("anda memilih penjumlahan")
def pengurangan():
    print("anda memilih pengurangan")

if option == "penjumlahan":
    print("(benar/salah) jika 19+7==5+15")
    Jawab = input("Masukkan jawaban anda : ")
    if Jawab == "salah":
        print("Jawaban Anda Sudah Benar")
    else:
        print("Jawaban Anda Masih Salah!")
elif option == "pengurangan":
    print("(benar/salah) jika 18-5==9-6")
    Jawab = input("Masukkan jawaban anda : ")
    if Jawab == "salah":
        print("Jawaban Anda Sudah Benar")
    else:
        print("Jawaban Anda Masih Salah!")
elif option == "penjumlahan":
    print("(benar/salah) jika 10+5>7+20")
    Jawaban = input("Masukkan jawaban anda : ")
    if Jawaban == "benar":
        print("Jawaban Anda Masih Salah!")
    else:
        print("Jawaban Anda Sudah Benar")
elif option == "pengurangan":
    print("(benar/salah) jika 11-6>9-6")
    Jawab = input("Masukkan jawaban anda : ")
    if Jawab == "salah":
        print("Jawaban Anda Masih Salah!")
    else:
        print("Jawaban Anda Sudah Benar")
