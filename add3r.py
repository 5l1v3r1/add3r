import sys,os,re,socket,binascii,time,json,random,threading,pprint,smtplib,telnetlib,os.path,hashlib,string,glob,sqlite3,urllib,argparse,marshal,base64,colorama,requests
from colorama import *
from colorama import Fore,Back,init
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from platform import system
from time import strftime
colorama.init()

CLEAR_SCREEN = '\033[2J'
RED = '\033[31m'  
RESET = '\033[0m'  
BLUE  = "\033[34m"
CYAN  = "\033[36m"
GREEN = "\033[32m"
RESET = "\033[0m"
BOLD    = "\033[m"
REVERSE = "\033[m"


def logo():
        clear = "\x1b[0m"
        colors = [36, 32, 34, 35, 31, 37  ]

        x = """ 
     _    _   _  ___  _   _ ____  _____ 
    / \  | \ | |/ _ \| \ | |  _ \| ____|
   / _ \ |  \| | | | |  \| | |_) |  _|  
  / ___ \| |\  | |_| | |\  |  _ <| |___ 
 /_/   \_\_| \_|\___/|_| \_|_| \_\_____|
                                            
        Coded By [ Anonre ]
            Tools Fitur
            [ python2 ]
              
[ 1. Add | http://          | On Beginning List  ]
[ 2. Add | https://         | On Beginning List  ]
[ 3. Add | /wp-login.php    | On End List        ]
[ 4. Add | /                | On End List        ]
[ 5. Add | /xmlrpc.php      | On End List        ]
[ 6. Coming soon updated    | On Progress Update ]

Copyright@2022
"""
        for N, line in enumerate(x.split("\n")):
            sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
            time.sleep(0.05)
logo()
anonre = raw_input("root@anonre:~# ")

class anonz():

	def httpbeg(self):
		kep = raw_input("Your List : ")
		kep = open(kep, 'r')
		for i in kep:
			i = i.rstrip()
			print("http://"+i)
			with open('http.txt', 'a') as o:
				o.write("http://" + i + '\n')
		print("[ >> ] root@anonre:~# successfully !! check http.txt !!")

	def wplogin(self):
		kep = raw_input("Your List : ")
		kep = open(kep, 'r')
		for i in kep:
			i = i.rstrip()
			print(i+"/wp-login.php")
			with open('wplog.txt', 'a') as o:
				o.write(i + "/wp-login.php" + '\n')
		print("[ >> ] root@anonre:~# successfully !! check wplog.txt !!")

	def slashend(self):
		kep = raw_input("Your List : ")
		kep = open(kep, 'r')
		for i in kep:
			i = i.rstrip()
			print(i+"/")
			with open('slashend.txt', 'a') as o:
				o.write(i + "/" + '\n')
		print("[ >> ] root@anonre:~# successfully !! check slashend.txt !!")

	def httpsbeg(self):
		kep = raw_input("Your List : ")
		kep = open(kep, 'r')
		for i in kep:
			i = i.rstrip()
			print("https://"+i)
			with open('https.txt', 'a') as o:
				o.write("https://" + i + '\n')
		print("[ >> ] root@anonre:~# successfully !! check https.txt !!")

	def xmlrpc(self):
		kep = raw_input("Your List : ")
		kep = open(kep, 'r')
		for i in kep:
			i = i.rstrip()
			print(i+"/xmlrpc.php")
			with open('xmlrpc.txt', 'a') as o:
				o.write(i + "/xmlrpc.php" + '\n')
		print("[ >> ] root@anonre:~# successfully !! check xmlrpc.txt !!")

dahah = anonz()
if anonre == '1':
	dahah.httpbeg()
elif anonre == '2':
	dahah.httpsbeg()
elif anonre == '4':
	dahah.slashend()
elif anonre == '5':
	dahah.xmlrpc()
elif anonre == '3':
	dahah.wplogin()
else:
	print("Pilih toolsnya terlebih dahulu")
	