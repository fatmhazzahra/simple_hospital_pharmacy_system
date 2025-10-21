from READ_CAPSTONE import menampilkan_pasien, menampilkan_obat
from CREATE_CAPSTONE import tambah_pasien_baru, input_obat_baru, tambah_resep_baru
from UPDATE_CAPSTONE import ubah_harga_obat, restock_obat
from DELETE_CAPSTONE import delete_pasien, delete_obat
from FITUR_CAPSTONE import total_price
from notes_capstone import bersihkan_terminal, opening, closing, login, cek_input_angka,backToMenu

def menu_utama():
    user=login()
    
    while True:
        opening()

        menu = cek_input_angka('''
    [1] Tampilkan Data Pasien
    [2] Tampilkan Data Obat
    [3] Tambahkan Data Pasien
    [4] Tambahkan Obat Baru
    [5] Restock Obat
    [6] Tambahkan Data Resep Pasien
    [7] Hapus Data Pasien
    [8] Hapus Data Obat
    [9] Ubah Harga Obat
    [10] Total Harga Obat
    [0] Exit

    Silahkan pilih menu: ''')
        
        if user == 'suster' or user=='dokter':
            if menu == 4 or menu==5 or menu == 8 or menu ==9:
                bersihkan_terminal()
                print('\nAkses ditolak, hanya APOTEKER yang dapat mengakses fitur ini.')
                backToMenu('\nTekan ENTER untuk kembali ke Menu Utama\n')
                continue
        elif user=='apoteker':
            if menu == 3 or menu== 6 or menu==7:
                bersihkan_terminal()
                print('\nAkses ditolak, hanya SUSTER dan DOKTER yang dapat mengakses fitur ini.')
                backToMenu('\nTekan ENTER untuk kembali ke Menu Utama\n')
                continue
        
        if menu == 0:
            return closing()
        elif menu == 1:
            menampilkan_pasien()
            backToMenu('\nTekan ENTER untuk kembali ke Menu Utama\n')
        elif menu == 2:
            menampilkan_obat()
            backToMenu('\nTekan ENTER untuk kembali ke Menu Utama\n')

        elif menu == 3:
            tambah_pasien_baru()
        elif menu == 4:
            input_obat_baru()
        elif menu == 5:
            restock_obat()
        elif menu == 6:
            tambah_resep_baru()
        elif menu == 7:
            delete_pasien()
        elif menu == 8:
            delete_obat()
        elif menu == 9:
            ubah_harga_obat()
        elif menu == 10:
            total_price()
     

if __name__ == '__main__':
    menu_utama()