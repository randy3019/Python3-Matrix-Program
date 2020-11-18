import numpy as np

B = int(input("Masukan Jumlah baris:"))
K = int(input("Masukan Jumlah Kolom:"))
##input_elemen**2_di-matrix
print(60*"+")
print("Masukan Elemen:(masing2 elemen dipisahkan dengan spasi):")
Masukan= list(map(int, input().split()))  ##mengolah_inputan_elemen_di-matrix
matrix = np.array(Masukan).reshape(B, K)  ##menampilkan_elemen_dan_ukuran_dari_matrix
print("jenis matrix =\n", matrix) 

Determinan = np.linalg.det(matrix)
print("Determinan dari matrix adalah:",Determinan)

##create by randy
##nim:0217***
#math-ITK
