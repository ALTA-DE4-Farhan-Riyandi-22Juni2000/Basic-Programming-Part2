'''
Input Harga: 370000
Input Diskon: 15
Output: harga yang harus dibayar adalah Rp. 314.500
'''
harga_awal = int(input('Input harga: '))
diskon = int(input('Input Diskon: '))

harga_diskon = (diskon/100) * harga_awal
harga_akhir = harga_awal - harga_diskon

print('harga yang harus dibayar adalah Rp.', int(harga_akhir))