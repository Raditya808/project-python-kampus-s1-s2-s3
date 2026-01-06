class Mahasiswa:
    def __init__(self,nama):
        self.nama=nama
        self.__nilai=0
    #Getter
    def get_nilai(self):
        return self.__nilai
    #Setter
    def set_nilai(self,nilai):
        if(0<=nilai<=100):
            self.__nilai=nilai
        else:
            print("Nilai Tidak Valid")

    def konversi_nilai(self):
        if(self.__nilai>=80):
            return "A"
        elif(self.__nilai>=75):
            return "B+"
        elif(self.__nilai>=70):
            return "B"
        elif(self.__nilai>=65):
            return "C+"
        elif(self.__nilai>=60):
            return "C"
        elif(self.__nilai>=50):
            return "D"
        else:
            return "E"
    def keterangan_nilai(self):
        if(self.__nilai>=60):
            return "LULUS"
        else:
            return "Tidak Lulus"



#Buat Objek
nm=input("Nama:")
mhs1=Mahasiswa(nm)

#Akses
a=int(input("Masukkan Nilai Angka:"))
mhs1.set_nilai(a)
print("Nama :",mhs1.nama)
print("Nilai Angka:",mhs1.get_nilai())
print("Nilai Huruf:",mhs1.konversi_nilai())
print("Keterangan:",mhs1.keterangan_nilai())

    
    

