def test(nama):
    print("Nama anda :",nama)

def barang(belanja1,belanja2,belanja3):
    gabungan = belanja1 , belanja2 , belanja3
    return gabungan

def hitung(harga_untuk_b1,harga_untuk_b2,harga_untuk_b3):
    gabungan = harga_untuk_b1 + harga_untuk_b2 + harga_untuk_b3
    return gabungan

batas = int(input("Masukan batas: "))
for i in range (batas):
    nama = input("Masukan nama: ")
    belanja1 = input("Masukan belanja ke 1: ")
    belanja2 = input("Masukan belanja ke 2: ")
    belanja3 = input("Masukan belanja ke 3: ")
    harga_untuk_b1 = int(input('Masukan harga belanja ke pertama: '))
    harga_untuk_b2 = int(input('Masukan harga belanja ke dua: '))
    harga_untuk_b3 = int(input('Masukan harga belanja ke tiga: '))
    data_belanja = barang(belanja1,belanja2,belanja3)
    print("=============== Struk Belanja Anda ===============")
    print(f'Nama Anda {nama} Dan Anda Membeli =',barang(belanja1,belanja2,belanja3))
    print("Untuk harga belanja b1 = ",harga_untuk_b1)
    print("Untuk harga belanja b2 = ",harga_untuk_b2)
    print("Untuk harga belanja b3 = ",harga_untuk_b3)
    print(f'Total Untuk Belanjaan Anda Senilai = ',hitung(harga_untuk_b1,harga_untuk_b2,harga_untuk_b3))
    print("="*50)

