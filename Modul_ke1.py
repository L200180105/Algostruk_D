from math import sqrt as sq
from random import randint

#No 1
def cetakSiku2(x):
    for i in range (0, x):
        i+=1
        print ("*" * i)


#No 2
def PersegiEmpat(x, y):
    print ('@'*y)
    for i in range(x-2):
        print ('@'+' '*(y-2)+'@')
    print ('@'*y)


#No 3 a
def jumlahHurufVokal(x):
    vokal = "AIUEOaiueo"
    a = len(x)
    b = 0
    for k in x:
        if k in vokal:
            b+=k
    c = len(b)
    return (a,c)


#No 3 b
def jumlahHurufKonsonan(x):
    vokal = "AIUEOaiueo"
    a = len(x)
    b = 0
    for k in x:
        if k not in vokal:
            b+=k
    c = len(b)
    return (a,c)


#No 4
def rerata(b):
    k = 0
    for i in (b):
        k+=i
    hasil = k / len(b)
    return hasil


#No 5
def apakahPrima(x):
    x = int(x)
    primaKecil = [2,3,5,7,11]
    bknPrimaKecil = [0,1,4,6,8,9,10]
    if x in primaKecil:
        return True
    elif x in bknPrimaKecil:
        return False
    else:
        for i in range(2, int(sq(x))+1):
            if x % i == 0:
                return False
            else:
                return True


#No 6
def apaPrima():
    lower = 2 
    upper = 1000
    print("Bilangan prima antara",lower,"and",upper,":")
    for num in range(lower,upper + 1): 
        if num > 1: 
            for i in range(2,num): 
                if (num % i) == 0: 
                    break 
            else: 
                print(num)


#No 7
def faktorprima(x):
    faktor=[]
    loop=2
    while loop<=x:
        if x%loop==0:
            x/=loop
            faktor.append(loop)
        else:
            loop+=1
    return faktor

         
#No 8
def apakahTerkandung(x, y):
    for k in x:
        if k in y:
            return True
        else:
            return False


#No 9
def rubah35():
    a = 1
    b = 100
    for i in range (a, b+1):
        if (i % 3) == 0 and (i % 5) == 0:
            print ("Python UMS")
        elif (i % 3) == 0:
            print ("Python")
        elif (i % 5) == 0:
            print ("UMS")
        else:
            print (i)

           
#No 10
def selesaikanABC(a, b, c):
    a=float(a)
    b=float(b)
    c=float(c)
    D=(b**2) - (4*a*c)
    if D<0:
        return "Determinannya negatif. Persamaan tidak mempunyai akar real"
    else:
        x1=(-b + sq(D))/2*a
        x2=(-b - sq(D))/2*a
        hasil=(x1, x2)
        return hasil


#No 11
def apakahKabisat(x):
    if (x % 4) == 0 and (x % 100) == 0 and (x % 400) != 0:
        return False
    elif (x % 4) == 0:
        return True
    else:
        return False


#No 12
print("""Permainan tebak angka.
Saya menyimpan sebuah angka bulat antara 1 sampai 100. Coba Tebak!""")
a = randint(1, 100)
for i in range (3):
    b = int(input("Masukkan tebakkan ke-{}:>".format(i+1)))
    if b == a:
        print ("Ya. Anda benar.")
    elif b > a:
        if i >= 2:
            print ("Itu terlalu besar. Kesempatan habis. Nilainya adalah",a)
        else: 
            print ("Itu terlalu besar. Coba lagi")
    else:
        if i >= 2:
            print ("Itu terlalu kecil. Kesempatan habis. Nilainya adalah",a)
        else: 
            print ("Itu terlalu kecil. Coba lagi")


#No 13
def katakan(angka):
    satuan = ["satu", "dua", "tiga", "empat", "lima",
              "enam", "tujuh", "delapan", "sembilan", "sepuluh",
              "sebelas", "dua belas", "tiga belas", "empat belas", "lima belas",
              "enam belas", "tujuh belas", "delapan belas", "sembilan belas"
              ]
    angka = '{:0,.0f}'.format(int(angka))
    angka = angka.split(",")
    katakan = []
    idx = 1
    for x in angka[::-1]:
        seribu = False
        if idx == 2 and x[-1]!="0":
            if int(x)< 2 :
                katakan.append("seribu")
                seribu = True
            else:
                katakan.append("ribu")
        if idx == 3 and x[-1]!="0":
            katakan.append("juta")
        if seribu == False:
            if int(x[-2:])<20 and int(x[-2:])>0:
                katakan.append(satuan[int(x[-2:])-1])
            elif int(x[-2:])>0:
                if int(x[-1])!=0:
                    katakan.append(satuan[int(x[-1])-1])
                if int(x[-2]) != 0:
                    katakan.append(satuan[int(x[-2])-1]+" puluh")
        if int(x[0]) > 2 and len(x)==3 :
            katakan.append(satuan[int(x[0])-1]+" ratus")
        elif len(x)==3 and int(x[0])!=0 :
            katakan.append("seratus")
        idx+=1
    return " ".join(katakan[::-1])


#No 14
def formatRupiah(n):
    x = '{:,}'.format(n).replace(',', '.')
    return "Rp " + x
