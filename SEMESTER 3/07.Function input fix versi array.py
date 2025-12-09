data = []


def barang(barang1,barang2,barang3):
    gabungan = barang1,barang2,barang3
    return gabungan

def hitung_belanja(harga_untuk_b1,harga_untuk_b2,harga_untuk_b3):
    hitung = harga_untuk_b1 + harga_untuk_b2 + harga_untuk_b3
    return hitung

batas = int(input('Masukan batas data: '))
for i in range(batas):
    nama = input("Masukan nama: ")
    barang1 = input('Masukan barang belanja ke 1: ')
    barang2 = input('Masukan barang belanja ke 2: ')
    barang3 = input('Masukan barang belanja ke 3: ')
    harga_untuk_b1 = int(input('Masukan harga belanja ke 1: '))
    harga_untuk_b2 = int(input('Masukan harga belanja ke 2: '))
    harga_untuk_b3 = int(input('Masukan harga belanja ke 3: '))

    # menyimpan seluruh data menggunakan data = []
    data.append((nama))



for i in range(batas):
    data_nama = data[i] 

# [0]mengambil indexing pertama di data append maka yang diambil dulu adalah nama jika angka nya 1 dll maka akan mengambil data yang lain / dan tentunya harus menggunakan data[i][0] agar dapat dipanggil
# data[i] berfungsi untuk mengambil/mengakses elemen data yang berada pada posisi indeks 'i' dalam list 'data'.
# dalam python jika suatu append adalah satu karakter maka jika memakai index [0] maka akan menampilkan suatu karakter
# mengatasi itu terjadi cukup menggunakan [i] saja
    data_barang = barang(barang1,barang2,barang3) # pemanggilan function dari barang maka akan dijadikan sebuah list barang tersebut 
    data_harga = hitung_belanja(harga_untuk_b1,harga_untuk_b2,harga_untuk_b3) 
# dan karena khasus nya menggunakan for i in range
    print("========Struuk belanja anda========")
    print(f"data_nama ke {i+1} {data_nama}") # menampilkan angka dari 1 sampai angka kesekian dari datanya
    print(f'data barang {data_barang}')
    print(f'''
                Nama 
              harga untuk barang ke 1 = {barang1} 
              harga untuk barang ke 2 = {barang2}   
              harga untuk barang ke 3 = {barang3}
              total = {data_harga}
    ''')
    print("="*40)
    
    
