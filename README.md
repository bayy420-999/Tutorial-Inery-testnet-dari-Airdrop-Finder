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

## Mendaftar di `testnet.inery.io`

Sebelum mengikuti testnet anda harus mendaftar akun di [sini](https://testnet.inery.io)

Langkah-langkah:

1. Klik link diatas

2. Klik strip 3 di pojok kanan halaman

3. Klik `sign up`

   Selanjutnya anda harus mengisi beberapa informasi dibawah

   | Informasi | Keterangan |
   |-----------|------------|
   |Server Name|Isi dengan alamat server anda, untuk lebih lengkapnya akan saya tulis dibawah|
   |IP Address|Isi dengan alamat ip yang dipake untuk login server/vps|
   |Account Name|Isi bebas, panjang maxsimal 13 karakter dan tidak boleh menggunakan karakter diluar karakter `.12345abcdefghijklmnopqrstuvwxyz`|
   |Password|Isi dengan password|
   |Confirm Password|Isi dengan password yang tadi|

4. Setelah semua informasi terisi klik tombol `create`

5. Simpan `Secret phrase`

6. Masukan `Secret phrase` yang tadi disimpan lalu klik tombol `next`

### Mengetahui Server Name

- Jika anda menggunakan VPS dari Digital Ocean maka Serber Name sama dengan Alamat IP

- Jika anda menggunakan VPS dari Contabo maka ikuti langkah berikut untuk mendapatkan Server Name

  1. Buka akun Contabo anda

  2. Pilih `Reverse DNS Management`

  3. Cari Alamat IP kalian dan salin link PTR Recordnya, itu adalah Server Name anda

- Jika anda menggunakan VPS dari Azure maka Server Name sama dengan Alamat IP publik

## Unduh dan jalankan node

### Unduh paket Inery node

```
git clone  https://github.com/inery-blockchain/inery-node
```
 
### Masuk ke folder `inery-node/inery.setup`
 
```
cd inery-node/inery.setup
```

### Jalankan perintah ini untuk memasang node secara otomatis

Jalankan perintah dibawah ini untuk menyunting file `ine.py` (terdapat beberapa kesalahan ketik dan paket dependesi yang perlu diubah)

```
rm ine.py
wget https://raw.githubusercontent.com/bayy420-999/Tutorial-Inery-testnet-dari-Airdrop-Finder/main/run.py; chmod +x run.py
wget https://raw.githubusercontent.com/bayy420-999/Tutorial-Inery-testnet-dari-Airdrop-Finder/main/ine.py; chmod +x ine.py
```

Lalu jalankan perintah dibawah untuk memasang dependesi dan setting node

```
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

> Untuk menjadi master node anda harus memiliki minimal 50000 INE testnet token, anda bisa pergi ke halaman [dashboard](https://testnet.inery.io/dashboard/) dan klaim 50000 INE faucet

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

### Menghentikan node

- Berhenti sementara

Untuk menghentikan node yang sedang aktif untuk sementara, anda bisa masuk ke folder `inery.setup/inery.node` dan jalankan skrip

```
./stop.sh
```

Untuk melanjutkan protokol blockchain gunakan perintah

```
./start.sh
```

### Hapus semua 

Untuk menghapus blockchain dan semua data dari server masuk `inery.setup/inery.node` dan jalankan skrip dibawah

```
./clean.sh
```

## Tugas-tugas testnet

Untuk bagian ini akan saya masukan [kesini](https://github.com/bayy420-999/Tutorial-Inery-testnet-dari-Airdrop-Finder/blob/main/Tugas.md)

## Update Inery-node

Karena ada beberapa binaries yang di update oleh dev Inery jadi kita perlu update nodenya

Ikuti langkah-langkah berikut

* Hentikan node
  ```console
  cd $HOME/inery-node/inery.setup/master.node
  ./stop.sh
  ```
  Cek apakah node sudah berhenti
  ```console
  pidof nodine
  ```

* Hapus Inery node
  ```console
  cd $HOME
  rm -rf inery-node
  ```

* Download Inery node versi terbaru
  ```console
   git clone  https://github.com/inery-blockchain/inery-node
  ```

* Masuk ke folder `inery.setup`
  ```console
   cd inery-node/inery.setup
  ```

* Ubah `ine.py` menjadi executable
  ```console
  chmod +x ine.py
  ```

* Export path
  ```console
  ./ine.py --export
  ```

* Load path
  ```console
  source $HOME/.bashrc
  ```

* Ubah konfigurasi
  ```console
  nano tools/config.json
  ```
  Cari `MASTER_ACCOUNT` lalu ubah value seperti berikut
  | Informasi | Keterangan |
  |-----------|------------|
  |NAME|Isi dengan nama akun anda|
  |PUBLIC_KEY|Isi dengan public key anda|
  |PRIVATE_KEY|Isi dengan private key anda|
  |PEER_ADDRESS|Di bagian IP ganti dengan IP VPS anda|

  Lalu simpan konfigurasi dengan menekan <kbd>CTRL</kbd>+<kbd>x</kbd>+<kbd>y</kbd>

* Jalankan node
  ```console
  ./ine.py --master
  ```

* Cek log node
  ```console
  tail -f master.node/blockchain/nodine.log
  ```

Jika node sudah tersinkronisasi jalankan script `start.sh`
```console
./master.node/start.sh
```

Lalu daftar menjadi produser blok

* Daftarkan akun menjadi produser
  ```console
  cline master bind <NAMA_AKUN> <PUBLIC_KEY_AKUN> <IP_VPS>:9010
  ```

  Hapus `<>` dan ganti sesuai petunjuk

  Jika terjadi error `wallet not unlocked` maka anda harus membuka dompet dulu

  ```console
  cline wallet unlock -n <NAMA_DOMPET> -p <PASSWORD_DOMPET>
  ```

* Izinkan akun sebagai produser
  ```console
  cline approve <NAMA_AKUN>
  ```

  Jika terjadi error `unable to find key` maka anda harus claim faucet lagi, lalu ulangi perintah diatas 

* Cek apakah akun sudah memproduksi blok
  ```console
  cline get account <NAMA_AKUN>
  ```

  Jika muncul seperti ini di terminal maka artinya akun telah memproduksi blok

  ```console
  created: 2022-11-29T09:59:25.500
  permissions:
       owner     1:    1 INE76WN7KvNS35HCXjCVUGUwoh2217KgAZpsD4eu6vM9CYFbkJWLo
          active     1:    1 INE76WN7KvNS35HCXjCVUGUwoh2217KgAZpsD4eu6vM9CYFbkJWLo
  memory:
       quota:     1.001 MiB    used:     5.062 KiB
  
  net bandwidth:
       staked:          1.0000 INR           (total stake delegated from account to self)
       delegated:       2.0000 INR           (total staked delegated to account from others)                                                                                           used:             3.026 KiB
       available:        32.32 GiB                                                             limit:            32.32 GiB                                                                                                                                                cpu bandwidth:
       staked:          1.0000 INR           (total stake delegated from account to self)
       delegated:       2.0000 INR           (total staked delegated to account from others)
       used:             27.15 ms
       available:        1.839 hr                                                              limit:            1.839 hr

  INR balances:
       liquid:        50000.0000 INR
       staked:            2.0000 INR
       unstaking:         0.0000 INR
       total:         50002.0000 INR                                                      
  producers:
       <NAMA_AKUNMU>
  ```


## Perintah berguna

### Mengecek log

```
tail -f blockchain/nodine.log
```

> pastikan anda sudah berada di folder `master.node` atau `lite.node`

### Mengecek informasi blockchain

```
cline get info
```

### Mengecek informasi akun

```
cline get account NAMA_AKUN_YANG_INGIN_DICEK
```

### Mengecek transaksi dari blockchain

```
 cline get transaction TX_ID
```

### Membuat dompet baru

```
cline wallet create --name NAMA_DOMPET --file NAMA_FILE.txt
```

> Salin sandi anda ke tempat yang aman, karena ada bug yang mengakibatkan sandi didalam file .txt hilang, yang mengakibatkan dompet tidak dapat dibuka

### Membuka dompet yang terkunci

```
cline wallet unlock --name NAMA_DOMPET --password KATA_SANDI_DOMPET
```

### Membuka dompet yang sudah terbuka

```
cline wallet open --name NAMA_DOMPET
```

### Mengimpor private key

```
cline wallet import --name NAMA_DOMPET --private-key PRIVATE_KEY
```

> Sebelum mengimpor private key, pastikan bahwa dompet yang anda gunakan sudah terbuka

### Melihat list dompet

```
cline wallet list
```

> `*` pada dompet menandakan bahwa dompet terbuka

### Melihat public key dari dompet yang terbuka

```
cline wallet keys
```

### Melihat private key dari dompet yang terbuka

```
 cline wallet private_keys --name NAMA_DOMPET --password KATA_SANDI_DOMPET
```

### Transfer token

```
 cline transfer ALAMAT_PENGIRIM ALAMAT_PENERIMA JUMLAH_YANG_AKAN_DITRANSFER
```


## Troubleshoot

Ada beberapa masalah yang mungkin timbul saat proses pemasangan dan menhjalankan node, di bagian ini saya akan memberikan solusi dari masalah-masalah tersebut

### Saya lupa kata sandi dompet saya, bagaimana saya membuka dompet saya

Jika anda lupa kata sandi dompet anda, maka dompet anda tidak akan bisa dibuka kembali. Solusinya adalah membuat dompet baru dan memasukan `private key` yang sama seperti sebelumnya

Untuk cara membuat dompet baru bisa anda lihat di bagian `Perintah berguna`, kali ini jangan lupa untuk menyimpan sandi anda

### FileNotFoundError: [Errno 2] No such file or directory: './blockchain/config/config.ini'

Jika pesan error ini muncul kemungkinan karena `libssl 1.1` tidak terpasang di server anda, untuk memasangnya silahkan gunakan perintah dibawah

```
wget http://nz2.archive.ubuntu.com/ubuntu/pool/main/o/openssl/libssl1.1_1.1.1f-1ubuntu2.16_amd64.deb
sudo dpkg -i libssl1.1_1.1.1f-1ubuntu2.16_amd64.deb
```

### net_plugin::plugin_startup failed to bind to port 9010

Jika pesan error ini muncul maka penyebabnya karena `nodine` masinh berjalan di latar belakang, solusinya adalah mematikan `nodine`. Anda bisa menggunakan perintah dibawah untuk mematikan `nodine`

```
pidkill nodine
```

Untuk memastikan bahwa `nodine` sudah berhenti, anda bisa menggunakan perintah ini

```
pidof nodine
```

Setelah memastikan `nodine` benar-benar berhenti, anda dapat menjalankan node lagi
