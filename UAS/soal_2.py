import pandas as pd

print('Data penjumlahan Toko Makmur')

df = pd.DataFrame([
   [90,50,65],
   [80,60,70]
],columns=['mahasiswa 1','mahasiswa 2','mahasiswa 3'], index=['algoritma dan struktur data 2','matematika numerik'])


df1 = df.mean(axis=1)
df3 = df.mean(axis=0)

print(f'rata-rata nilai untuk setiap mata kuliah : ')
print('nilai algoritma dan struktur data',df1)
print('nilai matematika numerik',df1)

print(f'rata-rata nilai untuk setiap mahasiswa : ')
print(
    ''' nilai mahasiswa 1 :
        nilai mahasiswa 2 : 
        nilai mahasiswa 3 : ''',df3)
