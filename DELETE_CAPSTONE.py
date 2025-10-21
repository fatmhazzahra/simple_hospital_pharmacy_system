from tabulate import tabulate
import time
from notes_capstone import bersihkan_terminal, frame_bintang
from database_capstone import database_pasien, database_obat
from READ_CAPSTONE import menampilkan_pasien, menampilkan_obat,backToMenu

#menghapus data pasien dari database pasien
def delete_pasien():
    id_database_pasien = [d['id'] for d in database_pasien]
    bersihkan_terminal()
    menampilkan_pasien()
    pasien_delete= input('Masukkan ID pasien yang ingin dihapus: ')

    for i in range(len(database_pasien)):
        if pasien_delete==database_pasien[i]['id']:
            nama=database_pasien[i]['nama']
            
            validasi=input(f'yakin ingin menghapus pasien {nama}? (ya/tidak) ')
            if validasi=='ya':
                del database_pasien[i]
                frame_bintang('Pasien berhasil dihapus')
                time.sleep(1)
                
            bersihkan_terminal()
            menampilkan_pasien()
            time.sleep(0.5)
            backToMenu('\nTekan ENTER untuk kembali ke Menu Utama\n')
            break
    if pasien_delete not in id_database_pasien:
        frame_bintang('ID yang anda masukkan belum terdaftar di sistem')
        time.sleep(0.5)
        backToMenu('\nTekan ENTER untuk kembali ke Menu Utama\n')
    
#menghapus data obat dari database obat
def delete_obat():
    id_database_obat = [d['kode'] for d in database_obat]
    bersihkan_terminal()
    menampilkan_obat()
    obat_delete= input('Masukkan kode obat yang ingin dihapus: ')

    for i in range(len(database_obat)):
        if obat_delete==database_obat[i]['kode']:
            nama=database_obat[i]['nama']
            dosis=database_obat[i]['dosis']
            validasi=input(f'yakin ingin menghapus obat {nama} {dosis}? (ya/tidak) ')
            if validasi=='ya':
                del database_obat[i]            
                frame_bintang('Obat berhasil dihapus')
                time.sleep(1.5)
                
            bersihkan_terminal()
            menampilkan_obat()
            time.sleep(0.5)
            backToMenu('\nTekan ENTER untuk kembali ke Menu Utama\n')
            break
    if obat_delete not in id_database_obat:
        frame_bintang('Kode yang anda masukkan belum terdaftar di sistem')
        time.sleep(0.5)
        backToMenu('\nTekan ENTER untuk kembali ke Menu Utama\n')
# delete_pasien()
            


