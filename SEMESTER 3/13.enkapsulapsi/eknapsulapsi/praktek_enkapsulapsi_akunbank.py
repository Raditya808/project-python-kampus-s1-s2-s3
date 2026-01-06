# Praktek enkapsulapsi versi sendiri
class Akunbank:
    def __init__(self,nominal):
        self.__nominal = nominal
    
    def dapat_saldo(self):
        return self.__nominal
    
    
    def tambah_saldo(self,angka):
        if angka >0 :
            self.__nominal += angka
        
        else:
            print("tidak valid")
            
    def kurang_saldo(self,angka2):
        if 0 <  angka2 <= self.__nominal:
            self.__nominal -= angka2

tes1 = Akunbank(100)
tes1.tambah_saldo(10)
print(tes1.dapat_saldo())
tes1.kurang_saldo(10)
print(tes1.dapat_saldo())
