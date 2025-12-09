# Polimorfisme static 
# Polimorfisme static sederhana mencari hasil penjumlahan dan perkalian 
# menggunakan and dan if statement


class matematik:                            # memiliki class bernama matematik
    def operasi (self,a=-1,b=-1,c=-1):      # memiliki function bernama operasi dan memiliki 3 parameter a b dan c yang berisi nilai integer - 1 agar mendapatkan output perkalian di bagian elif
                                            # menggunakan -1 sebagai "tanda rahasia" agar Python tahu bahwa pemanggilan dua angka harus melewati dan menggagalkan blok logika penjumlahan, dan langsung masuk ke blok perkalian. jika di isi menggunakan 0 maka dia akan mengeksekusi bagian if sehingga melanggar konsep if maka penjumlahan yang akan di eksekusi dan bukan perkalian
        if (a >= 0 and b >= 0 and c >= 0): #  if (a>=0 and b >=0 dan c>= 0 ): jika a lebih besar sama dengan 0 dan b lebih besar sama dengan 0 dan c lebih besar sama dengan 0 maka akan mengembalikan nilai return dalam bentuk penjumlahan 

            return a + b + c

        elif (a>= 0 and b>=0):             # elif (a>= 0 and b>=0): jika hanya a dan b saja yang lebih besar sama dengan 0 maka akan mengembalikan nilai return dalam bentuk perkalian
            return a * b 

        else:
            return "masukan angka"         # jika tidak ada angka maka tidak valid 



''' Ketika membuat objek di bawah ini dan memanggil suatu parameter a b atau c  maka itu lah hasil nya perkalian / pertambahan'''

# output objek menggunakan parameter
print("========================")
math = matematik()                        # membuat objek bernama math lalu memanggil class matematik 
print(math.operasi(a=2,b=3))              # membuat output objek dan operasi lalu mengisi dua nilai parameter maka yang berjalan adalah perkalian 
print("========================")




