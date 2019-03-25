##Nama : Yussynta Dewi Aprilya Putri
##NIM  : L200170084
##Kelas : C
class Mahasiswa(object):
    """Class Mahasiswa yang dibangun dari class Manusia."""
    def __init__(self, nama, NIM, kota, us):
        """Metode inisiasi ini menutupi metode inisiasi di class Manusia"""
        self.nama = nama
        self.NIM = NIM
        self.kotaTinggal = kota
        self.uangSaku = us
        
c0 = Mahasiswa('Roni',10,'Sukoharjo',240000)
c1 = Mahasiswa('Nauval',51,'Sragen',230000)
c2 = Mahasiswa('Ahmad',2,'Surakarta',250000)
c3 = Mahasiswa('Bintang',18,'Surakarta',235000)
c4 = Mahasiswa('Paw',4,'Boyolali',240000)
c5 = Mahasiswa('Yussy',31,'Salatiga',250000)
c6 = Mahasiswa('Gilang',13,'Klaten',245000)
c7 = Mahasiswa('Janto',5,'Wonogiri',245000)
c8 = Mahasiswa('Janto',23,'Klaten',245000)
c9 = Mahasiswa('Hasan',64,'Karanganyar',270000)
c10 = Mahasiswa('Khalid',29,'Purwodadi',265000)

Daftar = [c0,c1,c2,c3,c4,c5,c6,c7,c8,c9,c10]

def mencari(koleksi,target):
    output = []
    index = 0
    for i in koleksi:
        if i.kotaTinggal == target:
            output.append(index)
            index += 1
        else:
            index += 1
    return output
