from database_capstone import database_pasien, database_obat,resep
from tabulate import tabulate
from notes_capstone import frame,backToMenu
import time





def menampilkan_pasien():   #fungsi untuk menampilkan database pasien
    frame('Database Pasien')
    pasien=[]
    nama_kolom = ["ID", "Nama", 'Umur']
    for i in range(len(database_pasien)):

        id=database_pasien[i]['id']
        nama=database_pasien[i]['nama']
        umur=database_pasien[i]['umur']

        pasien.append([id, nama, umur])
    time.sleep(0.5)     
    print(tabulate(pasien, nama_kolom, tablefmt="simple_grid", numalign='center', stralign='center'))

# menampilkan_pasien()

def menampilkan_obat():     #fungsi untuk menampilkan database obat
    frame('Database Obat')
    obat=[]
    nama_kolom = ["Kode", "Nama Obat", 'Dosis','Bentuk','Stock Satuan','Harga Satuan']
    for i in range(len(database_obat)):
    # print(dictionaryContoh)

        kode=database_obat[i]['kode']
        nama_obat=database_obat[i]['nama']
        dosis=database_obat[i]['dosis']
        bentuk=database_obat[i]['bentuk']
        stock=database_obat[i]['stock']
        harga=database_obat[i]['harga']

        obat.append([kode,nama_obat,dosis,bentuk,stock,harga])
         
    print(tabulate(obat, nama_kolom, tablefmt="simple_grid", numalign='center', stralign='center'))



def menampilkan_resep(resep):   #fungsi untuk menampilkan resep yang tercatat dalam sistem
    tabel_resep=[]
    # print(tabulate(resep, nama_kolom, tablefmt="simple_grid", numalign='center', stralign='center'))
    frame('Database Resep')
    nama_kolom=['ID','Nama','Dokter','kode obat','dosis','durasi']
    for i in range(len(resep)):
    # print(dictionaryContoh)

        id=resep[i]['id']
        nama=resep[i]['nama']
        dokter=resep[i]['dokter']
        kode=resep[i]['kode']
        dosis=resep[i]['dosis']
        durasi=resep[i]['durasi']
        
        tabel_resep.append([id,nama,dokter,kode,dosis,durasi])
         
    print(tabulate(tabel_resep, nama_kolom, tablefmt="simple_grid", numalign='center', stralign='center'))
    time.sleep(0.5)
    backToMenu('\nTekan ENTER untuk kembali ke Menu Utama\n')



# menampilkan_resep(resep)

