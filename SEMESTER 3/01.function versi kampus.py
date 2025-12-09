def nama_mahasiswa(nama,umur=0,tujuan='',ktp=92929292929,tempattinggal=''):
    print('anda:',nama)
    print('umur anda:',umur)
    print('tempat tinggal:',tempattinggal)
    print("ktp: ",ktp)
    print('kenapa suka python:',tujuan)

nama_mahasiswa('radit',umur=18,tempattinggal='talang bakung',tujuan='python menyenangkan')


print("="*50)

# aritmatika


# function aritmatika 
def tes(a,b):
    tambah = a + b
    kali = a * b
    return tambah,kali

a = int(input("masukan angka 1: "))
b = int(input("masukan angka 1: "))

hitungtambah,hitungkali = tes(a,b)
print(hitungtambah)
print(hitungkali)
