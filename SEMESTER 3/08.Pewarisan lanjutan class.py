# tugas mandiri tanpa melihat dan kode class part 2 (pewarisan)
# menggunakan nilai return

class kendaraan: # class bernama mobil
    def __init__(self,merk="",model=""): # lalu memiliki function dengan __init__ ini adalah konstruktor kelas fungsi nya adalah menginisialisasi (memberi nilai awal) dari atribut merk dan model ketika turunan sebuah objek kendaraan (atau objek kelas lainnya dibuat) 
        self.merk = merk # self.merk dan model adalah objek tersebut
        self.model = model 

    def output(self): # menampilkan output dengan self menggunakan print dan objek dari merk dan model tadi dipanggil menggunakan syntax self
        print("============")
        print("data motro")
        print(self.merk) 
        print(self.model)
        print("============")


class mobil(kendaraan):     # class mobil dengan memanggil class kendaraan diatas
    def __init__(self, merk,model,kapasitas):   # turunan dari kendaraan dan memiliki function dari variabel baru bernama mobil dan di isi dengan kapasitas
        super().__init__(merk, model) # super().__init__ memanggil merk dan model lalu 
        self.kapasitas = kapasitas # memanggil kapasitas menggunakan self 

    def deskripsi(self):
        return f"mobil {self.merk} {self.model} dengan kapasitas {self.kapasitas}" # output

class motor(kendaraan): # turunan baru bernama class motor dan memanggil kendaraan
    def __init__(self, merk,model,cc): # lalu terdapat self dengan tambahan cc 
        super().__init__(merk,model) # panggilan untuk merk dan model di class kendaraan
        self.cc = cc # memanggil cc 

    def deskripsi(self):
        return f"motor {self.merk} dengan model {self.model} dengan cc {self.cc}" # memanggil merk , model ,cc menggunakan self dengan syntax return dan format str f""

output1 = mobil(merk="avanza",model="avanza",kapasitas=7) # output dari class mobil 
output_motor2 = motor(merk="revo",model="2012",cc="120cc") # output dari class motor
print("=====================================================")
print(output1.deskripsi())
print("=====================================================")
print(output_motor2.deskripsi())
print("=====================================================")

print("===============================================================================")


# class pewarisan versi sendiri menggunakan print
class kendaraan:
    def __init__(self,nama="",tipe=""):
        self.nama = nama 
        self.tipe = tipe

    def output(self):
        print(self.nama)
        print(self.tipe)
        


class Mobil(kendaraan):
    def __init__(self,nama,tipe,warna):
        super().__init__(nama,tipe)
        self.warna = warna 
     
    def output(self):
        print(self.nama)
        print(self.tipe)
        print(self.warna)
    

print("=======================================")
test1 = kendaraan(nama="motor",tipe="honda")
test1.output()
print("=======================================")
test2 = Mobil(nama="mobil",tipe="avanza",warna="hitam")
test2.output()






# PR tentukan objek nya apa class umum nya apa yang lebih kecil lagi menggunakan metode print 
