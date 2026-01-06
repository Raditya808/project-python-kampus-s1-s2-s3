class AkunBank:
    def __init__(self, saldo):
        self.__saldo = saldo  # disini adalah atribut private (encapsulation)

    # getter untuk mendapatkan saldo 
    def get_saldo(self):
        return self.__saldo
    
    # setter untuk menambahkan saldo dengan validasi 
    def tambah_saldo(self, jumlah):
        if jumlah > 0:
            self.__saldo += jumlah
        else:
            print("Jumlah tidak valid")

    # setter untuk menarik saldo dengan validasi  
    def tarik_saldo(self, jumlah): 
        if 0 < jumlah <= self.__saldo:
            self.__saldo -= jumlah 
        else:
            print("Saldo tidak cukup atau jumlah tidak valid")

akun = AkunBank(10000)
print(akun.get_saldo())
akun.tambah_saldo(5000)
print(akun.get_saldo())