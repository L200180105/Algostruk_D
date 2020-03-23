class MhsTIF():
    """ class mahsiswa yang dibangun dai class manusia """
    def __init__(self,nama,NIM,kota,us):
        self.nama = nama
        self.NIM = NIM
        self.kota = kota
        self.uang = us

c0 = MhsTIF('Ika', 10, 'Sukoharjo', 240000)
c1 = MhsTIF('Budi', 51, 'Sragen', 230000)
c2 = MhsTIF('Ahmad', 2, 'Sukoharjo', 250000)
c3 = MhsTIF('Chandra', 18, 'Sukoharjo', 23000)
c4 = MhsTIF('Eka', 4, 'Boyolali', 240000)
c5 = MhsTIF('Fandi', 31, 'Salatiga', 230000)
c6 = MhsTIF('Deni', 13, 'Klaten', 245000)
c7 = MhsTIF('Galuh', 5, 'Wonogiri', 245000)
c8 = MhsTIF('Janto', 23, 'Klaten', 245000)
c9 = MhsTIF('Hasan', 64, 'Karanganyar', 270000)
c10 = MhsTIF('Khalid', 29, 'Purwodadi', 265000)

Daftar = [c0, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10]
##Nomor 1
def cariKota(list, target):
    a = []
    for i in list:
        if i.kota == target:
            a.append(list.index(i))
    return a

x = cariKota(Daftar, 'Sukoharjo')
y = cariKota(Daftar, 'Klaten')
z = cariKota(Daftar, 'Pangkalan Bun')
print(x)
print(y)
print(z)

##Nomor 2
def cariUangSakuTerkecil(list):
    nama = []
    terkecil = list[0].uang
    for i in list[1:]:
        if i.uang < terkecil:
            terkecil = i.uang
            nama = i.Nama
    return nama, terkecil
print("Uang terkecil dimiliki oleh", cariUangSakuTerkecil(Daftar))

##Nomor 3
def cariUangSakuTerkecilObject(list):
    terkecil = [list[0]]
    for i in list[1:]:
        if i.uang < terkecil[0].uang:
            terkecil.append(i.Nama)
    return terkecil
print("Uang terkecil dimiliki oleh", cariUangSakuTerkecilObject(Daftar))

##Nomor 4
def cariUangSakuKurang250(Daftar):
    kurang = []
    for i in Daftar:
        if i.uang<250000:
            kurang.append(i)
    return kurang

a = cariUangSakuKurang250(Daftar)
for i in a:
    print(i.nama)

##Nomor 5
class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = None

    def cari(self, x):
        current = self
        while current != None:
            if current.next != None:
                if current.data != x:
                    current = current.next
                else:
                    print("Data", x, "ada dalam linked list")
                    break
            elif current.next == None:
                print("Data", x, "tidak ada dalam linked list")
                break
a = Node(12)
menu = a
a.next = Node(34)
a = a.next
a.next = Node(10)
a = a.next
a.next = Node(45)

menu.cari(110)
menu.cari(10)

##Nomor 6
def binSe(kumpulan, target):
    low = 0
    high = len(kumpulan) - 1

    
    while low <= high:
        mid = (high+low) // 2
        if kumpulan[mid] == target:
            return "Target berada di index", str(mid)
            break
        
        elif target < kumpulan[mid]:
            high = mid - 1

        else:
            low = mid + 1

    return False

list = [2,2,3,5,5,6,9,10,11,12,13,13,14,15,15]
targeta = 5
print("Listnya adalah", list)
print("Nilai target adalah", targeta)
print(binSe(list, targeta))

targetb = 15
print("Listnya adalah", list)
print("Nilai target adalah", targetb)
print(binSe(list, targetb))

##Nomor 7
def binSe(kumpulan, target):
    temp = []
    low = 0
    high = len(kumpulan)-1
    while low <= high :
        mid = (high+low)//2
        if kumpulan[mid] == target:
            midKiri = mid-1
            while kumpulan[midKiri] == target:
                temp.append(midKiri)
                midKiri = midKiri-1
            temp.append(mid)
            midKanan = mid+1
            while kumpulan[midKanan] == target:
                temp.append(midKanan)
                midKanan = midKanan+1
            return temp
        elif target < kumpulan[mid]:
            high = mid-1
        else:
            low = mid+1
    return False

l = [2,3,5,6,6,6,8,9,9,10,11,12,13,13,14]
caria = 6
carib = 13
print("Posisi data", caria, "pada list", l, "adalah", binSe(l, caria))
print("Posisi data", carib, "pada list", l, "adalah", binSe(l, carib))

Nomor 8
print(
"""ada dua pola
pertama menggunakan konsep Big-O. Dimana yang dipakai
adalah rumus O(log n) dengan rincian 1 = 1, 2 = 2, 4 = 3, 10 = 4, 100 = 7, 1000=10.
Di mana log berasal dari pangkat log berbasis 2. Dengan begitu dapat mengetahui jumlah
maksimal tebakan.
Untuk pola sendiri:
        apabila ingin menebak angka 70
        
        a = nilai tebakan pertama // 2
        tebakan selanjutnya = nilai tebakan "lebih dari" + a
        *jika hasil tebakan selanjutnya "kurang dari", maka nilai yang dipakai
        tetap nilai lebih dari sebelumnya*
        a = a // 2
    Simulasi
        tebakan ke 1: 50 (mengambil nilai tengah) jawaban= "lebih dari itu"
        tebakan ke 2: 75 (dari 50 + 25) jawaban = "kurang dari itu"
        tebakan ke 3: 62 (dari 50 + 12) jawaban = "lebih dari itu"
        tebakan ke 4: 68 (dari 62 + 6) jawaban = "lebih dari itu"
        tebakan ke 5: 71 (dari 68 + 3) jawaban = "kurang dari itu"
        tebakan ke 6: 69 (dari 68 + 1) jawaban = "lebih dari itu"
        tebakan ke 7: antara 71 dan 69 hanya ada 1 angka = 70!!!
        
kedua menggunakan barisan geometri Sn = 2^n
        barisan yang terjadi adalah : 2, 4, 8, 16, 32, 64
        Misal angka yang akan diebak adalah 68
        Tebakan ke-1 : 64 dijawab lebih dari itu
        Tebakan ke-2 : 96(dari 64 + 32) dijawab "Kurang dari itu"
        Tebakan ke-3 : 80(dari 64 + 16) dijawab "Kurang dari itu"
        Tebakan ke-4 : 72(dari 64 + 8) dijawab "Kurang dari itu"
        Tebakan ke-5 : 68(dari 64 + 4) dijawab "Lebih dari itu"
        Tebakan ke-6 : 70(dari 68 + 2) dijawab "TEPAT"
        """)
