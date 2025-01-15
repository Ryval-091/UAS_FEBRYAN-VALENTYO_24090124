import Soal_3_modul as md

while True:
    print(f'Antrian sekarang : {md.front()} Sedang memesan')
    print(f'Antrian selanjutnya : {md.front()+1} ')
    print(f'Jumlah antrian : {md.size()}')

    print(f'Pilihan : ')
    print(f'1. Tambah antrian')
    print(f'2. hapus')
    print(f'3. Keluar')

    pilihan = int(input(f'Masukkan pilihan (1/2/3) : '))

    nama = input(f'Masukkan pesanan : ')

    if pilihan == 1: 
        md.enqueue()
    elif pilihan == 2:
        md.dequeue()
    elif pilihan == 3:
        print('keluar')
        break