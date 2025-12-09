"""Polimorfisme dinamis di Python adalah kemampuan objek dari kelas berbeda untuk merespons pemanggilan metode yang sama dengan implementasi unik saat program berjalan (runtime), bukan saat kompilasi"""

# class yang diwariskan tidak menggunakan super().__init__ ataupun __init__
# agar bisa di panggil satu satu dan tidak memerlukan parameter

class hewan:                # membuat class bernama hewan 
    def suara (self):       # membuat 3 function variabel bernama suara dan menempatkan syntax self (penamaan) yang nantinya bisa di panggil satu persatu berdasarkan syntax akhir
        print("Hewan mengeluarkan suara:")


class Kucing(hewan):        # class kucing dengan mewariskan clas hewan    
    def suara (self):       # function suara yang di dalam nya ada syntax self yang bisa di panggil 
        print("Kucing mengeluarkan suara meoo") # output didalam syntax tersebut


class Kambing(hewan):       # class kambing yang mewariskan class dari hewan
    def suara (self):       # function suara yang juga didalam nya memiliki syntax penamaan yaitu (self) yang bisa di panggil 
        print("Kambing mengeluarkan suara mbekk") # output dari class


    # membuat suara

# Bagian ini adalah inti dari poliorisme dinamik 
def suara(a):           # membuat function dari variabel suara() menerima dari objek a fungsi a didalam nya adalah dia perlu tau apa yang ada didalam class masing masing diatas tersebut ia hanya memanggil metode suara pada objek tersebut / dengan ada syntax ini maka class yang memiliki function yang sama maka dapat di panggil 
    a.suara()

ts1 = Kucing() # membuat objek dengan variabel ts1 dan memanggil dari class Kucing
suara(ts1) # memanggil ts1 yang sudah memiliki class kucing yang tanpa print


# memanggil class yang sudah di wariskan ke class atas dan sudah di beri penamaan
# bisa menggunakan ini tetapi konsep nya bukan lagi Polimorfisme
# ts1 = kucing()
# ts1.suara()
