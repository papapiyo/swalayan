from self_service_cashier import Transaction

def main():
    print("Selamat datang di Kasir Self-Service")
    print("Silakan masukkan item belanjaan anda!")
    transaksi = Transaction()
    while True:
        print("==========================================")
        print("1. Tambah item belanjaan")
        print("2. Hapus item belanjaan")
        print("3. Reset transaksi")
        print("4. Cek pesanan")
        print("5. Hitung total harga")
        print("6. Update item name")
        print("7. Update item qty")
        print("8. Update item price")
        print("9. Keluar")
        print("==========================================")
        try:
            pilihan = int(input("Masukkan pilihan anda: "))
            if pilihan == 1:
                nama_item = input("Masukkan nama item: ")
                qty = int(input("Masukkan jumlah item: "))
                harga = int(input("Masukkan harga per item: "))
                transaksi.add_item([nama_item, qty, harga])
            elif pilihan == 2:
                nama_item = input("Masukkan nama item yang ingin dihapus: ")
                transaksi.delete_item(nama_item)
            elif pilihan == 3:
                transaksi.reset_transaction()
                print("Semua item berhasil dihapus!")
            elif pilihan == 4:
                transaksi.check_order()
            elif pilihan == 5:
                transaksi.total_price()
            elif pilihan == 6:
                nama_item_lama = input("Masukkan nama item yang ingin diupdate: ")
                nama_item_baru = input("Masukkan nama item yang baru: ")
                transaksi.update_item_name(nama_item_lama, nama_item_baru)
            elif pilihan == 7:
                nama_item = input("Masukkan nama item yang ingin diupdate: ")
                qty_baru = int(input("Masukkan jumlah item yang baru: "))
                transaksi.update_item_qty(nama_item, qty_baru)
            elif pilihan == 8:
                nama_item = input("Masukkan nama item yang ingin diupdate: ")
                harga_baru = int(input("Masukkan harga per item yang baru: "))
                transaksi.update_item_price(nama_item, harga_baru)
            elif pilihan == 9:
                print("Terima kasih telah berbelanja!")
                break
            else:
                print("Maaf, pilihan yang anda masukkan tidak valid. Silahkan coba lagi!")
        except ValueError:
            print("Maaf, pilihan yang anda masukkan tidak valid. Silahkan coba lagi!")
        except Exception as e:
            print(e)

if __name__ == "__main__":
    main()
