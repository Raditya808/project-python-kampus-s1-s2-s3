# class Polimorfisme dasar dalam hewan
class hewan:
    def suara(self):
        print(f"Suara hewan berbunyi")

class kucing(hewan):
    def suara(self):
        print("kucing berbunyi meow")

class anjing(hewan):
    def suara(self):
        print("suara annjing berbunyi guk guk guk")

def suara(a):
    a.suara()
kcing = kucing()
suara(kcing)


########################################################################
# Jikalau menggunakan nilai return untuk memanggil 

# class hewan:
    #def suara(self):
        #return f"suara hewan berbunyi"
    
#class kucing(hewan):
    #def suara(self):
        #return f"kucing berbunyi meow"

#class anjing(hewan):
    #def suara(self):
        #return f"anjing berbunyi guk guk guk"
        
#def suara(a):
    #return a.suara()
    
#ts1 = kucing()
#print(suara(ts1))
