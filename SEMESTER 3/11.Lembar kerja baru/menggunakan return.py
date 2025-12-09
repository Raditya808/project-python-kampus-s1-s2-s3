class hewan:
    def __init__(self,nama_hewan=""):
        self.nama_hewan = nama_hewan

    def output(self):
        return f"Nama hewan {self.nama_hewan}"

class mamalia(hewan):
    def __init__(self, nama_hewan,makan,jenis_bulu):
        super().__init__(nama_hewan)
        self.nama_hewan = nama_hewan
        self.makan = makan
        self.jenis_bulu = jenis_bulu

    def output(self):
        return f"Nama hewan {self.nama_hewan} dia suka makan {self.makan} jenis bulu nya {self.jenis_bulu}"

class kucing(hewan):
    def __init__(self,nama_hewan,makan,jenis_bulu,ras):
        super().__init__(nama_hewan)
        self.nama_hewan = nama_hewan
        self.makan = makan 
        self.jenis_bulu = jenis_bulu
        self.ras = ras
    
    def output(self):
        return f"Nama hewan {self.nama_hewan} dia suka makan {self.makan} jenis bulu nya {self.jenis_bulu} ras nya keturunan {self.ras}"


tes1 = mamalia(nama_hewan="kucing",makan="ikan",jenis_bulu="pendek")
print(tes1.output())

# pemanggilan juga bisa di lakukan langsung tanpa parameter
tes2 = kucing("katty","ikan","halus","niga")
print(tes2.output())

