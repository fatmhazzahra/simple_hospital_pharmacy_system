from READ_CAPSTONE import menampilkan_obat
from database_capstone import database_obat
from notes_capstone import frame, frame_bintang, bersihkan_terminal, backToMenu, cek_input_angka
import time

#fungsi untuk menambah stock obat yang sudah ada di database
def restock_obat():
    bersihkan_terminal()
    menampilkan_obat()
    kode=input('Masukkan kode obat: ')
    for i in range(len(database_obat)):
        if kode == database_obat[i]['kode']:
            nama_obat=database_obat[i]['nama']
            dosis=database_obat[i]['dosis']
            validasi=input(f'Apakah yang dimaksud {nama_obat} {dosis}? (ya/tidak) ')
            #penambahan stock obat ke dalam database obat
            if validasi=="ya":
                stock=input('Masukkan stock tambahan obat (satuan): ')   
                stock_baru=(int(database_obat[i]['stock'])+int(stock))
                database_obat[i]['stock']=stock_baru
                tambah=input('Apakah ada obat tambahan? (ya/tidak) ')
                if tambah=='ya':
                    restock_obat()
                else:
                    frame('Obat selesai diupdate')
                    time.sleep(1)
                    bersihkan_terminal()
                    menampilkan_obat()
                    time.sleep(0.5)
                    backToMenu('\nTekan ENTER untuk kembali ke Menu Utama\n')
                break
            else:
                frame_bintang('Kode yang anda masukkan salah')
                time.sleep(0.5)
                backToMenu('\nTekan ENTER untuk kembali ke Menu Utama\n')
    if kode != database_obat[i]['kode']:
                frame_bintang('Kode yang anda masukkan salah')
                time.sleep(0.5)
                backToMenu('\nTekan ENTER untuk kembali ke Menu Utama\n')

                
    


def ubah_harga_obat():
    bersihkan_terminal()
    menampilkan_obat()
    kode=input('Masukkan kode obat: ')
    for i in range(len(database_obat)):
        if kode == database_obat[i]['kode']:
            nama_obat=database_obat[i]['nama']
            dosis=database_obat[i]['dosis']
            validasi=input(f'Apakah yang dimaksud {nama_obat} {dosis}? (ya/tidak) ')
            if validasi=="ya":
                x=i
                harga=cek_input_angka('Masukkan harga obat terbaru (per pcs) (harga tanpa titik): ')
                database_obat[x]['harga']=harga               
                break
            else:
                ubah_harga_obat()
    
    tambah=input('Apakah ada harga obat yang ingin diubah lagi? (ya/tidak) ')
    if tambah=='ya':
        ubah_harga_obat()
    else:
        frame('Harga obat selesai diubah')
        time.sleep(1.5)
        bersihkan_terminal()
        menampilkan_obat()
        time.sleep(0.5)
        backToMenu('\nTekan ENTER untuk kembali ke Menu Utama\n')

