# macam macam alat bangunan 
class macam_mcam_barang_bangunan:
    def __init__(self,nama_barang=""):
        self.nama_barang = nama_barang

    def output1(self):
        print("=========================")
        print("TIPE BARANG")
        print(self.nama_barang)
        print("=========================")

class bagian_pearairan(macam_mcam_barang_bangunan):
    def __init__(self,nama_barang,barang_ke1_bagianperairan,barang_ke2_bagianperairan,barang_ke3_bagianperairan):
        super().__init__(nama_barang)
        self.barang_ke1_bagianperairan = barang_ke1_bagianperairan
        self.barang_ke2_bagianperairan = barang_ke2_bagianperairan
        self.barang_ke3_bagianperairan = barang_ke3_bagianperairan

    def output(self):
        print("=========================")
        print("DATA BAGIAN ALAT PERAIRAN")
        print(self.nama_barang)
        print(self.barang_ke1_bagianperairan)
        print(self.barang_ke2_bagianperairan)
        print(self.barang_ke3_bagianperairan)
        print("=========================")

class bagian_pewarna(macam_mcam_barang_bangunan):
    def __init__(self, nama_barang,bagian_pewarna1,bagian_pewarna2,bagian_pewarna3):
        super().__init__(nama_barang)
        self.bagian_pewarana1 = bagian_pewarna1
        self.bagian_pewarana2 = bagian_pewarna2 
        self.bagian_pewarana3 = bagian_pewarna3
    def output(self):
        print("=========================")
        print("DATA BAGIAN ALAT PEWARNA")
        print(self.nama_barang)
        print(self.bagian_pewarana1) 
        print(self.bagian_pewarana2)
        print(self.bagian_pewarana3)
        print("=========================")


class bagian_kelistrikan(macam_mcam_barang_bangunan):
    def __init__(self,nama_barang,barang_ke1_bagiankelistrikan,barang_ke2_bagiankelistrikan,barang_ke3_bagiankelistrikan):
        super().__init__(nama_barang)
        self.nama_barang
        self.barang_ke1_bagiankelistrikan = barang_ke1_bagiankelistrikan
        self.barang_ke2_bagiankelistrikan = barang_ke2_bagiankelistrikan
        self.barang_ke3_bagiankelistrikan = barang_ke3_bagiankelistrikan

    def output(self):
        print("=========================")
        print("DATA BAGIAN KELISTRIKAN")
        print(self.nama_barang)
        print(self.barang_ke1_bagiankelistrikan)
        print(self.barang_ke2_bagiankelistrikan)
        print(self.barang_ke3_bagiankelistrikan)
        print("=========================")
# Ouput ======================================================
tes1 = macam_mcam_barang_bangunan(nama_barang="bangunan")
tes1.output1()


tes2 = bagian_pearairan(nama_barang="Bagian Perairan",barang_ke1_bagianperairan="pipa",barang_ke2_bagianperairan="wastafel",barang_ke3_bagianperairan="lem pipa")
tes2.output()


tes3 = bagian_pewarna(nama_barang="Bagian Pewarna",bagian_pewarna1="cat",bagian_pewarna2="kuas",bagian_pewarna3="tinner")
tes3.output()


tes4 = bagian_kelistrikan(nama_barang="Bagian Kelistrikan",barang_ke1_bagiankelistrikan="kabel",barang_ke2_bagiankelistrikan="lampu",barang_ke3_bagiankelistrikan="seklar")
tes4.output()

