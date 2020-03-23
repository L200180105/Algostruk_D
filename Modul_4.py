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

list = [1,2,2,3,3,3,5,5,6,9,10,11,12,13,13,14,15,15]
targeta = 3
print("Listnya adalah", list)
print("Nilai target adalah", targeta)
print(binSe(list, targeta))
print("\n")
targetb = 15
print("Listnya adalah", list)
print("Nilai target adalah", targetb)
print(binSe(list, targetb))
print("\n")
targetc = 16
print("Listnya adalah", list)
print("Nilai target adalah", targetc)
print(binSe(list, targetc))
