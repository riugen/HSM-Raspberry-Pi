from time import sleep 
             
import socket              
import sys
import binascii
import string

if(len(sys.argv) < 3) :
   print ('Usage: python3 program.py hostname port')
   sys.exit()
   
host = sys.argv[1]
port = int(sys.argv[2])

if int(sys.argv[2]) != 1600 :   
   print ("Error: Bad port")
   sys.exit()
    
sock = socket.socket()

try :
        sock.connect((host, port))
except :
        print ('Unable to connect')
        sys.exit()

rlong = 256

f = open('encFile.bin','rb')
print ('Sending...')
l = f.read(rlong)
archivo = open('result','wb')
while (l):
    print ('Sending...')
    sock.send(l)
    text = sock.recv(256)
    if not text:
       sleep(0.001)
       text = sock.recv(256)
    archivo.write(text) 
    print("Reciving...")                   
    l = f.read(rlong)
f.close()

archivo.close()
print ("Done Sending")
print ("Done Reciving")
sock.close()     
          
