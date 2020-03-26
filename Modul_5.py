class MhsTIF(object):
    def __init__(self, nama, NIM, alamat,us):
        self.nama = nama
        self.NIM = NIM
        self.alamat = alamat
        self.us = us

    def __str__(self):
        s = self.nama + "NIM" + str(self.NIM)\
            + ". Tinggal di " + self.alamat\
            + ". Uang Saku Rp. " + str(self.us)\
            + " Tiap Bulannya."
        
def swap(A,p,q):
    tmp = A[p]
    A[p] = A[q]
    A[q] = tmp
    
#Nomor1    
Daftar = [MhsTIF('Amron', "L200180105", 'Surakarta', 900000),
          MhsTIF('Rayhan', "L200180100", 'Karanganyar', 1000000),
          MhsTIF('Dika', "L200180097", 'Bekasi', 800000),
          MhsTIF('Irul', "L200180101", 'Riau', 300000),
          MhsTIF('Beny', "L200180079", 'Karanganyar', 1200000),
          MhsTIF('Akbar', "L200180078", 'Madiun', 1130000),
          MhsTIF('Taufiq', "L200180069", 'Pacitan', 750000),
          MhsTIF('Annisa', "L200180066", 'Surakarta', 830000),
          MhsTIF('Aprinta', "L200180088", 'Sragen', 780000),
          MhsTIF('Sindhi', "L200180084", 'Klaten', 650000)]

def cekNIM(object):
    for i in object:
        print (i.NIM)
         
          
def urutNIM(object):
    n = len(object)
    for i in range(n-1):
        for j in range(n-i-1):
            if object[j].NIM > object[j+1].NIM:
                swap(object,j,j+1)

#Nomer2
                
def combine(A, B):
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
    while j < lb:
        c.append(B[j])
        j += 1
    return c

#Nomor3  
def swap(A,p,q):
    tmp = A[p]
    A[p] = A[q]
    A[q] = tmp

def cariPosisiYangTerkecil(A, dariSini, sampaiSini):
    posisiTerkecil = dariSini
    for i in range(dariSini+1, sampaiSini):
        if A[1] < A[posisiTerkecil]:
            posisiTerkecil = 1
    return posisiTerkecil

def bubbleSort(A):
    n = len(A)
    for i in range(n-1):
        for j in range(n-i-1):
            if A[j] > A[j+1]:
                swap(A,j,j+1)

def selectionSort(A):
    n = len(A)
    for i in range(n-1):
        indexKecil = cariPosisiYangTerkecil(A, i, n)
        if indexKecil != i:
            swap(A, i, indexKecil)

def insertionSort(A):
    n = len(A)
    for i in range(1,n):
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

aw = detak();bubbleSort(u_bub);ak=detak();print("Bubble    : %g detik"%(ak-aw));
aw = detak();selectionSort(u_sel);ak=detak();print("Selection : %g detik"%(ak-aw));
aw = detak();insertionSort(u_ins);ak=detak();print("Insertion : %g detik"%(ak-aw));
