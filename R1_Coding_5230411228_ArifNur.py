
class Pegawai:
    def __init__(self, NIK, nama, alamat):
        self.NIK = NIK
        self.nama = nama
        self.alamat = alamat

    def tampil_info(self):
        return f"NIK: {self.NIK}, Nama: {self.nama}, Alamat: {self.alamat}"

    def update_alamat(self, alamat_baru):
        self.alamat = alamat_baru

class Transaksi:
    def __init__(self, notransaksi, detailtransaksi):
        self.notransaksi = notransaksi
        self.detailtransaksi = detailtransaksi

    def tambah_detail(self, detail):
        self.detailtransaksi.append(detail)

    def tampil_detail(self):
        return f"No Transaksi: {self.notransaksi}, Detail: {self.detailtransaksi}"

class Struk:
    def __init__(self, notransaksi, namapegawai, namaproduk, jumlahproduk, totalharga):
        self.notransaksi = notransaksi
        self.namapegawai = namapegawai
        self.namaproduk = namaproduk
        self.jumlahproduk = jumlahproduk
        self.totalharga = totalharga

    def tampil_struk(self):
        return (f"Struk No: {self.notransaksi}, Pegawai: {self.namapegawai}, Produk: {self.namaproduk}, Jumlah: {self.jumlahproduk}, Total Harga: {self.totalharga}")

class Produk:
    def __init__(self, kodeproduk, namaproduk, jenisproduk, harga):
        self.kodeproduk = kodeproduk
        self.namaproduk = namaproduk
        self.jenisproduk = jenisproduk
        self.harga = harga

    def tampil_info_produk(self):
        return f"Kode: {self.kodeproduk}, Nama: {self.namaproduk}, Jenis: {self.jenisproduk}, Harga: {self.harga}"


snacks = [
    Produk("S001", "Cheetos", "Snack", 15000),
    Produk("S002", "Lays", "Snack", 12000),
    Produk("S003", "Pringles", "Snack", 20000),
    Produk("S004", "Oreo", "Snack", 18000),
    Produk("S005", "Tango", "Snack", 10000)
]

makanan = [
    Produk("M001", "Nasi Goreng", "Makanan", 25000),
    Produk("M002", "Sate Ayam", "Makanan", 30000),
    Produk("M003", "Mie Goreng", "Makanan", 20000),
    Produk("M004", "Ayam Penyet", "Makanan", 35000),
    Produk("M005", "Bakso", "Makanan", 22000)
]

minuman = [
    Produk("B001", "Coca Cola", "Minuman", 10000),
    Produk("B002", "Sprite", "Minuman", 10000),
    Produk("B003", "Teh Botol", "Minuman", 8000),
    Produk("B004", "Air Mineral", "Minuman", 5000),
    Produk("B005", "Jus Jeruk", "Minuman", 12000)
]
daftar_pegawai = []
daftar_transaksi = []

pegawai1 = Pegawai("001", "Joko", "Solo")
pegawai2 = Pegawai("002", "Bambang", "Bengkulu")
daftar_pegawai.append(pegawai1)
daftar_pegawai.append(pegawai2)

# Transaksi 1
transaksi1 = Transaksi(1, [])  # No transaksi 1
transaksi1.tambah_detail(snacks[0])  # Menambahkan Cheetos
transaksi1.tambah_detail(makanan[1])  # Menambahkan Sate Ayam
daftar_transaksi.append(transaksi1)

# Transaksi 2
transaksi2 = Transaksi(2, [])  # No transaksi 2
transaksi2.tambah_detail(minuman[2])  # Menambahkan Teh Botol
transaksi2.tambah_detail(makanan[3])  # Menambahkan Ayam Penyet
daftar_transaksi.append(transaksi2)

# Menambahkan jumlah produk pada transaksi
# Misalnya, untuk transaksi 1 kita beli 2 Cheetos dan 1 Sate Ayam
transaksi1.tambah_detail(Produk("S001", "Cheetos", "Snack", 15000 * 2))  # 2 Cheetos
transaksi1.tambah_detail(Produk("M002", "Sate Ayam", "Makanan", 30000 * 1))  # 1 Sate Ayam

# Untuk transaksi 2, kita bisa menambahkan jumlah juga
transaksi2.tambah_detail(Produk("B002", "Teh Botol", "Minuman", 8000 * 1))  # 1 Teh Botol
transaksi2.tambah_detail(Produk("M004", "Ayam Penyet", "Makanan", 35000 * 1))  # 1 Ayam Penyet

def TambahProduk():
    kodeproduk = input("Masukkan Kode Produk: ")
    namaproduk = input("Masukkan Nama Produk: ")
    jenisproduk = input("Masukkan Jenis Produk (Snack/Makanan/Minuman): ")
    harga = int(input("Masukkan Harga Produk: "))
    
    # Memeriksa jenis produk dan menambahkannya ke daftar yang sesuai
    if jenisproduk == "Snack":
        produk = Produk(kodeproduk, namaproduk, jenisproduk, harga)
        snacks.append(produk)
    elif jenisproduk == "Makanan":
        produk = Produk(kodeproduk, namaproduk, jenisproduk, harga)
        makanan.append(produk)
    elif jenisproduk == "Minuman":
        produk = Produk(kodeproduk, namaproduk, jenisproduk, harga)
        minuman.append(produk)
    else:
        print("Jenis produk tidak valid. Silakan masukkan Snack, Makanan, atau Minuman.")
        return
    print("Produk berhasil ditambahkan:")
    print(produk.tampil_info_produk())

# Fungsi untuk menghapus produk
def HapusProduk():
    kodeproduk = input("Masukkan Kode Produk yang ingin dihapus: ")
    for produk in snacks:
        if produk.kodeproduk == kodeproduk:
            snacks.remove(produk)
            print(f"Produk dengan Kode {kodeproduk} berhasil dihapus dari daftar Snacks.")
            return
    
    for produk in makanan:
        if produk.kodeproduk == kodeproduk:
            makanan.remove(produk)
            print(f"Produk dengan Kode {kodeproduk} berhasil dihapus dari daftar Makanan.")
            return
    
    for produk in minuman:
        if produk.kodeproduk == kodeproduk:
            minuman.remove(produk)
            print(f"Produk dengan Kode {kodeproduk} berhasil dihapus dari daftar Minuman.")
            return
    
    print(f"Produk dengan Kode {kodeproduk} tidak ditemukan.")



def RekrutPegawai():
    NIK = input("Masukkan NIK Pegawai: ")
    nama = input("Masukkan Nama Pegawai: ")
    alamat = input("Masukkan Alamat Pegawai: ")
    pegawai = Pegawai(NIK, nama, alamat)
    daftar_pegawai.append(pegawai) 
    print("Pegawai berhasil direkrut:")
    print(pegawai.tampil_info())

# Fungsi untuk memecat pegawai
def PecatPegawai():
    NIK = input("Masukkan NIK Pegawai yang ingin dipecat: ")
    for pegawai in daftar_pegawai:
        if pegawai.NIK == NIK:
            daftar_pegawai.remove(pegawai)
            print(f"Pegawai dengan NIK {NIK} berhasil dipecat.")
            return
    print(f"Pegawai dengan NIK {NIK} tidak ditemukan.")

# Fungsi untuk mencetak struk
def CetakStruk():
    notransaksi = input("Masukkan No Transaksi yang ingin dicetak: ")
    for transaksi in daftar_transaksi:
        if transaksi.notransaksi == notransaksi:
            print("Struk berhasil ditemukan:")
            print("=" * 70)
            print(f"{'No Transaksi':<15} {'Pegawai':<20} {'Produk':<20} {'Jumlah':<10} {'Total Harga':<10}")
            print("=" * 70)
            total_harga = 0
            for detail in transaksi.detailtransaksi:
                # Menghitung total harga
                total_harga += detail.harga
                print(f"{transaksi.notransaksi:<15} {detail.namaproduk:<20} {detail.jenisproduk:<20} 1 {detail.harga:<10}")
            print("=" * 70)
            print(f"{'Total':<55} {total_harga:<10}")
            return
    
    print(f"Transaksi dengan No {notransaksi} tidak ditemukan.")

def BuatTransaksi():
    notransaksi = input("Masukkan No Transaksi: ")
    detailtransaksi = []
    
    while True:
        print("Pilih produk yang ingin ditambahkan:")
        print("1. Snack")
        print("2. Makanan")
        print("3. Minuman")
        print("4. Selesai")
        pilihan = int(input("Pilih Menu: "))
        
        if pilihan == 1:
            for snack in snacks:
                print(snack.tampil_info_produk())
            kodeproduk = input("Masukkan Kode Produk Snack: ")
            for snack in snacks:
                if snack.kodeproduk == kodeproduk:
                    detailtransaksi.append(snack)
                    print(f"{snack.namaproduk} berhasil ditambahkan ke transaksi.")
                    break
            else:
                print("Kode produk tidak ditemukan.")
        
        elif pilihan == 2:
            for makanan_item in makanan:
                print(makanan_item.tampil_info_produk())
            kodeproduk = input("Masukkan Kode Produk Makanan: ")
            for makanan_item in makanan:
                if makanan_item.kodeproduk == kodeproduk:
                    detailtransaksi.append(makanan_item)
                    print(f"{makanan_item.namaproduk} berhasil ditambahkan ke transaksi.")
                    break
            else:
                print("Kode produk tidak ditemukan.")

        elif pilihan == 3:
            for minuman_item in minuman:
                print(minuman_item.tampil_info_produk())
            kodeproduk = input("Masukkan Kode Produk Minuman: ")
            for minuman_item in minuman:
                if minuman_item.kodeproduk == kodeproduk:
                    detailtransaksi.append(minuman_item)
                    print(f"{minuman_item.namaproduk} berhasil ditambahkan ke transaksi.")
                    break
            else:
                print("Kode produk tidak ditemukan.")

        elif pilihan == 4:
            break
        
        else:
            print("Pilihan tidak valid. Silakan pilih lagi.")

    transaksi = Transaksi(notransaksi, detailtransaksi)
    daftar_transaksi.append(transaksi)
    print("Transaksi berhasil dibuat.")


def main():
    while True :
        print(" ")
        print("-----------------------------------------")
        print("=   =   =   = Data Toko A =   =   =   =") 
        print("1. Produk")
        print("2. Pegawai")
        print("3. Transaksi")
        print("4. Keluar")
        print("----------------------------------------")
        print(" ")
        pilih = int(input("Pilih Menu : "))
        if pilih == 1 :
            print(" ")
            print("1. Tampil Daftar Produk")
            print("2. Tambah Produk")
            print("3. Hapus Produk")
            print(" ")
            pilih2 = int(input("Pilih Menu Produk : "))
            if pilih2 == 1 :
                print("=   =   =   = Daftar Produk =   =   =   =")
                print(f"{'Jenis Produk':<15} {'Kode Produk':<15} {'Nama Produk':<20} {'Harga':<10}")
                print("=" * 60)
                for snack in snacks:
                    print(f"{snack.jenisproduk:<15} {snack.kodeproduk:<15} {snack.namaproduk:<20} {snack.harga:<10}")
                for makanan_item in makanan:
                    print(f"{makanan_item.jenisproduk:<15} {makanan_item.kodeproduk:<15} {makanan_item.namaproduk:<20} {makanan_item.harga:<10}")
                for minuman_item in minuman:
                    print(f"{minuman_item.jenisproduk:<15} {minuman_item.kodeproduk:<15} {minuman_item.namaproduk:<20} {minuman_item.harga:<10}")


            elif pilih2 == 2 :
                TambahProduk()

            elif pilih2 == 3 :
                HapusProduk()    

            else :
                print("Error")


        elif pilih == 2 :
            print(" ")
            print("1. Tampil Daftar Pegawai")
            print("2. Rekrut Pegawai")
            print("3. Pecat Pegawai")
            print("---------------------------")
            print(" ")
            pilih2 = int(input("Pilih Menu Pegawai: "))
            if pilih2 == 1:
                #Tampilkan Daftar Pegawai
                print("=   =   =   = Daftar Pegawai =   =   =   =")
                print(f"{'NIK':<15} {'Nama':<20} {'Alamat':<30}")
                print("=" * 65)
                for pegawai in daftar_pegawai:
                    print(f"{pegawai.NIK:<15} {pegawai.nama:<20} {pegawai.alamat:<30}")

            elif pilih2 == 2:
                RekrutPegawai()

            elif pilih2 == 3 :
                PecatPegawai()        

            else:
                print("Error")    

        elif pilih == 3 :
            print(" ")
            print("1. Riwayat Transaksi")
            print("2. Cetak Struk")
            print("3. Buat Transaksi")
            print("4. Hapus Transaksi")
            print("-----------------------")
            print(" ")
            pilih2 = int(input("Pilih Menu Transaksi : "))
            if pilih2 == 1 :
                print("=   =   =   = Riwayat Transaksi =   =   =   =")
                print(f"{'No Transaksi':<15} {'Jenis Barang':<20}")
                print("=" * 35)
                for transaksi in daftar_transaksi:
                    jenis_barang = ', '.join([produk.jenisproduk for produk in transaksi.detailtransaksi])  # Ambil jenis barang dari detail transaksi
                    print(f"{transaksi.notransaksi:<15} {jenis_barang:<20}")
            elif pilih2 == 2 :
                CetakStruk()

            elif pilih2 == 3 :  
                BuatTransaksi()

            elif pilih2 == 4:
                notransaksi = input("Masukkan No Transaksi yang ingin dihapus: ")
                for transaksi in daftar_transaksi:
                    if transaksi.notransaksi == notransaksi:
                        daftar_transaksi.remove(transaksi)
                        print(f"Transaksi dengan No {notransaksi} berhasil dihapus.")
                        break  # Menggunakan break untuk keluar dari loop
                    else:
                     print(f"Transaksi dengan No {notransaksi} tidak ditemukan.")

            else : 
                print("Error")

        elif pilih == 4 :
            break

        else :
            print("Maaf,Menu Tidak Tersedia")

main()            
