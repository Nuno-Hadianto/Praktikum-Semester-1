a = 100
print (a)
print(a, type(a))

b = "saya suka makan"
print (b)
print(b, type(b))

c = str(a)
print(c, type(c))

d = int(a)
print(d, type(d))

nama = input ("masukkan nama : ")
nim = int(input ("masukkan nim : "))
print(nama)
print(type(nim))

print ("nama: ", nama)
print ("nim: ", nim)

print(f' hai nama aku   {nama}. saya kuliah di oxford. nim saya {nim}')


amerika = 10 
jepang = 5
kali = amerika * jepang
tambah = amerika + jepang
bagi = amerika / jepang
kurang = amerika - jepang
modulus = amerika % jepang

print (kali, tambah, bagi, kurang, modulus)

a = int(input ('masukkan angka: '))
if (a != 100):
    print ("variabel a adalah 100")
else:
    print ("Variabel a lain 100")


a = (input ('masukkan kata: '))
if (a == "hujan" ):
    print ("basah")
else:
    print ("kering")

print (" PROGRAM MENGHITUNG VOLUME KUBUS\n")
print("nuno\n")

sisi = int(input("Masukkan sisi kubus : "))
volumekubus = sisi * sisi * sisi
print (f'volume kubus adalah : {volumekubus}')

print ("="*40)
print("PROGRAM MENGHITUNG KELILING LINGKARANG\n")
print ("="*40)
diameter = int(input("masukkan diameter lingkaran: "))
phi = 3.14
kelilinglingkaran = 2 * phi * diameter
print(int(kelilinglingkaran))

print(f"keliling lingkaran adalah : {kelilinglingkaran}")