# poliorisme dinamic
class lingkaran:
    def luas(self,radius):
        return 3.14 * radius * radius 

class Persegi:
    def luas (self,sisi) :
        return sisi * sisi



def hitung_luas(bangun,ukuran):
    print(f"luas: {bangun.luas(ukuran)}")


lingkaran = lingkaran()
persegi = Persegi()
    
    
hitung_luas(lingkaran,ukuran=10)
hitung_luas(persegi,ukuran=4)
