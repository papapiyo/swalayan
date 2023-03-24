# Self-Service Cashier
## Latar Belakang
Pemilik supermarket berencana untuk memperbaiki proses bisnis. Salah satu rencananya adalah membuat sistem kasir self-service di supermarket miliknya. Sehingga customer bisa langsung memasukkan item yang dibeli, jumlah item yang dibeli, dan harga item yang dibeli. 

## Tujuan
Membuat sistem kasir sederhana supaya customer dapat melakukan hal-hal berikut
* Memasukkan item yang akan dibeli
* Menambahkan item yang akan dibeli
* Memasukkan harga item yang akan dibeli
* Mengecek kembali daftar belanja sebelum melakukan pembayaran

## Feature Requirements
1. Customer input nama item, jumlah item, dan harga item `add_item()`
2. Jika ada kesalahan input, maka customer:
   * Update nama item `update_item_name()`
   * Update jumlah item `update_item_qty()`
   * Update harga item `update_item_price()`
3. Jika batal item belanjaan, maka customer:
   * Hapus salah satu item `delete_item()`
   * Langsung hapus transaksi/reset transaksi `reset_transaction()`
4. Jika sudah selesai, customer mengecek list belanja `check_order()`
5. Pembeli mengecek total harga `total_price()`

## Flowchart Self-Service Cashier
![image](https://user-images.githubusercontent.com/119731555/227449740-90fa0a65-7eda-4b9d-843f-5347db851e40.png)
| ID | Step Proses                | Deskripsi Proses                                                                 | Method                |
|----|----------------------------|----------------------------------------------------------------------------------|-----------------------|
| 0  | Start                      | Jalankan file main.py.                                                           |                       |
| 1  | Input order                | Pembeli melakukan input order. Ulangi sebanyak item yang akan dibeli.            | `add_item()`          |
| 2  | Cek order                  | Pembeli melakukan cek order.                                                     | `check_order()`       |
| 3  | Order sudah benar?         | Decision point, apakah order pembeli sudah benar?                                |                       |
| 4  | Update order               | Jika order belum benar, pembeli melakukan update order.                          | `update_item_name()`  |
|    |                            |                                                                                  | `update_item_qty()`   |
|    |                            |                                                                                  | `update_item_price()` |
| 5  | Batal item belanja?        | Decison point, apakah pembeli akan membatalkan item belanja?                     |                       |
| 6  | Batal semua item?          | Decison point, apakah pembeli akan membatalkan semua item belanja?               |                       |
| 7  | Batal semua item           | Pembeli membatalkan semua item.                                                  | `reset_transaction()` |
| 8  | Batal item                 | Pembeli membatalkan salah satu item.                                             | `delete_item()`       |
| 9  | Belanja selesai, cek order | Pembeli telah selesai berbelanja dan melakukan cek order                         | `check_order()`       |
| 10 | Total price + discount     | Pembeli melakukan pengecekan total harga dan mendapatkan diskon sesuai ketentuan | `total_price()`       |

## Penjelasan code
Program self-service cashier terdapat dua file program, main.py dan self_service_cashier.py.
File main.py merupakan file utama yang dijalan oleh user dengan command:

File self_service_cashier.py berisi modul Transaction yang di-import oleh file main.py.
Pada file self_service_cashier.py terdapat beberapa method, diantaranya adalah:
1. `add_item()`. Fungsi untuk memasukkan nama item, qty, dan harga.
2. `delete_item()`. Fungsi untuk hapus item.
3. `update_item_name()`. Fungsi untuk update nama item.
4. `update_item_qty()`. Fungsi untuk update qty item.
5. `update_item_price()`. Fungsi untuk update harga item.
6. `check_order()`. Fungsi untuk melakukan pengecekan barang yang di order.
7. `total_price()`. Fungsi untuk menghitung total harga (beserta diskon, bila eligible).
8. `reset_transaction()`. Fungsi untuk reset transaksi, hapus semua item belanja.

## Hasil test-case

## Conclusion/Future Work
Program Self-Service Cashier bisa dijalankan melalui terminal.
Kedepannya perlu dibangun database untuk menyimpan data transaksi setiap pembeli serta membangun GUI agar semakin user-friendly.
