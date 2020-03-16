##Nomor 1
####a
def cekKonsist(n):
    c = 0
    y = 0
    for i in n:
        for j in i:
            y+=1
            if (str(j).isdigit()==False):
                print("Isi Matriks tidak angka semua \nMatrik tidak Konsisten")
                break
            else:
                c+=1
    if(c==y):
        print("Semua Isi Matriks adalah Angka")
        x = len(n[0])
        z = 0
        for i in range(len(n)):
            if (len(n[i]) == x):
               z+=1
        if(z == len(n)):
            print("Matriks Konsisten")
        else:
            print("Matrik tidak Konsisten")
####b
def ordo(n):
    x,y = 0,0
    for i in range(len(n)):
        x+=1
        y = len(n[i])
    print("Mempunyai Ordo "+str(x)+"x"+str(y))
####c
def jumlah(n,m):
    x,y = 0,0
    for i in range(len(n)):
        x+=1
        y = len(n[i])
    xy = [[0 for j in range(x)] for i in range(y)]
    
    z = 0
    if(len(n)==len(m)):
        for i in range(len(n)):
            if(len(n[i]) == len(m[i])):
                z+=1
    if(z==len(n) and z==len(m)):
        print("Ukuran Sama")
        for i in range(len(n)):
            for j in range(len(n[i])):
                xy[i][j] = n[i][j] + m[i][j]
        print(xy)
    else:
        print("Ukuran Beda")
####d
def kali(n,m):
    aa = 0
    x,y = 0,0
    for i in range(len(n)):
        x+=1
        y = len(n[i])
    v,w = 0,0
    for i in range(len(m)):
        v+=1
        w = len(m[i])
        
    if(y==v):
        print("Bisa dikalikan")
        vwxy = [[0 for j in range(w)] for i in range(x)]
        for i in range(len(n)):
            for j in range(len(m[0])):
                for k in range(len(m)):
                    #print(n[i][k], m[k][j])
                    vwxy[i][j] += n[i][k] * m[k][j]
        print(vwxy)
            
    else:
        print("Tidak memenuhi syarat")

####e
def determinHitung(A, total=0):
    x = len(A[0])
    z = 0
    for i in range(len(A)):
        if (len(A[i]) == x):
           z+=1
    if(z == len(A)):
        if(x==len(A)):
            indices = list(range(len(A)))
            if len(A) == 2 and len(A[0]) == 2:
                val = A[0][0] * A[1][1] - A[1][0] * A[0][1]
                return val
            for fc in indices: 
                As = A 
                As = As[1:] 
                height = len(As) 
                for i in range(height): 
                    As[i] = As[i][0:fc] + As[i][fc+1:] 
                sign = (-1) ** (fc % 2) 
                sub_det = determinHitung(As)
                total += sign * A[0][fc] * sub_det
        else:
            return "Tidak bisa dihitung Determinan, bukan Matrix Bujursangkar"
    else:
        return "Tidak bisa dihitung Determinan, bukan Matrix Bujursangkar"
    return total


##Nomor 2

####a
def buatNOL(n,m=None):
    if(m==None):
        m=n
    print("Membuat Matriks 0 dengan Ordo "+str(n)+"x"+str(m))
    print([[0 for j in range(m)] for i in range(n)])

####b
def buatIDENT(n):
    print("Membuat Matriks Identitas dengan Ordo"+str(n)+"x"+str(n))
    print([[1 if j==i else 0 for j in range(n)] for i in range(n)])


##Nomor 3 dan 4
    
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None
##Nomer 3
                
class Linkedlist:
	def __init__(self):
		self.head = None
	def tambahDepan(self, new_data):
		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node
	def tambahAkhir(self, data):
		if (self.head == None):
			self.head = Node(data)
		else:
			current = self.head
			while (current.next != None):
				current = current.next
			current.next = Node(data)
		return self.head
	def tambah(self,data,pos):
		node = Node(data)
		if not self.head:
			self.head = node
		elif pos==0:
			node.next = self.head
			self.head = node
		else:
			prev = None
			current = self.head
			current_pos = 0
			while(current_pos < pos) and current.next:
				prev = current
				current = current.next
				current_pos +=1
			prev.next = node
			node.next = current
		return self.head
	def hapus(self, position):
		if self.head == None:
			return
		temp = self.head
		if position == 0:
			self.head = temp.next
			temp = None
			return
		for i in range(position -1 ):
			temp = temp.next
			if temp is None:
				break
			if temp is None:
				return
			if temp.next is None:
				return
			next = temp.next.next
			temp.next = None
			temp.next = next
	def cari(self, x):
		current = self.head
		while current != None:
			if current.data == x:
				return "True"
			current = current.next
		return "False"
	def tampilkan(self):
		current = self.head
		while current is not None:
			print(current.data, end = ' ')
			current = current.next

##Nomer 4

class DoublyLinkedList: 
    def __init__(self): 
        self.head = None
    def awal(self, new_data):
        print("menambah pada awal", new_data)
        new_node = Node(new_data) 
        new_node.next = self.head 
        if self.head is not None: 
            self.head.prev = new_node 
        self.head = new_node 
    def akhir(self, new_data):
        print("menambah pada akhir", new_data)
        new_node = Node(new_data) 
        new_node.next = None
        if self.head is None: 
            new_node.prev = None
            self.head = new_node 
            return 
        last = self.head 
        while(last.next is not None): 
            last = last.next
        last.next = new_node 
        new_node.prev = last 
        return
    def printList(self, node): 
        print("\nDari Depan :")
        while(node is not None): 
            print(" % d" %(node.data))
            last = node 
            node = node.next
        print("\nDari Belakang :")
        while(last is not None): 
            print(" % d" %(last.data)) 
            last = last.prev 
