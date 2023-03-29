class Transaction:
    """
    Kelas Transaction digunakan untuk melakukan transaksi pembelian dengan item-info berupa list yang terdiri dari 
    nama item, jumlah item, dan harga item.

    Metode yang tersedia:
    - add_item(item_info): Menambahkan item baru ke dalam daftar transaksi.
    - delete_item(name): Menghapus item dari daftar transaksi berdasarkan nama item.
    - update_item_name(name, update_name): Mengubah nama item pada daftar transaksi.
    - update_item_qty(name, update_qty): Mengubah jumlah item pada daftar transaksi.
    - update_item_price(name, update_price): Mengubah harga item pada daftar transaksi.
    - check_order(): Menampilkan seluruh daftar transaksi beserta total harga.
    - total_price(): Menghitung total harga dan diskon yang didapat, kemudian menampilkannya.
    - reset_transaction(): Menghapus seluruh item dari daftar transaksi.

    Atribut:
    - order_list (dict): dictionary yang menyimpan seluruh item pada daftar transaksi. 
                         Key: nama item (string)
                         Value: list berisi jumlah item (int) dan harga item (float)
    """

    def __init__(self):
        """
        Inisialisasi Transaction dengan membuat order_list kosong.
        """
        self.order_list = {}

    def add_item(self, item_info):
        """
        Menambahkan item baru ke dalam daftar transaksi.

        Parameter:
        - item_info (list): list yang terdiri dari nama item (string), jumlah item (int), dan harga item (float).

        Output:
        - Tidak ada output yang dihasilkan.
        """
        try:
            name, qty, price = item_info
            if name not in self.order_list:
                self.order_list[name] = [qty, price]
            else:
                self.order_list[name][0] += qty
        except ValueError:
            print("Input data harus berisi nama item, jumlah item, dan harga item dalam format [nama, jumlah, harga]")

    def delete_item(self, name):
        """
        Menghapus item dari daftar transaksi berdasarkan nama item.

        Parameter:
        - name (string): nama item yang ingin dihapus.

        Output:
        - Tidak ada output yang dihasilkan.
        """
        try:
            del self.order_list[name]
        except KeyError:
            print(f"Item {name} tidak ditemukan dalam transaksi")

    def update_item_name(self, name, update_name):
        """
        Mengubah nama item pada daftar transaksi.

        Parameter:
        - name (string): nama item yang ingin diubah.
        - update_name (string): nama baru yang ingin diberikan.

        Output:
        - Tidak ada output yang dihasilkan.
        """
        try:
            self.order_list[update_name] = self.order_list.pop(name)
        except KeyError:
            print(f"Item {name} tidak ditemukan dalam transaksi")

    def update_item_qty(self, name, update_qty):
        """
        Mengubah jumlah item pada daftar transaksi.

        Parameter:
        - name (string): nama item yang ingin diubah.
        - update_qty (int): jumlah baru yang ingin diberikan.

        Output:
        - Tidak ada output yang dihasilkan.
        """
        try:
            self.order_list[name][0] = update_qty
        except KeyError:
            print(f"Item {name} tidak ditemukan dalam transaksi")

    def update_item_price(self, name, update_price):
        """
        Mengubah harga item pada daftar transaksi.

        Parameter:
        - self (Transaction): instance dari kelas Transaction.
        - name (string): nama item yang ingin diubah.
        - update_price (int): harga baru yang ingin diberikan.

        Output:
        - Tidak ada output yang dihasilkan.
        """
        try:
            self.order_list[name][1] = update_price
        except KeyError:
            print(f"Item {name} tidak ditemukan dalam transaksi")

    def check_order(self):
        """
        Mengecek daftar item yang telah dibeli dan total harga.

        Parameter:
        - self (Transaction): instance dari kelas Transaction.

        Output:
        - total_price (int): total harga semua item yang dibeli.
        """
        if not self.order_list:
            print("Belum ada item yang dibeli")
        else:
            print("Item yang dibeli adalah:")
            print("| No | Nama item | Jumlah item | Harga/item | Total harga |")
            print("-" * 65)
            total_price = 0
            for index, (name, item_info) in enumerate(self.order_list.items(), start=1):
                qty, price = item_info
                total = qty * price
                print(f"| {index:<2} | {name:<9} | {qty:<11} | {price:>10,.0f} | {total:>11,.0f} |")
                total_price += total
            print("-" * 65)
            return total_price

    def total_price(self):
        """
        Menghitung total harga yang harus dibayar dan mengeluarkan diskon jika diperlukan.

        Parameter:
        - self (Transaction): instance dari kelas Transaction.

        Output:
        - Tidak ada output yang dihasilkan.
        """
        total_price = self.check_order()
        if total_price:
            discount = 0
            if total_price > 500000:
                discount = 0.1
            elif total_price > 300000:
                discount = 0.08
            elif total_price > 200000:
                discount = 0.05

            discounted_price = total_price - (total_price * discount)
            print(f"Total belanja yang harus dibayarkan adalah {discounted_price:,.0f}")


    def reset_transaction(self):
        """
        Menghapus semua item pada daftar transaksi.

        Parameter:
        - self (Transaction): instance dari kelas Transaction.

        Output:
        - Tidak ada output yang dihasilkan.
        """
        self.order_list = {}
        print("Semua item berhasil dihapus!")

