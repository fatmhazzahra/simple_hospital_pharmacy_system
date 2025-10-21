from READ_CAPSTONE import menampilkan_pasien, menampilkan_obat, menampilkan_resep
import random
import time
from notes_capstone import bersihkan_terminal, frame, frame_bintang,backToMenu,cek_input_angka
from database_capstone import database_pasien, database_obat,resep


#menambahkan pasien baru ke dalam database
def tambah_pasien_baru ():
    bersihkan_terminal()
    frame('Pasien Baru')
    id=input('Masukkan ID Pasien : ')
    nama=input('Masukkan Nama Pasien : ')
    umur=cek_input_angka('Masukkan Umur Pasien: ')
    pasien_baru={'id':id,'nama':nama, 'umur':umur}
    database_pasien.append(pasien_baru)

    tambah=input('Apakah ada Pasien baru yang ingin ditambahkan lagi? (ya/tidak) ')
    if tambah=='ya':
        tambah_pasien_baru()
    else:
        frame_bintang('Pasien selesai dimasukkan')
        time.sleep(2)
        bersihkan_terminal()
        menampilkan_pasien()
        time.sleep(0.5)
        backToMenu('\nTekan ENTER untuk kembali ke Menu Utama\n')

#menambahkan obat baru ke dalam database
def input_obat_baru():
    bersihkan_terminal()
    nama_obat=input('Masukkan nama obat : ')
    dosis=(input(str('Masukkan dosis obat (mg per pcs) : '))+'mg')
    bentuk=input('Masukkan bentuk obat (tablest/sirup/serbuk) : ')
    stock=input('Masukkan stock obat (pcs): ')
    harga=input('Masukkan harga obat (Rp per pcs): ')
    #generate kode obat
    kode=((''.join(random.sample(nama_obat,3)))+dosis[:-2])
    obat_baru={'kode':kode,'nama':nama_obat,'dosis':dosis,'bentuk':bentuk,'stock':stock,'harga':harga}
    database_obat.append(obat_baru)

    tambah=input('Apakah ada obat tambahan? (ya/tidak) ')
    if tambah=='ya':
        input_obat_baru()
    else:
        frame_bintang('Obat selesai dimasukkan')
        time.sleep(2)
        bersihkan_terminal()
        menampilkan_obat()
        time.sleep(0.5)
        backToMenu('\nTekan ENTER untuk kembali ke Menu Utama\n')


#dibuat untuk dipanggil ke dalam fungsi tambah_resep_baru, 
# supaya tidak mengulangi input nama, id dan dokter pasien ke dalam database resep
def resep_obat(id,nama,dokter):     
    
    bersihkan_terminal()
    menampilkan_obat()
    kode=input('Masukkan kode obat : ')
    dosis=input('Masukkan dosis obat (axb): ') 
    durasi=cek_input_angka('Masukkan durasi pemberian obat (hari): ')
    validasi=input('input resep lagi?(ya/tidak) ')
    
    resep_baru={'id':id,'nama':nama, 'dokter':dokter,'kode':kode,'dosis':dosis,'durasi':durasi}
    
    resep.append(resep_baru) 
    
    # mengurangi stock obat di database sesuai dengan resep yang diinput
    for i in range(len(database_obat)):
        if kode==database_obat[i]['kode']:
            x,y=dosis.split('x')
            x=int(x)
            y=int(y)
            jumlah_obat_per_jenis=(x*y)*int(durasi)
            if jumlah_obat_per_jenis>int(database_obat[i]['stock']):
                pass
            else:
                stock_update=int(database_obat[i]['stock'])-jumlah_obat_per_jenis
                database_obat[i]['stock']=stock_update
            break

    if validasi=='ya':
        resep_obat(id,nama,dokter)
    else:
        frame_bintang('resep selesai di input')
        time.sleep(2)
        bersihkan_terminal()
        menampilkan_resep(resep) #yang tampil semua resep, ga cuma pasien itu aja
        

#menambahkan resep baru ke dalam database
def tambah_resep_baru():
    bersihkan_terminal()
    id=input('Masukkan ID Pasien : ')

    id_database_pasien = [d['id'] for d in database_pasien]
    
    for i in range(len(database_pasien)):
        if id == database_pasien[i]['id']:
            nama=database_pasien[i]['nama']
            umur=database_pasien[i]['umur']
            validasi=input(f'Apakah Pasien yang dimaksud {nama} berumur {umur}? (ya/tidak) ')
            if validasi=="ya":
                dokter=input('Masukkan Nama dokter: ')
                resep_obat(id,nama,dokter)      #memanggil fungsi resep_obat
                break
            else:
                frame('ID yang anda cari tidak ditemukan')
                time.sleep(0.5)
                backToMenu('\nTekan ENTER untuk kembali ke Menu Utama\n')


            
                
    if id not in id_database_pasien:
        frame_bintang('ID yang anda masukkan belum terdaftar di sistem')
        time.sleep(0.5)
        backToMenu('\nTekan ENTER untuk kembali ke Menu Utama\n')

# tambah_resep_baru()
