# Tutorial menyelesaikan tugas testnet inery dari Airdrop Finder

Tutorial ini akan di update jika terdapat tugas baru

Sebelum menyelesaikan tugas-tugas dibawah, pastikan bahwa anda sudah mendaftar di `testnet.inery.io` dan sudah menjalankan node

## Tugas 1: Master Approval

Untuk tugas ini, anda harus menjadi master node, untuk tutorial master node sudah dibahas sebelumnya

Jika sudah maka ikuti langkah-langkah berikut

1. Pergi ke `testnet.inery.io` lalu login 
2. Klik tombol `dashboard` maka anda akan diarahkan ke dashboard anda 
3. Scroll ke bawah sampe bagian `Tasks`
4. Disitu anda akan melihat `Master Approval` 
5. Klik `read more` 
6. Klik `Finish task`
7. Tunggu Paling Lama 1-7 Hari Hingga di Approve dan Akan Menerima 800 INR (Real) 

## Tugas 2: Make your own currency and transfer to someone

1. Buka dompet 
   ```
   cline wallet unlock --name NAMA_DOMPET --password KATA_SANDI_DOMPET
   ```
2. Buat ABI dan WASM
   ```
   cline get code inery.token -c token.wasm -a token.abi --wasm
   ``` 
3. Set kode akun

   ```
   cline set code -j NAMA_AKUN token.wasm
   cline set abi NAMA_AKUN token.abi
   ```
   
   - Ganti `NAMA_AKUN` dengan nama akun anda
   
4. Buat token baru
   ```
   cline push action inery.token create '["NAMA_AKUN", "SUPPLY_TOKEN SYMBOL"], "DESKRIPSI_TOKEN"' -p NAMA_AKUN
   ```

   - Ganti `NAMA_AKUN` dengan nama akun anda

   - Ganti `SUPPLY` dengan seberapa banyak supply token yang anda inginkan

   - Ganti `SYMBOL` dengan symbol yang anda inginkan

   - Ganti `DESKRIPSI_TOKEN` dengan deskripsi yang anda inginkan

5. Issue token

   ```
   cline push action inery.token issue '["NAMA_AKUN", "SUPPLY_TOKEN SYMBOL"], "DESKRIPSI_TOKEN"' -p NAMA_AKUN
   ```
   
   Isi seperti tadi

6. Kirim token

   Gunakan script dibawah untuk mengirim token secara otomatis

   ```
   wget https://raw.githubusercontent.com/bayy420-999/Tutorial-Inery-testnet-dari-Airdrop-Finder/main/bulk_transfer.py; chmod +x bulk_transfer.py
   ./bulk_transfer.py
   ```

7. Masuk ke `testnet.inery.io` dan buka dashboard kalian
8. Scroll sampe bawah dan klik `FINISH`
9. Tunggu hingga tugas dikonfirmasi