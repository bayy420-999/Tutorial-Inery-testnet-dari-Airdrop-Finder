#!/usr/bin/python3
import ine
import os, re, time, json, pkg_resources

def setup():
    print('{:=^10}'.format('MENGINSTALL DEPENDENSI'))
    time.sleep(2)
    ine.instalDep()
    time.sleep(2)
    print('{:=^10}'.format('EXPORT PATH'))
    ine.exportPath()
    time.sleep(2)
    if '.bashrc' in os.listdir('/root'):
        print('Enviromental variable loaded')

if __name__ == '__main__':
    setup()
    if 'inquirer' not in [pkg.key for pkg in pkg_resources.working_set]:
        os.system('pip install inquirer')
    import inquirer

    os.system('clear')

    questions = [
        inquirer.List(
            'node_type',
            message = 'Pilih jenis node yang ingin dibuat',
            choices = ['Lite Node', 'Master Node'],
            default = 'Lite Node'
        ),
        inquirer.Text(
            'name',
            message = 'Masukan nama akun (sesuai di dashboard inery)',
            validate = lambda _, x: x != '',
            ignore = lambda x: x['node_type'] != 'Master Node'
        ),
        inquirer.Text(
            'pubkey',
            message = 'Masukan public key anda',
            validate = lambda _, x: x != '',
            ignore = lambda x: x['node_type'] != 'Master Node'
        ),
        inquirer.Text(
            'privkey',
            message = 'Masukan private key anda',
            validate = lambda _, x: x != '',
            ignore = lambda x: x['node_type'] != 'Master Node'
        ),
        inquirer.Text(
            'ip',
            message = 'Masukan Alamat IP (server) anda',
            validate = lambda _, x: re.match(r'\d+\.\d+\.\d+\.\d+', x)
        )
    ]
    
    answers = inquirer.prompt(questions)
    node_type = answers.get('node_type') if answers.get('node_type') else None
    name = answers.get('name') if answers.get('name') else None
    pubkey = answers.get('pubkey') if answers.get('pubkey') else None
    privkey = answers.get('privkey') if answers.get('privkey') else None
    ip = answers.get('ip') if answers.get('ip') else None
    
    with open('/root/inery-node/inery.setup/tools/config.json', 'r') as f:
        config = json.load(f)
    
    if name:
        config['MASTER_ACCOUNT']['NAME'] = name
    if pubkey:
        config['MASTER_ACCOUNT']['PUBLIC_KEY'] = pubkey
    if privkey:
        config['MASTER_ACCOUNT']['PRIVATE_KEY'] = privkey
    if ip:
        config['LITE_NODE']['PEER_ADDRESS'] = config['LITE_NODE']['PEER_ADDRESS'].replace('IP', ip)
        config['MASTER_ACCOUNT']['PEER_ADDRESS'] = config['MASTER_ACCOUNT']['PEER_ADDRESS'].replace('IP', ip)
    
    with open('/root/inery-node/inery.setup/tools/config.json', 'w') as f:
        json.dump(config, f, indent = 4)
