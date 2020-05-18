##menjumlahkan bilangan 1 sampai n
import time
##jml cara 1
def jumlahkan_cara_1(n):
    hasilnya=0
    for i in range (1,n+1):
        hasilnya+=i
    return hasilnya
##jml cara 2
def jumlahkan_cara_2(n):
    return (n*(n+1))/2

print("cara ke 2",jumlahkan_cara_2(1000000))
for i in range(5):
    awal = time.time()
    h = jumlahkan_cara_2(1000000)
    akhir = time.time()
    print("jumlah adalah %d,memerlukan waktu %9.8f detik" % (h,akhir-awal))

##kasus terburuk,rata-rata dan terbaik
    import time
import random

def insertionsort(a):
    for i in range(1,len(a)):
        nilai = a[i]
        b = i
        while b >0 and nilai<a[b - 1]:
            a[b]=a[b-1]
            b -=1
        a[b]=nilai

print("===============================Average Case====================")    
##average case
for i in range (5):
    L = list(range(3000))
    random.shuffle(L)
    awal = time.time()
    U = insertionsort(L)
    akhir = time.time()
    print("mengurutkan %d bilangan,memerlukan waktu %8.7f detik" % (len(L),akhir-awal))
##worst case
print("===============================Worst Case====================") 
for i in range (5):
    L = list(range(3000))
    L = L[::-1]
    awal = time.time()
    U = insertionsort(L)
    akhir = time.time()
    print("mengurutkan %d bilangan,memerlukan waktu %8.7f detik" % (len(L),akhir-awal))
##best case
print("===============================Best Case====================") 
for i in range (5):
    L = list(range(3000))
    awal = time.time()
    U = insertionsort(L)
    akhir = time.time()
    print("mengurutkan %d bilangan,memerlukan waktu %8.7f detik" % (len(L),akhir-awal))

##analisi pewaktuan menggunakan timeit
from timeit import timeit
timeit('sqrt(2)','from math import sqrt',number = 10000)

timeit("1+2")

timeit("sin (pi/3)", setup = "from math import sin,pi")

timeit("sin (1.047)", setup = "from math import sin")

## melihat O(n2) pada nested loop
import timeit
import matplotlib.pyplot as plt

def kalangBersusuh(n):
    for i in range(n):
        for j in range (n):
            i+j

def ujiKalangBersusuh(n):
    ls=[]
    jangkauan=range(1,n+1)
    siap = "from __main__ import kalangBersusuh"
    for i in jangkauan:
        ##print('i = ',i)
        t=timeit.timeit("kalangBersusuh(" +str(i) +")",setup=siap,number=1)
        ls.append(t)
    return ls

n=1000
LS=ujiKalangBersusuh(n)

plt.plot(LS)
skala=7700000
plt.plot([x*x/skala for x in range (1,n+1)])
plt.show()
