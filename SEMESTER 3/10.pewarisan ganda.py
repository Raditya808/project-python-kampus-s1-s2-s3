# class pewarisan ganda versi kampus
# memanggil dua class(elektronik,portable)
# membuat dua variabel yang sama di class lalu menggunakan .__init__(self,variabel) menggunakan variabel yang sama tetapi menggunakan koma tidak menggunakan titik
# contoh kode ini hanya menerima satu argumen aja di dalam konstruktor
# ketika membuat class tidak boleh menambah kan variabel yang sama itu akan terjadi konflik serta error 
class elektronik:
    def __init__(self,merk=""):
        self.merk = merk 
    
    def output1(self):
        return f"Produk elektronik ber merek {self.merk}"

class portable:
    def __init__(self,berat):
        self.berat = berat

    def output2(self):
        return f" Produk ini memiliki berat {self.berat}"

class laptop(elektronik,portable): # membuat class laptop dengan memanggil elektronik dan portable
    def __init__(self,merk,berat,series):
        elektronik.__init__(self,merk) # memanggil variabel yang sama menggunakan titik . lalu penamaan menggunakan self 
        portable.__init__(self,berat) # juga sama 
        self.series = series # membuat penamaan series sebagai data baru 

    def output2(self):
        return f"Produk elektronik ini ber merek {self.merk} produk ini memiliki berar {self.berat} series {self.series}" 


# output 
tes1 = laptop(merk="lenovo",berat="200 kg",series="loq")
print(tes1.output2()) # memanggil fungsi dengan print 
