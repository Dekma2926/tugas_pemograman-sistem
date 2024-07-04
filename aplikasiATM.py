print('SELAMAT DATANG DI ATM ')
print('PILIH OPTION:')
print('1. check uang saya')
print('2. ambil uang saya')
print('3. tabung uang saya')
option=int(input('silahkan pilih option:'))
uang_kamu=200000
if option==1:
    print('uang saya berjumlah Rp.200.000')
elif option==2:
    print('uang saya berjumlah Rp.200.000,mau ambilberapa?')
    print('1. Rp.100.000')   
    print('2. Rp.200.000')
    option2=int(input('option:')) 
    if option2==1:
        hasil=uang_kamu-100000
        print('uang kamu sekarang berjumlah',hasil)
    elif option2==2:
        hasil=uang_kamu-200000
        print('uang kamu sekarang berjumlah', hasil)
    else:
        print('keyword anda salah, mohon ulangi lagi!')
elif option==3:
    print('uang saya berjumlah Rp.200.000, mau tabung berapa?') 
    option3=int(input('masukan jumlah uang:')) 
    hasil3=uang_kamu+option3
    print('jumlah uang kamu sekarang adalah',hasil3) 
else:
    print("pilihan anda salah, silahkan ulangi lagi!!!")     