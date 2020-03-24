def swap(a,p,q):
    tmp = a[p]
    a[p]=a[q]
    a[q]=tmp
K = [50,20,70,10]
swap(K,1,3)
print(K)

def cariposisiterkecil(a,darisini,sampaisini):
    posisiyangterkecil = darisini
    for i in range(darisini+1,sampaisini):
        if a[i]< a[posisiyangterkecil]:
            posisiyangterkecil = i
    return posisiyangterkecil
A = [18,13,44,25,66,107,78,89]
j = cariposisiterkecil(A,2,len(A))
print(j)

def kecil(a):
    ter = 0
    for i in range(ter,len(a)):
        if a[i] < a[ter]:
            ter = i
    return ter
f = kecil(A)
print(f)

def bubblesort(a):
    for buble in range(len(a)-1,0,-1):
        for i in range(buble):
            if a[i]>a[i+1]:
                swap(a,i,i+1)

bubblesort(A)
print(A)

def selectionsort(a):
    n = len(a)
    for i in range(n-1):
        kecil = cariposisiterkecil(a,i,n)
        if kecil != i:
            swap(a,i,kecil)
selectionsort(K)
print(K)

def insertionsort(a):
    for i in range(1,len(a)):
        nilai = a[i]
        b = i
        while b >0 and nilai<a[b - 1]:
            a[b]=a[b-1]
            b -=1
        a[b]=nilai
P=[10,51,2,18,4,31,13,5,23,64,29]
insertionsort(P)
print(P)
