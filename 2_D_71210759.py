print(" Penyisipan Kata/Kalimat")
f = input("Masukkan Sebuah Kata/Kalimat : ")
g = input("Masukkan Karakter yang ingin disisipkan : ")

def sisipHuruf():
    x = g.join(f)
    print(x)

def sisipKata():
    i = g.join(f)
    h = list(i)
    print(h)


sisipHuruf()
sisipKata()

