# class hewan 
# menggunakan print
class hewan:
    def __init__(self,nama_hewan="",makan=""):
        self.nama_hewan = nama_hewan 
        self.makan = makan

    def output(self):
        print("="*30)
        print('Macam macam hewan')
        print(self.nama_hewan)
        print(self.makan)
        print("="*30)

class mamalia(hewan):
    def __init__(self, nama_hewan,makan,jenis_bulu):
        super().__init__(nama_hewan, makan)
        self.jenis_bulu = jenis_bulu
    

    def output(self):
        print("="*30)
        print('jenis mamalia')
        print(self.nama_hewan)
        print(self.makan)
        print(self.jenis_bulu)
        print("="*30)

class kucing(mamalia):
    def __init__(self, nama_hewan, makan, jenis_bulu,ras):
        super().__init__(nama_hewan,makan,jenis_bulu)
        self.nama_hewan = nama_hewan
        self.makan = makan
        self.jenis_bulu = jenis_bulu
        self.ras = ras
    

    def output(self):
        print("="*30)
        print('jenis kucing')
        print(self.nama_hewan)
        print(self.makan)
        print(self.jenis_bulu)
        print(self.ras)
        print("="*30)

tes1 = kucing(nama_hewan="Nama kucing adalah moty",makan="moty sedang memakan ikan",jenis_bulu="moty berbulu pendek",ras="moty ras siam")
tes1.output()
