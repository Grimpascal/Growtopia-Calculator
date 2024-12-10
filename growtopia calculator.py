print('='*39)
print('''Selamat datang di growtopia Calculator...
      Pilih Opsi : 
      1. World Lock -> Diamond lock
      2. Diamond Lock -> BGL''')
inputan_user = input('Pilih [1] atau [2] : ')

if inputan_user == '1':
    wl = int(input('Masukkan Jumlah World Lock : '))
    hasil = wl/100
    print(f'Jumlah diamond Lock anda adalah {hasil}')
elif inputan_user == '2':
    dl = int(input('Masukkan Jumlah Diamond Lock : '))
    hasil = dl/100
    print(f'Jumlah bgl anda adalah {hasil}')
else:
    print('Perintah Tidak Valid')