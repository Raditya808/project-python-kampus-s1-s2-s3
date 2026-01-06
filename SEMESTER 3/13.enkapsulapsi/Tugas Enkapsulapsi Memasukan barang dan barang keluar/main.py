class Barang:
    def __init__(self,barang):
        self.__barang = barang
    
    def dapat_barang(self):
        print(f"Total Barang Gudang = {self.__barang}")
    

    # bagian barang masuk
    def barang_masuk(self,b1):
        if b1 > 0:
            self.__barang += b1
        else:
            print("gagal")
    def barang_masuk_output(self):
        print(f"Total Barang Masuk = {self.__barang}")

    # bagian barang keluar 
    def barang_keluar(self,b2):
        if b2 > 0:
            self.__barang -= b2
        else:
            print("gagal")
    def barang_keluar_output(self):
        print(f"Total Barang Keluar = {self.__barang}")

print("=======Hasil Barang Masuk / Keluar=======")
# total barang gudang sebesar 100 barang
barang_gudang = Barang(100)
barang_gudang.dapat_barang()

# barang masuk sebesar 10 barang 
barang_gudang.barang_masuk(10)
barang_gudang.barang_masuk_output()

# barang keluar sebesar 40 barang 
barang_gudang.barang_keluar(40)
barang_gudang.barang_keluar_output()
print("="*40)
