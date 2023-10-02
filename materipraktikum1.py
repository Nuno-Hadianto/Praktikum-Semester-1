# materi: variabel
a = 20
b = 30

ab = a + b
print (ab)

# ---------------------------------------------------------------------

# latihan variabel dan aritmatika
nilai1 = 23
nilai2 = -2

#! gunakan operator aritmatika dan operator perbandingan untuk melakukan perhitungan antara nilai1 dan nilai2. dicoba semua dari perkalian, pembagian, modulus, dll
# contoh:
kali = nilai1 * nilai2
print(kali)

# bagi = ....
bagi = nilai1 / nilai2
print(bagi)

# tambah = ....
tambah = nilai1 + nilai2
print(tambah)

# ---------------------------------------------------------------------

# materi parsing/convert tipe data dan cek tipe data
# variabel ada tipe datanya: string untuk kata, integer untuk angka, float untuk desimal, dll

cobaParsing = 22

# untuk mengecek tipe variabel cobaParsing
print(type(cobaParsing))

ubahTipe = str(22)

# untuk mengecek tipe datanya variabel ubahTpe
print(type(ubahTipe))
# ---------------------------------------------------------------------

# latihan parsing data
harga = "20000"

# ubah variabel harga dari tipe data sebelumnya menjadi angka
harga_int = harga
print(type(harga))

# ubah variabel harga dari tipe data sebelumnya menjadi desimal
harga_float = harga
print(type(harga))

# ---------------------------------------------------------------------
# materi input
#nim = input("masukkan nim kamu: " )
#print(nim, "dan", type(nim))

# ---------------------------------------------------------------------
# latihan inputan dan parsing data
# buatlah 3 inputan, yaitu input nama produk, harga produk, dan deskripsi produk. pastikan harga produk harus bertipe data integer/number/float

# Meminta input dari pengguna
nama_produk = input("Masukkan nama produk: ")
harga_produk = float(input("Masukkan harga produk (angka): "))
deskripsi_produk = input("Masukkan deskripsi produk: ")

# Menampilkan informasi produk
print("\nInformasi Produk:")
print("Nama Produk:", nama_produk)
print("Harga Produk:", harga_produk)
print("Deskripsi Produk:", deskripsi_produk)


# ---------------------------------------------------------------------
# LATIHAN
# buat program sederhana untuk menghitung Body Mass Index (BMI)
# program diawali dengan indetifikasi user. masukkan nama, umur, dll

nama = input("masukkan nama kamu: " )
print(nama, "dan", type(nama))

nim = input("masukkan nim kamu: " )
print(nim, "dan", type(nim))

# Input berat (dalam kilogram) dan tinggi (dalam meter)
berat = float(input("Masukkan berat Anda (kg): "))
tinggi = float(input("Masukkan tinggi Anda (m): "))

# Menghitung BMI
bmi = berat / (tinggi ** 2)

# Menampilkan hasil BMI
print("BMI Anda adalah:", bmi)

# Menampilkan kategori BMI
if bmi < 18.5:
    kategori = "Kurang berat badan"
elif 18.5 <= bmi < 24.9:
    kategori = "Normal (sehat)"
elif 25 <= bmi < 29.9:
    kategori = "Kelebihan berat badan"
else:
    kategori = "Obesitas"

print("Kategori BMI Anda adalah:", kategori)
