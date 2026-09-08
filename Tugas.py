buku = ("Cara menghitung rumus fisika kuantum khusus anak anak", "cara masuk tk favorit", "buku snbt untuk balita", "makan", "mandi")
list_peminjaman = []
print(buku)

while True:
    nama_buku = input("inputkan buku dan jika udah selesai ketik aja selesai beres :")
    if nama_buku.lower() == "selesai":
        break  
    if nama_buku in buku:
        print ("buku tersedia")
        list_peminjaman.append(nama_buku)
    else:
        print("maaf buku ga ada")

if list_peminjaman:
    hapus_buku = input("mau hapus buku? silahkan masukan, kalau ga ada ketik aja (ga ada): ")
    if hapus_buku.lower() == "ga ada":
        print("mantap ga ada buku yang terhapus")
    elif hapus_buku in list_peminjaman:
        list_peminjaman.remove(hapus_buku)
        print("buku terhapus bro")
    else:
        print("buku tidak ada di daftar pinjaman anda")
else:
    print("anda belum meminjam buku")
print(list_peminjaman)


