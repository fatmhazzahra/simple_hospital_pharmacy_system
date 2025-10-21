import os
import time
from tabulate import tabulate
import pwinput

#Daftar pasangan username dan password yang dapat mengakses aplikasi
list_login = [
    {
        'username': 'suster',
        'password': 'sus123',
    },
    {
       'username': 'dokter',
        'password': 'dok123',
   },
    {
       'username': 'apoteker',
        'password': 'apt123',
 }
]

def login():
    opening() #Menampilkan layar opening
    time.sleep(1) #jeda 1 detik sebelum memasukkan username dan password
    nama = [d['username'] for d in list_login]
    pw = [d['password'] for d in list_login]

    user=input('USERNAME: ')    #Masukkan username
    user=user.lower()
   

    if user not in nama:    #jika username tidak dikenal/salah, ulangi proses login
        bersihkan_terminal()
        frame('User tidak dikenal')
        time.sleep(1)
        login()  
    else:
        password = pwinput.pwinput('PASSWORD: ')    #jika username benar, masukkan password
           
        if password not in pw:
            bersihkan_terminal()         #jika password salah, ulangi login dari awal, masukkan username lagi
            frame('Password yang anda masukkan tidak cocok')
            time.sleep(1)
            login()    
        else:    
            x=input("Nama {}:".format(user))        #jika password benar, masukkan nama asli user 

    for i in range (len(nama)):             #menandakan user telah masuk ke dalam sistem
        if user==nama[i] and password==pw[i]:
            frame('Anda telah masuk ke sistem {}'.format(user))
            time.sleep(1)
        elif user==nama[i] and password!=pw[i]:     #jika password dan username sesuai tapi bukan pasangan yang benar, sistem menolak akses
            bersihkan_terminal()
            
            frame('Anda ditolak masuk ke sistem')
            time.sleep(1)
            login()
            break
    return user 

def cek_input_angka(angka):
# Fungsi ini akan meng-handle error jika
    # -> User memberikan input yang bukan digit
    # -> User memberikan input berupa angka negatif
# Lalu memberikan feedback di setiap error yang terdeksi oleh cek_input_angka(angka)
    while True:
        try:
            input_angka = int(input(angka))
            if input_angka < 0:
                print('Input tidak boleh negatif, silahkan coba lagi.')
                continue
            elif input_angka > 1000000:
                print('\nInput melebihi batasan, silahkan coba lagi.')
                continue
            return input_angka
        except ValueError:
            print('\nInvalid input, silahkan coba lagi.')


def backToMenu(perintah):
# Fungsi untuk handle error dari user input
# saat validasi lanjut/tidak di setiap fitur CRUD
    pressEnter = input(perintah)
    if pressEnter == '':
        return
    
#format tampilan teks
def frame(text):
    print('='*(len(text)))
    print(text)
    print('='*(len(text)))

#format tampilan teks 
def frame_bintang(text):
    print('*'*(len(text)))
    print(text)
    print('*'*(len(text)))

#menghapus isi terminal
def bersihkan_terminal():
    # Periksa nama OS: 'nt' untuk Windows, 'posix' untuk Linux/macOS
    if os.name == 'nt':
        _ = os.system('cls') # Gunakan 'cls' untuk Windows
    else:
        _ = os.system('clear') # Gunakan 'clear' untuk Linux/macOS

#tampilan pembuka aplikasi
def opening():
    bersihkan_terminal() 
    frame('     APLIKASI RUMAH SAKIT APOTEK     ')


#tampilan penutup aplikasi
def closing():
    
    closing_msg = [['   PROGRAM SELESAI TERIMAKASIH     ']]
    print('         \n')
    print(tabulate(closing_msg, tablefmt='grid', stralign='center'))

