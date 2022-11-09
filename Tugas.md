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
   cline push action inery.token issue '["NAMA_AKUN", "SUPPLY_TOKEN SYMBOL", "DESKRIPSI_TOKEN"]' -p NAMA_AKUN
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

## Tugas 3: Create Your Value Contract

1. Unduh pake `inery.cdt`

   ```
   wget -qO crud.sh https://raw.githubusercontent.com/bangpateng/inery/main/crud.sh && chmod +x crud.sh && ./crud.sh
   ```

2. Ekspor path

   ```
   export PATH="$PATH:$HOME/inery.cdt/bin:$HOME/inery-node/inery/bin"
   ```

3. Buat folder

   ```
   mkdir -p $HOME/inrcrud
   ```

4. Tulis code

   ```
   sudo tee $HOME/inrcrud/inrcrud.cpp >/dev/null <<EOF
   #include <inery/inery.hpp>
   #include <inery/print.hpp>
   #include <string>
    
   using namespace inery;
    
   using std::string;
    
   class [[inery::contract]] inrcrud : public inery::contract {
     public:
       using inery::contract::contract;
    
    
           [[inery::action]] void create( uint64_t id, name user, string data ) {
               records recordstable( _self, id );
               auto existing = recordstable.find( id );
               check( existing == recordstable.end(), "record with that ID already exists" );
               check( data.size() <= 256, "data has more than 256 bytes" );
    
               recordstable.emplace( _self, [&]( auto& s ) {
                  s.id         = id;
                  s.owner      = user;
                  s.data       = data;
               });
    
               print( "Hello, ", name{user} );
               print( "Created with data: ", data );
           }
    
            [[inery::action]] void read( uint64_t id ) {
               records recordstable( _self, id );
               auto existing = recordstable.find( id );
               check( existing != recordstable.end(), "record with that ID does not exist" );
               const auto& st = *existing;
               print("Data: ", st.data);
           }
    
           [[inery::action]] void update( uint64_t id, string data ) {
               records recordstable( _self, id );
               auto st = recordstable.find( id );
               check( st != recordstable.end(), "record with that ID does not exist" );
    
    
               recordstable.modify( st, get_self(), [&]( auto& s ) {
                  s.data = data;
               });
    
               print("Data: ", data);
           }
    
               [[inery::action]] void destroy( uint64_t id ) {
               records recordstable( _self, id );
               auto existing = recordstable.find( id );
               check( existing != recordstable.end(), "record with that ID does not exist" );
               const auto& st = *existing;
    
               recordstable.erase( st );
    
               print("Record Destroyed: ", id);
    
           }
    
     private:
       struct [[inery::table]] record {
          uint64_t        id;
          name     owner;
          string          data;
          uint64_t primary_key()const { return id; }
       };
    
       typedef inery::multi_index<"records"_n, record> records;
    };
   EOF
   ```

5. Compile code

   ```
   inery-cpp $HOME/inrcrud/inrcrud.cpp -o $HOME/inrcrud/inrcrud.wasm
   ```

6. Buka dompet

   ```
   cline wallet unlock -n NAMA_DOMPET
   ```

7. Setting contract

   ```
   cline set contract NAMA_AKUN ./inrcrud
   ```

8. Buat contract

   ```
   cline push action NAMA_AKUN create '[1, "NAMA_AKUN", "My first Record"]' -p NAMA_AKUN --json
   ```

   > Simpan transaksi

9. Baca contract

   ```
   cline push action NAMA_AKUN read [1] -p NAMA_AKUN --json
   ```

10. Update contract

    ```
    cline push action NAMA_AKUN update '[ 1,  "My first Record Modified"]' -p NAMA_AKUN --json
    ```

11. Hancurkan contract 
    ```
    cline push action NAMA_AKUN destroy [1] -p NAMA_AKUN --json
    ```

12. Jika tidak ada error anda bisa klik `Finish task` di dashboard inery
