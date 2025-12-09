# Polimorfisme statis fix tanpa memanggil parameter variabel a atau b atau c ( hanya angka saja )
class hitung:
    def operasi(self,a=-1,b=-1,c=-1) :
        if a>= 0 and b >=0 and c>= 0:
            return a + b + c 
        elif a>= 0 and b>=0:
            return a * b 
        else:
            print("Masukan angka yang valid")

# pemanggilan menggunakan objek variabel tes1_perkalian dan tes2_perkalian 
print("perkalian")
tes1_perkalian = hitung() # memanggil class hitung
print(tes1_perkalian.operasi(2,3)) # bagian ini perkalian di karenakan dia memanggil 2 parameter a dan b
print("=========")

print("pertambahan")
tes2_perkalian = hitung() # memanggil class hitung
print(tes2_perkalian.operasi(10,10,10)) # bagian ini pertambahan di karenakan dia memanggil 3 parameter a dan b dan c 
print("=========")
