import time
from database_capstone import database_pasien, database_obat, resep
from READ_CAPSTONE import menampilkan_pasien
from notes_capstone import bersihkan_terminal, frame_bintang, backToMenu, frame
from tabulate import tabulate

def menampilkan_resep_tertentu(id):   #fungsi untuk menampilkan resep yang tercatat dalam sistem
    tabel_resep=[]
    nama_kolom=['kode obat','dosis','durasi','harga']
    for i in range(len(resep)):
    # print(dictionaryContoh)
        if id==resep[i]['id']:
            id=resep[i]['id']
            nama=resep[i]['nama']
            dokter=resep[i]['dokter']
            kode=resep[i]['kode']
            dosis=resep[i]['dosis']
            durasi=resep[i]['durasi']
            
        
            tabel_resep.append([kode,dosis,durasi])
    frame(f''' ID \t: {id} \n PASIEN\t: {nama} \n DOKTER\t: dr. {dokter}''')
    print(tabulate(tabel_resep, nama_kolom, tablefmt="simple_grid", numalign='center', stralign='center'))
    time.sleep(0.5)


def total_price():
    bersihkan_terminal()
    menampilkan_pasien()
    id_database_pasien = [d['id'] for d in database_pasien]
    id = input('harga obat dari ID Pasien: ')
#jika pasien tidak ditemukan dalam database pasien
    if id not in id_database_pasien:
        frame_bintang('ID yang dicari tidak ditemukan')
#mencari id pasien dalam database pasien
    for i in range(len(database_pasien)):
        if id == database_pasien[i]['id']:
            nama=database_pasien[i]['nama']
            validasi=input(f'Apakah Pasien yang dimaksud {nama}? (ya/tidak) ')
            if validasi=="ya":
                break

    total_harga=0
    for i in range(len(resep)): #perhitungan harga untuk setiap jenis obat
        if id==resep[i]['id']:
            dosis=resep[i]['dosis']
            durasi=resep[i]['durasi']
            durasi=int(durasi)
            kode=resep[i]['kode']
            x,y=dosis.split('x')
            x=int(x)
            y=int(y)

            jumlah_obat_per_jenis=(x*y)*durasi
# jika stock mencukupi, hitung total harga
# jika stock tidak cukup, tampilkan pesan stock tidak mencukupi
            for i in range(len(database_obat)):
                if kode==database_obat[i]['kode']:
                    stock_obat=int(database_obat[i]['stock'])
                    if jumlah_obat_per_jenis<stock_obat:
                        harga_satuan=database_obat[i]['harga']
                        harga=int(harga_satuan)
                        total_harga_perjenis=jumlah_obat_per_jenis*harga             
                        total_harga+=total_harga_perjenis
                    elif jumlah_obat_per_jenis>stock_obat:
                        obat_tidak_cukup=str(f'Stock obat tidak mencukupi untuk kode obat {kode}. Stock tersedia: {stock_obat}')
                else:
                    obat_tidak_tersedia=str(f'Obat dengan kode {kode} tidak tersedia.')
            
            
    bersihkan_terminal()
#jika ID pasien tidak ditemukan dalam database resep,
#pasien ada dalam database pasien, tapi saat dijalankan fungsi perhitungan total harganya 0, karena belum ada resep yang diinput
    if total_harga<=0:
        frame_bintang('Resep belum di input ke dalam sistem')
        time.sleep(0.5)
        backToMenu('\nTekan ENTER untuk kembali ke Menu Utama\n')
    
#menampilkan total harga dan stock obat yang tidak mencukupi
    else:
        menampilkan_resep_tertentu(id)
        frame_bintang(f'Total harga obat pasien atas nama {nama} adalah Rp {total_harga}')
        print('\n')
        print(obat_tidak_cukup) if 'obat_tidak_cukup' in locals() else None       
        print(obat_tidak_tersedia) if 'obat_tidak_tersedia' in locals() else None
        print('\n')
        time.sleep(1)
        backToMenu('\nTekan ENTER untuk kembali ke Menu Utama\n')


                                                                                    
            