from collections import deque
#Jumlah Antrian Pagi Jam 10.00 WIB
antrian = deque([1,2,3,4,5])

print("Jumlah Antrian : ",antrian)

#Antrian Bertambah / Kedatangan Nasabah Baru pada Pagi Jam 10.20 WIB
antrian.append(6)
print("Nasabah ke ",6)
print("Jumlah Antrian :",antrian)

#Antrian Bertambah / Kedatangan Nasabah Baru pada Pagi Jam 10.30 WIB
antrian.append(7)
print("Nasabah ke ",7)
print("Jumlah Antrian :",antrian)

#Antrian Berkurang / Nomor Antrian telah dipanggil Pada 10.35 WIB
out = antrian.popleft()
print("Nasabah yang keluar",out)
print("Jumlah Nasabah Sekarang :",antrian)

#Antrian Berkurang / Nomor Antrian telah dipanggil Pada 10.40 WIB
out = antrian.popleft()
print("Nasabah yang keluar",out)
print("Jumlah Nasabah Sekarang :",antrian)

#Antrian Berkurang / Nomor Antrian telah dipanggil Pada 10.45 WIB
out = antrian.popleft()
print("Nasabah yang keluar",out)
print("Jumlah Nasabah Sekarang :",antrian)

#Antrian Bertambah / Kedatangan Nasabah Baru pada Pagi Jam 10.50 WIB
antrian.append(8)
print("Nasabah ke ",8)
print("Jumlah Antrian :",antrian)