import socket             
import pkcs11
import pkcs11.util.rsa
import os
import sys, traceback
import threading

from pkcs11 import KeyType, ObjectClass, Mechanism
from pkcs11.util.rsa import encode_rsa_public_key

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5

tolab = ('Test')
upin = ('654321')

lib = pkcs11.lib(os.environ['PKCS11_MODULE'])
token = lib.get_token(token_label= tolab)

# Open a session on our token
session = token.open(rw=True, user_pin= upin) 
#print(session) 

# Extract public key
key = session.get_key(key_type=KeyType.RSA, object_class=ObjectClass.PUBLIC_KEY)
key = RSA.importKey(encode_rsa_public_key(key))

# Encryption on the local machine
cipher = PKCS1_v1_5.new(key)

class ThreadedServer(object):
    def __init__(self, host, port): 
        self.host = ('localhost')
        self.port = (1500)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port)) 
        print ('Starting up on', self.host, self.port)
  
    def listen(self):
        self.sock.listen(10)    
        while True:
            client, address = self.sock.accept()
            client.settimeout(60) 
            threading.Thread(target = self.listenToClient,args = (client,address)).start()
            print ("Got connection from", address)

    def listenToClient(self, client, address):
        l = client.recv(256)
        while (l):
            print ("Receiving...", address)
            encText=cipher.encrypt(l)  
            client.sendall(encText)
            l = client.recv(256)
            
        print ("Done Reciving")
        print ("Done Sending")  

if __name__ == "__main__":
    while True:
        port_num = 1500
        try:
            port_num = 1500
            break
        except ValueError:
            pass

    ThreadedServer('',port_num).listen()

