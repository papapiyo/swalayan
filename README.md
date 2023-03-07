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
1. Customer membuat ID transaksi
2. Customer input nama item, jumlah item, dan harga item
3. Jika ada kesalahan input, maka customer:
  * Update nama item update_item_name()
  * Update jumlah item
  * Update harga item
4. Jika batal item belanjaan, maka customer:
  * Hapus salah satu item
  * Langsung hapus transaksi/reset transaksi
5. Jika sudah selesai, customer mengecek list belanja
6. Jika sudah benar, maka terdapat pesan **"Pemesanan sudah benar"**
7. Jika belum benar, maka terdpat pesan **"Terdapat kesalahan input data"**
![Self Service Cashier](https://user-images.githubusercontent.com/119731555/223314509-c83aaac9-b662-45fe-9f3d-c82eec6827e5.png)
