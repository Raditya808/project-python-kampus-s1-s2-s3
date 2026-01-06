# 2 
class Akunbang:
    def __init__(self,saldo):
        self.saldo = saldo 
    def get_saldo(self):
        return self.saldo 


    def tambah_saldo(self,jumlah):
        if jumlah > 0:
            self.saldo +=jumlah 
        else:
            print("tidak valid")

    def tarik_saldo(self,jumlah):
        if 0 < jumlah <= self.saldo:
            self.saldo -= jumlah 
        else:
            print("saldo tidak cukup")

akun = Akunbang(10000)
print(akun.get_saldo())
akun.tambah_saldo(5000)
print(akun.get_saldo())
akun.tarik_saldo(2000)
print(akun.get_saldo())
