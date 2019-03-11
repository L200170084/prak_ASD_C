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
class Mahasiswa(object):
    """Class Mahasiswa yang di bangun dari class Manusia"""
    def __init__(self,Nama,Nim,Kota,US):
        self.Nama = Nama
        self.Nim = Nim
        self.KotaTinggal = Kota
        self.UangSaku = US
    def __str__(self):
        s = self.Nama + ', Nim ' + str(self.Nim) + '. Tinggal di ' + self.KotaTinggal + '. Uang Saku Rp ' + str(self.UangSaku) + ' tiap bulannya.'
        return s

    # No2(a)
    def ambilKotaTinggal(self):
        return self.KotaTinggal

    # No2(b)
    def perbaruiKotaTinggal(self, stringBaru):
        self.KotaTinggal = stringBaru

    # No2(c)
    def ambilUangSaku(self):
        return self.UangSaku
    def tambahUangSaku(self, TambahUang):
        return self.UangSaku + TambahUang
#nomor3
class Mahasiswa(object):
    """Class Mahasiswa yang di bangun dari class Manusia"""
    def __init__(self,Nama,Nim,Kota,US):
        self.Nama = Nama
        self.Nim = Nim
        self.KotaTinggal = Kota
        self.UangSaku = US
    def __str__(self):
        s = self.Nama + ', Nim ' + str(self.Nim) + '. Tinggal di ' + self.KotaTinggal + '. Uang Saku Rp ' + str(self.UangSaku) + ' tiap bulannya.'
        return s
    def masukanDataMahasiswaBaru(self):
        DataMHSBaruNama = input("Masukan Nama Anda")
        DataMHSBaruNim = input("Masukan Nim Anda")
        DataMHSBaruKotaTinggal = input("Masukan KotaTinggal Anda")
        DataMHSBaruUangSaku = input("Masukan UangSaku Anda")
        self.Nama = DataMHSBaruNama
        self.Nim = DataMHSBaruNim
        self.KotaTinggal = DataMHSBaruKotaTinggal
        self.UangSaku = DataMHSBaruUangSaku

#nomor4
class Mahasiswa(object):
    """Class Mahasiswa yang di bangun dari class Manusia"""
    listaKuliah = []
    def __init__(self,MK):
        self.MataKuliah = MK
        
    def __str__(self):
        s = 'Mk saya =' + str(self.MataKuliah)
        return s

    def ListKuliah(self):
        s = ['Matematika Diskrit', 'Methods Numerik']
        return s

    def ambilKuliah(self, a):
        Mahasiswa.listaKuliah.append(a) # (Mahasiswa.)Untuk Mengakses VariableClass
        
        
#Nomor5
class Mahasiswa(object):
    """Class Mahasiswa yang di bangun dari class Manusia"""
    listaKuliah = []
    def __init__(self,MK):
        self.MataKuliah = MK
        
    def __str__(self):
        s = 'Mk saya =' + str(self.MataKuliah)
        return s

    def ListKuliah(self):
        s = ['Matematika Diskrit', 'Methods Numerik']
        return s

    def ambilKuliah(self, a):
        Mahasiswa.listaKuliah.append(a) # (Mahasiswa.)Untuk Mengakses VariableClass

    def hapusMK(self, b):
        Mahasiswa.listaKuliah.remove(b)


#Nomor6
class SiswaSMA(Manusia):
    def __init__(self, nama, NISN, uangSaku, alamat):
        self.nama = nama
        self.nisn = NISN
        self.uangSaku = uangSaku
        self.alamat = alamat
    def __str__(self):
        a = 'Nama      : ' + str(self.nama) \
            'NISN      : ' + str(self.nisn) \
            'Alamat    : ' + str(self.alamat) \
            'Uang Saku : ' + str(self.uangSaku)
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
