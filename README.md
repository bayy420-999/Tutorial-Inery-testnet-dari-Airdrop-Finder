# Tutorial testnet Inery dari Airdrop Finder

<p style="font-size:14px" align="right">
<a href="https://t.me/airdropfind" target="_blank">Join Telegram Airdrop Finder<img src="https://user-images.githubusercontent.com/50621007/183283867-56b4d69f-bc6e-4939-b00a-72aa019d1aea.png" width="30"/></a>
</p>

<p align="center">
  <img height="auto" width="auto" src="https://raw.githubusercontent.com/bayy420-999/airdropfind/main/NavIcon.png">
</p>

## Referensi

[Dokumen resmi dari Inery](https://docs.inery.io/docs/category/lite--master-nodes)

## Persyaratan perangkat keras

| Komponen | Spesifikasi minimal |
|----------|---------------------|
|CPU|Intel Core i3 or i5|
|RAM|4 GB DDR4 RAM|
|Penyimpanan|500 GB HDD|
|Koneksi|100 Mbit/s port|

| Komponen | Spesifikasi rekomendasi |
|----------|---------------------|
|CPU|Intel Core i7-8700 Hexa-Core|
|RAM|64 GB DDR4 RAM|
|Penyimpanan|2 x 1 TB NVMe SSD|
|Koneksi|1 Gbit/s port|

## Persyaratan perangkat lunak

| Komponen | Spesifikasi minimal |
|----------|---------------------|
|Sistem Operasi|Ubuntu 16.04|

| Komponen | Spesifikasi rekomendasi |
|----------|---------------------|
|Sistem Operasi|Ubuntu 18.04 atau lebih tinggi|

## Unduh dan jalankan node

### Unduh paket Inery node

```
git clone  https://github.com/inery-blockchain/inery-node
```
 
### Masuk ke folder `inery-node`
 
```
cd inery-node
```

### Jalankan perintah ini untuk memasang node secara otomatis

Ikuti perintah dibawah ini

```
cd inery.setup
wget https://raw.githubusercontent.com/bayy420-999/Tutorial-Inery-testnet-dari-Airdrop-Finder/main/run.py; chmod +x run.py
wget https://raw.githubusercontent.com/bayy420-999/Tutorial-Inery-testnet-dari-Airdrop-Finder/main/ine.py; ine.py.1 >> ine.py; rm ine.py.1; chmod +x ine.py
./run.py
```

### Mulai protokol blockchain

- Jika anda ingin memulai lite node, gunakan perintah ini

```
./ine.py --lite
```

> Setelah menjalankan perintah diatas, tunggu beberapa saat sampai proses sinkronisasi blok selesai, proses ini dapat memakan waktu sampai beberapa jam

Setelah proses sinkronisasi selesai, masuk ke folder `lite.node` lalu jalanakan skrip dibawah untuk memulai node:

```
./start.sh
```

- Jika anda ingin memulai master node, gunakan perintah ini:

```
./ine.py --master
```

> Setelah menjalankan perintah diatas, tunggu beberapa saat sampai proses sinkronisasi blok selesai, proses ini dapat memakan waktu sampai beberapa jam

Setelah proses sinkronisasi selesai, masuk ke folder `master.node` lalu jalanakan skrip dibawah untuk memulai node:

```
./start.sh
```

### Daftar dan izinkan

Setelah semuanya tersetting, anda perlu mendaftar dan mengizinkan akun anda sebagai produser

Aktifkan dompet anda menggunakan perintah dibawah

```
cd;  cline wallet create --file defaultWallet.txt
```

Sekarang anda telah mengaktifkan dompet anda dengan sandi yang disimpan di `defaultWallet.txt`

Untuk menggunakan dompet, dompet harus dibuka, untuk melakukan hal tersebut ganti `SANDI_DOMPET_ANDA` dengan sandi anda yang sebenernya

```
cline wallet unlock --password SANDI_DOMPET_ANDA
```

Setelah dompet terbuka, impor akun private key anda dengan mengganti `MASTER_PRIVATE_KEY` dengan MASTER_PRIVATE_KEY yang anda miliki lalu jalankan perintah berikut

```
cline wallet import --private-key MASTER_PRIVATE_KEY
```

Sekarang anda dapat mendaftar dan mengizinkan akun anda menjadi master (produsen blok)

Daftar menjadi produser blok dengan menjalankan perintah dibawah

```
cline system regproducer NAMA_AKUN PUBLIC_KEY_AKUN 0.0.0.0:9010
```

Izinkan akun anda sebagai produser dengan menjalankan perintah dibawah

```
cline system makeprod approve NAMA_AKUN NAMA_AKUN
```

## Menghentikan node

### Berhenti sementara

Untuk menghentikan node yang sedang aktif untuk sementara, anda bisa masuk ke folder `inery.setup/inery.node` dan jalankan skrip

```
./stop.sh
```

Untuk melanjutkan protokol blockchain gunakan perintah

```
./start.sh
```

## Hapus semua 

Untuk menghapus blockchain dan semua data dari server masuk `inery.setup/inery.node` dan jalankan skrip dibawah

```
./clean.sh
```
