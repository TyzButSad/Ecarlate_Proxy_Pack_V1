import requests
from bs4 import BeautifulSoup
import os
import time
import random
import sys
os.system("apt install toilet")
color1=["\033[1;31;40m","\033[1;32;40m","\033[1;33;40m","\033[1;34;40m","\033[1;35;40m","\033[1;36;40m"]
def color():
 return str(random.choice(color1))
def generate(url,count):
 try:
  r=requests.get(url)
  soup=BeautifulSoup(r.content,'html.parser')
  list = soup.find(class_='table table-striped table-bordered')
  list1 = list.findAll('td')
  iplist=[]
  portlist=[]
  codelist=[]
  countrylist=[]
  anonymitylist=[]
  googlelist=[]
  httpslist=[]
  last_checklist=[]
  finallist=[]
  j=0
  while(j<(8*count)):
   a=str(list1[j].contents[0])
   iplist.append(a)
   j=j+8
  j=1
  while(j<(8*count)):
   a=str(list1[j].contents[0])
   portlist.append(a)
   j=j+8
  j=2   
  while(j<(8*count)):
   a=str(list1[j].contents[0])
   codelist.append(a)
   j=j+8   
  j=3   
  while(j<(8*count)):
   a=str(list1[j].contents[0])
   countrylist.append(a)
   j=j+8 
  j=4   
  while(j<(8*count)):
   a=str(list1[j].contents[0])
   anonymitylist.append(a)
   j=j+8
  j=5   
  while(j<(8*count)):
   a=str(list1[j].contents[0])
   googlelist.append(a)
   j=j+8  
  j=6   
  while(j<(8*count)):
   a=str(list1[j].contents[0])
   httpslist.append(a)
   j=j+8  
  j=7   
  while(j<(8*count)):
   a=str(list1[j].contents[0])
   last_checklist.append(a)
   j=j+8
  for k in range (0,count):
      print(color()+iplist[k]+":"+color()+portlist[k]+"\t"+color()+codelist[k]+"\t"+color()+countrylist[k]+"\t\t"+color()+anonymitylist[k]+color()+"\tGoogle:"+googlelist[k]+color()+"\thttps:"+httpslist[k]+color()+"\tLast checked "+last_checklist[k]+"\n")
 except:
  print("\033[1;31;40m%d Proxies can't be generated at this time. Try giving a smaller amount(i.e 1) or try again after some time."%count)
def socks(count):
 try:
  r=requests.get("https://www.socks-proxy.net")
  soup=BeautifulSoup(r.content,'html.parser')
  list = soup.find(class_='table table-striped table-bordered')
  list1 = list.findAll('td')
  iplist=[]
  portlist=[]
  codelist=[]
  countrylist=[]
  versionlist=[]
  anonymitylist=[]
  httpslist=[]
  last_checklist=[]
  j=0
  while(j<8*count):
   a=str((list1[j].contents[0]))
   iplist.append(a)
   j=j+8
  j=1
  while(j<8*count):
   a=str((list1[j].contents[0]))
   portlist.append(a)
   j=j+8
  j=2
  while(j<8*count):
   a=str((list1[j].contents[0]))
   codelist.append(a)
   j=j+8
  j=3
  while(j<8*count):
   a=str((list1[j].contents[0]))
   countrylist.append(a)
   j=j+8
  j=4
  while(j<8*count):
   a=str((list1[j].contents[0]))
   versionlist.append(a)
   j=j+8
  j=5
  while(j<8*count):
   a=str((list1[j].contents[0]))
   anonymitylist.append(a)
   j=j+8
  j=6
  while(j<8*count):
   a=str((list1[j].contents[0]))
   httpslist.append(a)
   j=j+8
  j=7
  while(j<8*count):
   a=str((list1[j].contents[0]))
   last_checklist.append(a)
   j=j+8

  for k in range (0,count):
   print(color()+iplist[k]+":"+color()+portlist[k]+"\t"+color()+codelist[k]+"\t"+color()+countrylist[k]+"\t"+color()+versionlist[k]+"\t"+color()+anonymitylist[k]+"\thttps:"+color()+httpslist[k]+"\tLast Checked :"+color()+last_checklist[k]+"\n")
 except:
  print("\033[1;31;40m%d Proxies can't be generated at this time. Try giving a smaller amount(i.e 1) or try again after some time."%count)
def banner():
 os.system("clear")
 os.system("toilet -fmono12 -F gay Tyz")

 print("    \033[1;36;40m Create By \033[1;32;40m Tyz")
 print("\n\n")

banner()
number=int(raw_input("\033[1;33;40mEntre le nombre de proxy que tu veux (Max:40) :"))
if(number>40):
 print("\033[1;31;40mEntre un nombre <=40. Quitter...")
 time.sleep(1.5)
 sys.exit()  
banner()
print("          \033[1;32;40m[1] \033[1;36;40mNEW PROXY")
print("          \033[1;32;40m[2] \033[1;36;40mUS PROXY")
print("          \033[1;32;40m[3] \033[1;36;40mUK PROXY")
print("          \033[1;32;40m[4] \033[1;36;40mSSL PROXY")
print("          \033[1;32;40m[5] \033[1;36;40mANONYMOUS PROXY")
print("          \033[1;32;40m[6] \033[1;36;40mSOCKS PROXY")

op=int(raw_input("Choisi:"))
banner()
if(op==1):
 generate("https://free-proxy-list.net",number) 
elif(op==2):
 generate("https://us-proxy.org",number) 
elif(op==3):
 generate("https://free-proxy-list.net/uk-proxy.html",number)
elif(op==4):
 generate("https://www.sslproxies.org",number)
elif(op==5):
 generate("https://free-proxy-list.net/anonymous-proxy.html",number)
elif(op==6):
 socks(number)
else:
 print("\033[1;31;40mInvalid input. Quiting...")
 time.sleep(1.5)
 sys.exit()









