# Swalayan ~ Self-Service Cashier

## Latar Belakang

Pemilik supermarket berencana untuk memperbaiki proses bisnis. Salah satu rencananya adalah membuat sistem kasir self-service di supermarket miliknya. Sehingga customer bisa langsung memasukkan item yang dibeli, jumlah item yang dibeli, dan harga item yang dibeli. 
Program ini dinamakan dengan `swalayan`. Menurut [KBBI](https://kbbi.kemdikbud.go.id/entri/swalayan), swalayan adalah 'pelayanan sendiri oleh pembeli karena perusahaan tidak menyediakan pramuniaga'.

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
| ID | Step Proses                | Deskripsi Proses                                                                  | Method                |
|----|----------------------------|-----------------------------------------------------------------------------------|-----------------------|
| 0  | Start                      | Jalankan file main.py.                                                            |                       |
| 1  | Input order                | Pembeli melakukan input order. Ulangi sebanyak item yang akan dibeli.             | `add_item()`          |
| 2  | Cek order                  | Pembeli melakukan cek order.                                                      | `check_order()`       |
| 3  | Order sudah benar?         | Decision point, apakah order pembeli sudah benar?                                 |                       |
| 4  | Update order               | Jika order belum benar, pembeli melakukan update order.                           | `update_item_name()`  |
|    |                            |                                                                                   | `update_item_qty()`   |
|    |                            |                                                                                   | `update_item_price()` |
| 5  | Batal item belanja?        | Decison point, apakah pembeli akan membatalkan item belanja?                      |                       |
| 6  | Batal semua item?          | Decison point, apakah pembeli akan membatalkan semua item belanja?                |                       |
| 7  | Batal semua item           | Pembeli membatalkan semua item.                                                   | `reset_transaction()` |
| 8  | Batal item                 | Pembeli membatalkan salah satu item.                                              | `delete_item()`       |
| 9  | Belanja selesai, cek order | Pembeli telah selesai berbelanja dan melakukan cek order.                         | `check_order()`       |
| 10 | Total price + discount     | Pembeli melakukan pengecekan total harga dan mendapatkan diskon sesuai ketentuan. | `total_price()`       |

## Penjelasan code

Program self-service cashier terdapat dua file program, main.py dan self_service_cashier.py.
File main.py merupakan file utama yang dijalankan oleh user dengan command: `python main.py`

![image](https://user-images.githubusercontent.com/119731555/227688906-3d7e2f4d-101b-443e-9da0-8b0b4c1fde9f.png)



File self_service_cashier.py berisi modul Transaction yang di-import oleh file main.py.
Pada file self_service_cashier.py terdapat beberapa method, diantaranya adalah:
1. `add_item()`. Fungsi untuk memasukkan nama item, qty, dan harga.
![image](https://user-images.githubusercontent.com/119731555/227688924-206ddd60-bf9d-42ba-a594-a547119a3134.png)

2. `delete_item()`. Fungsi untuk hapus item.
![image](https://user-images.githubusercontent.com/119731555/227688942-1bd4e9e8-8eff-4421-9823-67863fe26865.png)

3. `update_item_name()`. Fungsi untuk update nama item.
![image](https://user-images.githubusercontent.com/119731555/227688956-045bb17f-ff3e-4766-857c-91d97e515fbe.png)

4. `update_item_qty()`. Fungsi untuk update qty item.
![image](https://user-images.githubusercontent.com/119731555/227688974-12bf4118-f78b-456e-8fd9-1f076e18c9bf.png)

5. `update_item_price()`. Fungsi untuk update harga item.
![image](https://user-images.githubusercontent.com/119731555/227688995-8254496a-00b1-4471-8820-d0bf79f41437.png)

6. `check_order()`. Fungsi untuk melakukan pengecekan barang yang di order.
![image](https://user-images.githubusercontent.com/119731555/227689014-f8331e02-be9c-414b-89f0-c8827b7d8638.png)

7. `total_price()`. Fungsi untuk menghitung total harga (beserta diskon, bila eligible).
![image](https://user-images.githubusercontent.com/119731555/227689032-42f5142d-d602-43c3-853a-cc3dc0a4025e.png)

8. `reset_transaction()`. Fungsi untuk reset transaksi, hapus semua item belanja.
![image](https://user-images.githubusercontent.com/119731555/227689039-146b07e4-3e93-4f5d-bf90-219ed234b0a6.png)


## Hasil test-case
1. Buka terminal dan jalankan file main.py.

![image](https://user-images.githubusercontent.com/119731555/227689230-690b1250-6b5a-471e-b24f-72f81942f799.png)


2. Input 1 untuk tambah item belanjaan.

![image](https://user-images.githubusercontent.com/119731555/227689337-387d9dfc-a950-49a3-a5d0-1d42c1e4dacf.png)
![image](https://user-images.githubusercontent.com/119731555/227689358-9521c936-d78c-4268-9c16-5ce2514ff13f.png)


3. Input 4 untuk cek pesanan.

![image](https://user-images.githubusercontent.com/119731555/227689388-e9ef7abd-c2d4-431c-9943-7d94fb0811d5.png)


4. Input 2 untuk hapus item belanjaan.

![image](https://user-images.githubusercontent.com/119731555/227689452-b8e30cdf-4d2c-4021-8dd1-95effd52ff34.png)
![image](https://user-images.githubusercontent.com/119731555/227689466-95eb1e8d-230f-447f-b397-2f3a7fe9fc8c.png)


5. Input 3 untuk reset transaksi.

![image](https://user-images.githubusercontent.com/119731555/227689495-8b944466-602e-477d-904b-4b879b487933.png)
![image](https://user-images.githubusercontent.com/119731555/227689508-014c11f0-dd04-484d-836c-e32b3047f136.png)


6. Pembeli melakukan pembelian kembali.

![image](https://user-images.githubusercontent.com/119731555/227689613-28b6caf6-e3b8-422e-824f-e63951e9aa8e.png)
![image](https://user-images.githubusercontent.com/119731555/227689628-c204cd32-ed05-48b5-8b45-d55f29cf902f.png)


7. Input 5 untuk menghitung total harga.

![image](https://user-images.githubusercontent.com/119731555/227689701-918929fb-ab2d-4f2a-a5b2-6e776e2125d3.png)



## Conclusion/Future Work

Program Self-Service Cashier bisa dijalankan melalui terminal.

Kedepannya perlu dibangun database harga untuk menghindari fraud serta untuk menyimpan data transaksi setiap pembeli. 
Perlu membangun GUI agar semakin user-friendly.
