import socket              
import sys
import binascii
import string

if(len(sys.argv) < 3) :
   print ('Usage : python program.py hostname port')
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


data=str(sys.argv[3])
l=data.encode('utf-8')
text = ""
for i in range (0, len(l), 512) :
    hex_str = binascii.unhexlify(l)
    sock.send(hex_str[i:i+512])
    text += sock.recv(256).decode("utf-8")
print ("Desencrypt:", text)

sock.close()  
     

