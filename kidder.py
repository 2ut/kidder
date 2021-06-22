import os
import string
import random
import time
import datetime
import sys
import keyboard
import os.path
def exit():
    sys.exit

ROOT_DIR = os.path.abspath(os.curdir)

host_file = open(ROOT_DIR + '/data/host.txt', 'r')
host_file_contents = host_file.read()

sec_file = open(ROOT_DIR + '/data/sec.txt', 'r')
sec_file_contents = sec_file.read()

method_file = open(ROOT_DIR + '/data/method.txt', 'r')
method_contents = method_file.read()

port_file = open(ROOT_DIR + '/data/port.txt', 'r')
port_file_contents = port_file.read()

user_file = open(ROOT_DIR + '/data/user.txt', 'r')
user_file_contents = user_file.read()
time.sleep(1)

def logo():
    os.system("cls")
    print("")
    print("")
    print("")
    print("")
    print("                                                     \u001b[38;5;87m╦╔═╦\u001b[38;5;85m╔╦╗╔\u001b[38;5;83m╦╗╔═\u001b[38;5;82m╗╦═╗")
    print("                                                     \u001b[38;5;87m╠╩╗║\u001b[38;5;85m ║║ \u001b[38;5;83m║║║╣\u001b[38;5;82m ╠╦╝")
    print("                                                     \u001b[38;5;87m╩ ╩╩\u001b[38;5;85m═╩╝═\u001b[38;5;83m╩╝╚═\u001b[38;5;82m╝╩╚═")
    print("")
    print("                                      \u001b[38;5;87m═══════════\u001b[38;5;85m═══════════════════\u001b[38;5;83m══════\u001b[38;5;82m══════")
    print ("                                       \u001b[38;5;251mHost: " + host_file_contents)
    print ("                                       \u001b[38;5;251mSeconds: " + sec_file_contents)
    print ("                                       \u001b[38;5;251mMethod: " + method_contents)
    print ("                                       \u001b[38;5;251mPort: " + port_file_contents)
    print ("                                       \u001b[38;5;251mUser: " + user_file_contents)
    print("                                      \u001b[38;5;87m═══════════\u001b[38;5;85m═══════════════════\u001b[38;5;83m═══════\u001b[38;5;82m═════")
    print("")
    print("")
    print("")
    
def choices():
    choice = input("\u001b[38;5;87m[" + user_file_contents + "\u001b[38;5;87m/\u001b[38;5;85mKi\u001b[38;5;83mdd\u001b[38;5;82mer]\u001b[38;5;249m$")
    if choice.startswith(("port")):
        logo()
        choices()                    
    elif choice.startswith(("")):
        exit()   
    else:
        exit()
logo()
choices()
