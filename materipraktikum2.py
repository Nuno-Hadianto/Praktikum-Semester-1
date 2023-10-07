# percabangan

x = 22

#! percabangan if else
# if ((x % 2) == 0):
#   print('ini bilangan genap')
# else:
#   print("ini bilangan ganjil")

#! percabangan if, elif, else
# tanya = input("apakah kamu jujur? (y/n): ")

# if (tanya == 'y'):
#   print("oke, kamu jujur")

# elif (tanya == 'n'):
#   print("kamu berbohong akupun percaya")

# else:
#   print("gaje")


#! nested if
# tabungan = 10000
# umur = 20

# if umur < 20:
#   print('kamu dah masih kecil dek')

# elif umur >= 20:
#   print("udah gede")
#   if tabungan < 1000000:
#     print("tapi kamu bokek")
#   elif tabungan == 1000000:
#     print("aman sih. tapi kerja lagi ya")
#   else:
#     print("aman dah tabungan")

# else:
#   print("error")

# =================================================================================================================
# ? perulangan

#! for loop

# umur = 90

# for i in range(umur):
#   print(umur)
#   umur += 1
#   if umur == 100:
#     print("innalillah")
#     # buat berentiin perulangan
#     break

# # hitung terbalik ke bawah
# for ayam in reversed(range(10)):
#     print("mati 1, tinggallah", ayam)


#! while loop
# ask = 'yes'
# while (ask == 'yes'):
#   print("oke")
#   ulang = input("ulang? (y/n)")
#   if (ulang == 'n'):
#     print("terimakasih")
#     # break

# =================================================================================================================

#? list dan tuple
# list adalah tempat dimana kita bisa menaruh beberapa value (nilai)
# list ditandai dengan kurung siku

# kotaKosong = []
# print(kotaKosong, type(kotaKosong), "\n")

# # index
# #         0             1           2           3           4         5
# #         -6            -5          -4          -3            -2       -1
kota = ["samarinda", "bontang", "sangatta", "balikpapan", "berau", "tenggarong"]
# campursari = ["aku", 12, "yesh", 3.4]

# print(kota)
# print(campursari)

# # cara narik data dari list
# # index dimulai dari 0
# print(kota[0])

# # reverse index
# print(kota[-2])

# # slicing
# # print dari index 1 sampai sebelum index 4
# print(kota[1:4])

#! CRUD (create, read, update, delete)

# create: nambah data di kota (dipaling belakang) 
kota.append("paser")
print(kota)
print('\n')
# nambah data di list kota (diselipin)
kota.insert(2, "bengalon" )
print(kota)
print('\n')

# read: membaca data
print(kota[1], kota[2])

# update
kota[1] = "sepaku"
print(kota)

# kalo mau tukar tempatnya
kota[-1], kota [0] = kota[0], kota[-1]
print(kota)

# delete

# remove: menghapus berdasarkan nilai
kota.remove("berau")
print(kota)

# pop: menghapus data index terakhir
kota.pop()
print(kota)

#del
del kota[2]
print(kota)


# ! nested list
penyanyi = ['justin', ['bieber', 'hailey'] , 'hivi', 'odo', 'avril']
print(penyanyi[1][1])

# gabungin 2 list
kartun = ['sopo jarwo', 'tayo', 'dora']
anime = ['doraemon', 'naruto', 'conan']

kartun.extend(anime)
print(kartun)

# prettytable
from prettytable import PrettyTable
table = PrettyTable()
table.field_names = [" No ", " Nama ", " Warna "]
table.add_row([1, "pisang", "kuning"])
table.add_row([2, "mangga", "hijau"])
table.add_row([3, "kiwi", "coklat"])
print(table)