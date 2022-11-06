#!/usr/bin/python3
import os, inquirer

if __name__ == '__main__':
    os.system('clear')

    q = [
        inquirer.Text(
            'acc_name',
            message = 'Masukan nama akun anda',
            validate = lambda _, x: x != '',
        ),
        inquirer.Text(
            'token',
            message = 'Masukan jumlah token dan symbol, contoh: 1.0 INR',
            validate = lambda _, x: x != '',
        ),
        inquirer.Text(
            'msg',
            message = 'Masukan pesan yang ingin diberikan kepada si penerima token',
            validate = lambda _, x: x != '',
        )
    ]
    
    a = inquirer.prompt(q)
    acc_name = a.get('acc_name')
    token = a.get('token')
    msg = a.get('msg')

    l = ['inery', 'bgpateng', 'jisoo', 'alfonova', 'dexa', 'jambul.inery', 'riandwiyandi', 'armz', 'asphxwzrd', 'away', 'bintangnl', 'blacktokyoo']
    s = 'cline push action inery.token transfer' 
    for n in l:
        os.system(s, f"'[\"{acc_name}\", \"{n}\", \"{token}\", \"{msg}\"]' -p {acc_name}")