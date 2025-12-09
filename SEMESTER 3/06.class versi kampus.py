# Membuat class versi kampus oleh bapak kevin 

# kata kunci nya class

# dan harus menggunakan __init__ berfungsi mendefinisikan parameter data 
class MOBIL:
    def __init__(self,merek="",tipe="",warna=""):
        self.merek = merek   
        self.tipe = tipe 
        self.warna = warna
        
    def tampilkan(self):
        print("="*50)
        print('Mobil anda = ',self.merek) 
        print('Tipe nya = ',self.tipe)
        print('warna nya = ',self.warna)
        print("="*50) 
        # atau bisa menggunakan return f"Mobil {self.merek} tipe {self.tipe} warna {self.warna}"
        # cuman harus menggunakan print lagi
        
# output membuat variabel yang sama tetapi kita memanggil fungsi yang kedua 
# Tampil_mobil.tampilkan() itu memanggil fungsi def tampilkan()
# maka akan mengeluarkan output
# kita bisa membuat input merk = input("")
# dan memanggil ouput Tampil_mobil = MOBIL(merk) maka akan membuat input 
Tampil_mobil1 = MOBIL(merek="avanza",tipe="2.0",warna="hitam")

# dan juga bisa membuat variabel baru dengan output yang sama 
Tampil_mobil2 = MOBIL(merek="toyota",tipe="3.0",warna="putih")

# memanggil fungsi tidak perlu parameter data karena data nya 
# sudah tertulis di variabel Tampil_mobil = MOBIL
Tampil_mobil1.tampilkan()
Tampil_mobil2.tampilkan()

        


# Contoh sendiri yang kedua
class Laptop:
    def __init__(self,merek="",series="",tipewarna=""):
        self.merek = merek
        self.series = series
        self.tipewarna = tipewarna

    def tampilkan(self):
        print("Laptop")
        print("Merek = ",self.merek)
        print("Series = ",self.series)
        print("Warna = ",self.tipewarna)
        print("=======================")

tampillaptop = Laptop(merek="lenovo",series="loq",tipewarna="hitam")

# untuk memanggil harus menggunakan titik di variabel utama lalu 
# panggil function kedua 
tampillaptop.tampilkan()


# Contoh sendiri yang ketiga parameter data di awal 
class Laptop:
    def __init__(self,nama_laptop="lenovo",tipe="tuf"):
        self.nama_laptop = nama_laptop
        self.tipe = tipe
    
    def output(self):
        print("="*50)
        print(self.nama_laptop)
        print(self.tipe)
        print("="*50)
tampil = Laptop()
tampil.output()
