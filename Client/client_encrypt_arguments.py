import socket               
import sys
import binascii
import string

if(len(sys.argv) < 3) :
   print ('Usage: python program.py hostname port')
   sys.exit()
     
host = sys.argv[1]
port = int(sys.argv[2])

if int(sys.argv[2]) != 1500 :   
   print ("Error: Bad port")
   sys.exit() 
    
sock = socket.socket()
    
try :
        sock.connect((host, port))
        
except :
        print ('Unable to connect')
        sys.exit()

if(len(sys.argv) < 4) :
  print ('Error: Missing Text')
  sys.exit()
   
data = sys.argv[3]
l = data.encode('utf-8')
hex_bytes = ""
for i in range (0, len(l), 244) :
    sock.send(l[i:i+244])
    text = sock.recv(256)
    hex_bytes += binascii.hexlify(text).decode("utf-8") 
print (hex_bytes)

sock.close()                  


