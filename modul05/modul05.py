"""Nama : Yussynta Dewi Aprilya Putri
   NIM  : L200170084
   Kelas: C"""

#no1
class MhsTIF(object):
    def __init__(self, nama, nim, asal, us):
        self.nama = nama
        self.nim = nim
        self.asal = asal
        self.uangsaku = us

    def __str__(self):
        s = self.nama + 'NIM' + str(self.nim)\
            + ' Tinggal di ' + self.asal \
            + ' Uang Saku Rp ' + str(self.uangsaku)\
            + ' tiap harinya.'

def swap(A,p,q):
    temp = A[p]
    A[p] = A[q]
    A[q] = temp
  
daftar = [(MhsTIF('bayu','L200170052','sragen',10000)),
          (MhsTIF('kori','L200170053','merauke',2000)),
          (MhsTIF('gentur','L200170085','sukoharjo',15000)),
          (MhsTIF('vicky','L200170065','sragen',22000)),
          (MhsTIF('anom','L200170071','weru',23000)),
          (MhsTIF('majid','L200170063','klaten',25000)),
          (MhsTIF('fachrul','L200170042','indramayu',25000)),
          (MhsTIF('rima','L200170039','brebes',19000)),
          (MhsTIF('susi','L200170047','bojonegoro',18000)),
          (MhsTIF('naufal','L200170079','bogor',21000))]

def ceknim(object):
    for i in object:
        print(i.nim)

def nimurut(object):
    n = len(object)
    for i in range(n-1):
        for j in range(n-i-1):
            if object[j].nim > object[j+1].nim:
                swap(object,j,j+1)

#no2
pertama = [1,4,6,7,10,12]
kedua = [2,3,5,8,11]

def gabung(A,B):
    la = len(A)
    lb = len(B)
    c = list()
    i = 0
    j = 0
    while i < la and j < lb:
        if A[i] < B[j]:
            c.append(A[i])
            i += 1
        else:
            c.append(B[j])
            j += 1
    while i < la:
        c.append(A[i])
        i += 1
    while j > lb:
        c.append(B[j])
        j += 1
    return c

print("list pertama",pertama)
print("list kedua",kedua)
print("\nkedua list digabung menjadi ...\n")

print(gabung(pertama, kedua))

#no3
def swap(A,p,q):
    temp = A[p]
    A[p] = A[q]
    A[q] = temp
    
def cariposisiterkecil(A, darisini, sampaisini):
    posisiterkecil = darisini
    for i in range(darisini+1, sampaisini):
        if A[1] < A[posisiterkecil]:
            posisiterkecil = 1
    return posisiterkecil

def bubblesort(A):
    n = len(A)
    for i in range(n-1):
        for j in range(n-i-1):
            if A[j] > A[j+1]:
                swap(A,j,j+1)
                
def selectionsort(A):
    n = len(A)
    for i in range (n-1):
        indexkecil = cariposisiterkecil(A,i,n)
        if indexkecil != i:
            swap(A,i,indexkecil)

def insertionsort(A):
    n = len(A)
    for i in range (1,n):
        nilai = A[i]
        pos = i
        while pos > 0 and nilai < A[pos-1]:
            A[pos] = A[pos-1]
            pos = pos-1
        A[pos] = nilai
        
from time import time as detak
from random import shuffle as kocok

k = [i for i in range(1,6001)]
kocok(k)
u_bub = k[:]
u_sel = k[:]
u_ins = k[:]

aw = detak();bubblesort(u_bub);ak=detak();print('Buble      : %g detik' %(ak-aw));
aw = detak();selectionsort(u_sel);ak=detak();print('Selection  : %g detik' %(ak-aw));
aw = detak();insertionsort(u_ins);ak=detak();print('Insertion  : %g detik' %(ak-aw));

