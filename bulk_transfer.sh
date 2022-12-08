read -p "Masukan nama akun : " acc_name
read -p "Masukan jumlah token dan symbol, (contoh: 1.0 INR) : " token
read -p "Berikan pesan untuk penerima token : " msg

accounts=("inery" "bgpateng" "bayy421" "jisoo" "alfonova" "dexa" "jambul.inery" "riandwiyandi" "armz" "asphxwzrd" "away" "bintangnl" "blacktokyoo")

for account in ${accounts[@]}; do
    cline push action inery.token transfer \'[\"$acc_name\", \"$account\", \"$token\", \"$msg\"]\' -p $acc_name
done
