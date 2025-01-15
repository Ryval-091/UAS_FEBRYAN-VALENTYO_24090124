import pandas as pd

print('Data penjumlahan Toko Makmur')

df = pd.DataFrame([
   [90,50,65],
   [80,60,70]
],columns=['mahasiswa 1','mahasiswa 2','mahasiswa 3'], index=['algoritma dan struktur data 2','matematika numerik'])


df['total nilai algoritma'] = df.sum(axis=1)
df['total nilai matematika'] = df.sum(axis=1)

print(f'rata-rata nilai untuk setiap mata kuliah : ')
print('nilai algoritma dan struktur data',df)
print('nilai matematika numerik',df)

print(f'rata-rata nilai untuk setiap mahasiswa : ')
print('nilai mahasiswa 1 : ', )
print('nilai mahasiswa 2 : ', )
print('nilai mahasiswa 3 : ', )
