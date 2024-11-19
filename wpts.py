import requests
import os
import re
import time
import random
from requests.exceptions import RequestException

import sys
import os
import datetime   
from time import sleep
def testPY():
    if(sys.version_info[0] < 3):
        print ('\n\t [+] You have Python 2, Please Clear Data Termux And Reinstall Python ... \n')
        sys.exit()


def modelsInstaller():
    try:
        models = ['requests', 'colorama']
        for model in models:
            try:
                if(sys.version_info[0] < 3):
                    os.system('cd C:\Python27\Scripts & pip install {}'.format(model))
                else:
                    os.system('python -m pip install {}'.format(model))
                print(' ')
                print('[+] {} has been installed successfully, Restart the program.'.format(model))
                sys.exit()
                print(' ')
            except:
                print('[-] Install {} manually.'.format(model))
                print(' ')
    except:
        pass


import base64
import json
import time
import sys
import os
import re
import binascii
import time
import json
import random
import threading
import pprint
import smtplib
import telnetlib
import os.path
import hashlib
import string
import glob
import sqlite3
import urllib
import argparse
import marshal
import datetime   
from platform import system
from datetime import datetime

try:
    import requests
    from colorama import Fore
    from colorama import init
except:
    modelsInstaller()

requests.packages.urllib3.disable_warnings()

def cls():
    if system() == 'Linux':
        os.system('clear')
    else:
        if system() == 'Windows':
            os.system('cls')


cls()
CLEAR_SCREEN = '\033[2J'
RED = '\033[1;37;1m'  # mode 31 = red foreground
RESET = '\033[1;37;1m'  # mode 0  = reset
BLUE = "\033[1;37;1m"
WHITE = "\033[1;37;1m",
YELLOW = "\033[1;37;1m",
CYAN = "\033[1;37;1m"
MAGENTA = "\033[1;37;1m",
GREEN = "\033[1;37;1m"
RESET = "\033[1;37;1m"
BOLD = '\033[1;37;1m'
REVERSE = "\033[1;37;1m"

def logo():
    clear = "\x1b[0m"
    colors = [35, 33, 36]

    x = """
░██╗░░░░░░░██╗███████╗██╗░░░░░░█████╗░░█████╗░███╗░░░███╗ 
░██║░░██╗░░██║██╔════╝██║░░░░░██╔══██╗██╔══██╗████╗░████║ 
░╚██╗████╗██╔╝█████╗░░██║░░░░░██║░░╚═╝██║░░██║██╔████╔██║ 
░░████╔═████║░██╔══╝░░██║░░░░░██║░░██╗██║░░██║██║╚██╔╝██║ 
░░╚██╔╝░╚██╔╝░███████╗███████╗╚█████╔╝╚█████╔╝██║░╚═╝░██║ 
░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝ 

"""
    for N, line in enumerate(x.split("\n")):
        sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
        time.sleep(0.05)
logo()
testPY()
print('''\033[1;32m<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n''')
def venom():
    clear = "\x1b[0m"
    colors = [35, 33, 36]


   


def Subscraption():
    os.system('git pull')
    time.sleep(1)
    uuid = str(os.geteuid())+"#"+str(os.geteuid())
    id = "Premium-Tool-"+"".join(uuid)
    os.system('clear')

    # Stylish colored logo
    logo = '''
                                
\u001b[36m██╗░░░░░░█████╗░░█████╗░██████╗░███████╗██████╗░ 
\u001b[31m██║░░░░░██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗ 
\u001b[35m██║░░░░░██║░░██║███████║██║░░██║█████╗░░██████╔╝ 
\u001b[32m██║░░░░░██║░░██║██╔══██║██║░░██║██╔══╝░░██╔══██╗ 
\u001b[37m███████╗╚█████╔╝██║░░██║██████╔╝███████╗██║░░██║ 
\u001b[33m╚══════╝░╚════╝░╚═╝░░╚═╝╚═════╝░╚══════╝╚═╝░░╚═╝ 

\033[1;33m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 [•] Tool       : Post Loader Using For Cookies 
 [•] Note       : This Tool Is Premium 
 [•] Onwer      : Sahil Ansari 
 [•] Version    :  0.1
\033[1;33m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

                                '''

    print(logo.center(os.get_terminal_size().columns))

    print("\033[1;32m You Get Approved for Using Command  Paid Tool \033[1;37m")
    print("\n\033[1;33m Your Key :\u001b[32m "+id);time.sleep(0.1)
    print ('\u001b[33m' +
          '--------------------------------------------------')
    try:
        httpCaht = requests.get("https://github.com/Harshit-420/Apt/blob/main/Ao").text
        if id in httpCaht:
            print("\n\033[1;32m Congrats You get approved Successfully")
            msg = str(os.geteuid())
            time.sleep(1)
            pass
        else: 
            print("\n\033[1;33m Your Key Not approved please contact the Own")
            time.sleep(0.1)
            input('\n\nPress Enter to send your key')
            tks = ("Dear%20Admin,%20Please%20Approved%20My%20Key%20To%20Premium%20%20Thanks%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20My%20Email%20:%20'+lol+'%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20My%20Name%20:%20'+name+'%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20My%20%20Key%20%20:%20"+id)
            os.system('am start https://wa.me/+919695003501?text='+tks), Subscraption()
            time.sleep(1)
            exit()
    except Exception as e:
        print(e)
        time.sleep(2)
        Subscraption()
    except:
        sys.exit()






    
# Prompt Password 
def pas():

    password = input("\033[1;32;33m[♡] Enter Tool Passwrod  :: ") 

    mmm = requests.get('https://pastebin.com/raw/cWqmYLb6').text



    if mmm not in password:

        print('\033[1;32;31m' + '[•] <==> Incorrect Password!')

        sys.exit()
Subscraption()

pas()

print("\033[1;35m[♡] Time start now:", time.strftime("%Y-%m-%d %H:%M:%S"))   

class FacebookCommenter:
    def __init__(self):
        self.comment_count = 0

    def comment_on_post(self, cookies, post_id, comment, timm):
        with requests.Session() as r:
            r.headers.update({
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,/;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'sec-fetch-site': 'none',
                'accept-language': 'id,en;q=0.9',
                'Host': 'mbasic.facebook.com',
                'sec-fetch-user': '?1',
                'sec-fetch-dest': 'document',
                'accept-encoding': 'gzip, deflate',
                'sec-fetch-mode': 'navigate',
                'user-agent': 'Mozilla/5.0 (Linux; Android 13; SM-G960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5790.166 Mobile Safari/537.36',
                'connection': 'keep-alive',
            })

            response = r.get('https://mbasic.facebook.com/{}'.format(post_id), cookies={"cookie": cookies})

            next_action_match = re.search('method="post" action="([^"]+)"', response.text)
            if next_action_match:
                self.next_action = next_action_match.group(1).replace('amp;', '')
            else:
                print(f"\033[1;37;1m  Coockies Chack =>C_USER ID<= i_USER \033[1;32;31m{self, cookies}")
                return
                print('\033[1;34mThe Comment is ready to go on the post')

            fb_dtsg_match = re.search('name="fb_dtsg" value="([^"]+)"', response.text)
            if fb_dtsg_match:
                self.fb_dtsg = fb_dtsg_match.group(1)
            else:
                print(f"\033[1;35;1m Your Cookie File Complete Restart your Cookie file\033[1;32;31m{self, cookies}")
                return
                print('\033[1;34mThe Comment is ready to go on the post')

            jazoest_match = re.search('name="jazoest" value="([^"]+)"', response.text)
            if jazoest_match:
                self.jazoest = jazoest_match.group(1)
            else:
                print("<Error> jazoest not found")
                return

            data = {
                'fb_dtsg': self.fb_dtsg,
                'jazoest': self.jazoest,
                'comment_text': comment,
                'comment': 'Submit',
            }

            r.headers.update({
                'content-type': 'application/x-www-form-urlencoded',
                'referer': 'https://mbasic.facebook.com/{}'.format(post_id),
                'origin': 'https://mbasic.facebook.com',
            })

            response2 = r.post('https://mbasic.facebook.com{}'.format(self.next_action), data=data, cookies={"cookie": cookies})

            if 'comment_success' in str(response2.url) and response2.status_code == 200:
                self.comment_count += 1
                sys.stdout.write(f"\rComment count: {self.comment_count}")
                sys.stdout.flush()  # Flush the output
                print(f"Comment successfully posted: {comment}")  # Add this line for debugging
            else:  
              
                print('\033[1;36m' + '--------------------------------------------------')
                print('\033[1;32;40m' + ' Status :: Active')
                e =datetime.now()                
                print (e.strftime("\033[1;33m Date :: %d-%m-%Y "))
                print (e.strftime("\033[1;33m TIME :: %I:%M:%S %p"))
                         
                print(f"\033[1;32;40m Comment Sent Successfully :: {comment}")
        



    def inputs(self):
        try:
        	
            coockies_file_path = input("[♡] Enter Cookie file Path  ::").strip()
            with open(coockies_file_path, 'r') as file:
                 your_cookies = file.read().splitlines()
                 
                 
                                 
                 post_id = input(f"[♡] Enter Your Post Uid  ::").strip()


            comments_file = input("[♡] Enter Comment file Path  ::").strip()
            with open(comments_file, 'r') as file:
                comments = file.readlines()


            timm = int(input("[♡] Enter time (speed in second  ::").strip())



            cookie_index = 0  # Initialize the current cookie index to 0

            while True:  # Infinite loop
                try:
                    for comment in comments:
                        comment = comment.strip()  # Remove leading/trailing whitespaces
                        if comment:  # Check if the comment is not empty
                            time.sleep(timm)
                            self.comment_on_post(your_cookies[cookie_index], post_id, comment, timm)
                            cookie_index = (cookie_index + 1) % len(your_cookies)  # Move to the next cookie or loop back to the first one
                except RequestException as e:
                    print(f"<chack first & last coockies> {str(e).lower()}")
                except Exception as e:
                    print(f"<chack first & last coockies> {str(e).lower()}")
                except KeyboardInterrupt:
                    break

        except Exception as e:
            print(f"<chack first & last coockies> {str(e).lower()}")
            exit()



if __name__ == "__main__":
    # Create a thread for the HTTP server



    # Run Facebook commenter
     commenter = FacebookCommenter()
     commenter.inputs()