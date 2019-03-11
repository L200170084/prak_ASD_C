"""Nama : Yussynta Dewi Aprilya Putri
   NIM  : L200170084
   Kelas: C"""

#nomor1(a)
class Pesan(object):
    """ Class Bernama Pesan Pendeteksi Kalimat"""
    def __init__(self,a):
        self.a = a
    def apakahTerkandung(self,a):
        return a.lower() in self.a.lower()

#nomor1(b)
class Pesan(object):
    """ Metode untuk menghitung jumlah koonsonan """
    def __init__(self,a):
        self.a = a
    def hitungKonsonan(self):
        konsonan = "BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnopqrstvwxyz"
        jumlahkonsonan = ""
        for i in self.a:
            if i in konsonan:
                jumlahkonsonan += i
        return (len(jumlahkonsonan))

#nomor1(c)
class Pesan(object):
    """ Metode untuk menghitung jumlah huruf vokal """
    def __init__(self,a):
        self.a = a
    def hitungVokal(self):
        vokal = "AIUEOaiueo"
        jumlahvokal = ""
        for i in self.a:
            if i in vokal:
                jumlahvokal += i
        return (len(jumlahvokal))

#nomor2
class Manusia(object):
    """class 'Manusia' dengan inisiasi 'nama'"""
    keadaan = "lapar"
    def __init__(self, nama):
        self.nama = nama
    def ucapkanSalam(self):
        print("Salam, namaku ",self.nama)
    def makan(self, s):
        print("Saya baru saja makan ", s)
        self.keadaan = 'kenyang'
    def olahraga(self, k):
        print("Saya baru saja latihan ", k)
        self.keadaan = 'lapar'
    def mengalikanDenganDua(self, n):
        return n * 2

class Mahasiswa(Manusia):
    """Class Mahasiswa yang dibangun dari class Manusia."""
    def __init__(self, nama, NIM, kota, us):
        """Metode inisiasi ini menutupi metode inisiasi di class Manusia"""
        self.nama = nama
        self.NIM = NIM
        self.kotaTinggal = kota
        self.uangSaku = us
    def __str__(self):
        s = self.nama + ', NIM ' + str(self.NIM) \
            + '. Tinggal di ' + self.kotaTinggal \
            + ' tiap bulannya.'
        return s
    def ambilNama(self):
        return self.nama
    def ambilNIM(self):
        return self.NIM
    def ambilUangSaku(self):
        return self.uangSaku
    def makan(self, s):
        """Metode ini menutupi metode 'makan'-nya class manusia.
           Mahasiswa kalau makan sambil belajar."""
        print("Saya baru saja makan", s, "Sambil belajar.")
        self.keadaan = 'kenyang'

    def ambilKotaTinggal(self):
        return self.kotaTinggal
    def perbaruiKotaTinggal(self, ubah):
        self.kotaTinggal = ubah
    def tambahUangSaku(self, tambah):
        self.uangSaku += tambah

#nomor3
print("Silahkan Masukkan Data Mahasiswa Di bawah Ini :")
a = input("Nama Mahasiswa      : ")
b = input("NIM Mahasiswa       : ")
c = input("Asal Mahasiswa      : ")
d = input("Uang Saku Mahasiswa : ")
maha = Mahasiswa(a, b, c, d)
print("""Silahkan Ketik 'maha.instruksi' untuk menjalankan program yang
kalian inginkan.""")

#nomor4
    listKuliah = []
    def ambilKuliah(self, kuliah):
        self.listKuliah.append(kuliah)
        
#Nomor5
    def hapusKuliah(self, hapus):     #metode untuk menghapus sebuah matakuliah dari listKuliah
        self.listKuliah.remove(hapus)


#Nomor6
class SiswaSMA(Manusia):
    def __init__(self, nama, NISN, uangSaku, alamat):
        self.nama = nama
        self.nisn = NISN
        self.uangSaku = uangSaku
        self.alamat = alamat
    def __str__(self):
        a = 'Nama      : ' + str(self.nama) \
            +'NISN      : ' + str(self.nisn) \
            +'Alamat    : ' + str(self.alamat) \
            +'Uang Saku : ' + str(self.uangSaku)
        return a
    
#Nomor7
Class Manusia = Parent Class
Mahasiswa = SubClass dari Manusia
MhsTIF = SuBclass dari Class Mahasiswa, Class (MhsTIF) ini parent classnya(Manusia)
**
    Manusia-> ParentClass (SuperClass)
    Mahasiswa-> SubClass induknya adalah Class (Manusia)
    MhsTIF -> SubClass induknya adalah Class(Mahasiswa)

a.NIM = """ Untuk Membuat Object Yang Akan Menampilkan Nim Mahasiswa yang hanya bisa menampilkan parameter yang ada di def __init__ yang Berada
            di class Mahasiswa """

a.ambilNim = """Untuk Membuat Object Yang Akan Menjalankan methods ambilNim(self) Mahasiswa yang Ada di class Mahasiswa yang akan meminta data dari fungsi
            def __init__ yang berada di class Mahasiswa"""

a.ambilNama = """Untuk Membuat Object Yang Akan Menjalankan methods ambilNama(self) Mahasiswa yang Ada di class Mahasiswa yang akan meminta data dari fungsi
                def __init__ yang berada di class Mahasiswa"""

a.ambilUangSaku = """Untuk Membuat Object Yang Akan Menjalankan methods ambiUangSaku(self) Mahasiswa yang Ada di class Mahasiswa yang akan meminta data dari
                    fungsi def __init__ yang berada di class Mahasiswa"""

a.katakanPy = """Untuk Membuat Object Yang Akan Menjalankan methods katakanPy(self) yang Berada di class MhsTIF """

a.keadaan = """Untuk Membuat Object Yang Akan Menjalankan ClassVariable, dan akan menampilkan sisi dari ClassVariable tersebut, ClassVariable Tersebut Berada
            di dalam Class Manusia"""

a.kotaTinggal = """Untuk Membuat Object Yang Akan Menampilkan kotaTinggal Mahasiswa yang hanya bisa menampilkan parameter yang ada di def __init__ yang Berda
                    di class Mahasiswa"""

a. Makan = """ Untuk Membuat Object Yang Akan Menjalankan methods Makan(self) yang Berada di dalam class Mahasiswa """

a.mengalikanDenganDua = """ Untuk Membuat Object Yang Akan Menjalankan methods mengalikanDenganDua(self) yang Berada di dalam class Manusia, Karena Methods tersebut
                        tidak ada di class Mahasiswa, demikian class MhsTIF bisa mengakses methods tersebut di class Manusia """

a.nama = """ Untuk Membuat Object Yang Akan Menampilkan Nama Mahasiswa yang hanya bisa menampilkan parameter yang ada di def __init__ yang Berada
            di class Mahasiswa """
