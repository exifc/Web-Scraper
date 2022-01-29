# \ Coded by Volt#1672 /


import requests
import threading
import random
import sys

if len(sys.argv)<2:
  print("\nWrong usage! Usage: python3 " + sys.argv[0] + " <threads> <request rate, higher = faster scanning> <port>\n")
  exit()

if len(sys.argv)<3:
  print("\nNo Request rate specified! Specify more than 1.\n")
  exit()

if len(sys.argv)<4:
  print("\nNo port specified! Available options: \nhttp (80, 8080) \nhttps (443) \nssh (22) \nftp (21) \ntelnet (23) \nminecraft (25565)\nall (every available port)\n")
  exit()

threads = sys.argv[1]
reqrate = sys.argv[2]
port = sys.argv[3]

def det():

  avalport = ['ssh', 'ftp', 'telnet', 'all', 'minecraft', 'http', 'https']

  if str(port) not in avalport:
    print("\nInvalid port! Available options: \nhttp (80, 8080) \nhttps (443) \nssh (22) \nftp (21) \ntelnet (23) \nminecraft (25565)\nall (every available port)\n")
    exit()

  if int(threads)<1:
    print("\nNo threads specified! Specify more than 1 thread.\n")
    exit()

  if int(reqrate)<1:
    print("\nNo Request rate specified! Specify more than 1.\n")
    exit()

  
  if int(threads) and int(reqrate)>0:
    start()


def attack():
   while True: 
    for _ in range(int(reqrate)):
      if str(port) == "ssh":
        ports = ['22']
      elif str(port) == "http":
        ports = ['80', '8080']
      elif str(port) == "https":
        ports = ['443']
      elif str(port) == "telnet":
        ports = ['23']
      elif str(port) == "ftp":
        ports = ['21']
      elif str(port) == "minecraft":
        ports = ['25565']
      elif str(port) == "all":
        ports = ['80', '443', '8080', '25565', '22', '23', '21'] # You can add more ports! (W.I.P.)
      randport = random.choice(ports)
      randip = random.randint(1, 255)
      randip2 = random.randint(1, 255)
      randip3 = random.randint(1, 255)
      randip4 = random.randint(1, 255)
      empty = "."
      randit = str(randip) + str(empty) + str(randip2) + str(empty) + str(randip3) + str(empty) + str(randip4)
      url = f"http://{randit}:" + str(randport)
      try:
        ses = requests.Session()
        a = ses.get(url=url, timeout=7)
        if randport == "80":
          with open("found.txt","a") as all:
            all.write(str(url) + str(" HTTP Webserver detected!\n"))
            all.close()
          print(str(url) + str(" HTTP Webserver detected!"))
        elif randport == "443":
          with open("found.txt","a") as all:
            all.write(str("https://" + randit) + str(" HTTPS Webserver detected!\n"))
            all.close()
          print(str("https://" + randit) + str(" HTTPS Webserver detected!"))
        elif randport == "8080":
          with open("found.txt","a") as all:
            all.write(str(url) + str(" HTTP Webserver detected!\n"))
            all.close()
          print(str(url) + str(" HTTP Webserver detected!"))
        elif randport == "25565":
          with open("found.txt","a") as all:
            all.write(str(randit + randport) + str(" Minecraft server detected!\n"))
            all.close()
          print(str(randit + randport) + str(" Minecraft server detected!"))
        elif randport == "22":
          with open("found.txt","a") as all:
            all.write(str(randit + randport) + str(" SSH Detected!\n"))
            all.close()
          print(str(randit + randport) + str(" SSH Detected!"))
        elif randport == "23":
          with open("found.txt","a") as all:
            all.write(str(randit + randport) + str(" Telnet detected!\n"))
            all.close()
          print(str(randit + randport) + str(" Telnet detected!"))
        elif randport == "21":
          with open("found.txt","a") as all:
            all.write(str(randit + randport) + str(" FTP Detected!\n"))
            all.close()
          print(str(randit + randport) + str(" FTP Detected!"))
      except:
        pass

def start():
  print("\n\ Coded by Volt#1672 /")
  print("\nStarting, this might take a while...\n")
  for _ in range(int(threads)):
    threading.Thread(target=attack).start()


det()
