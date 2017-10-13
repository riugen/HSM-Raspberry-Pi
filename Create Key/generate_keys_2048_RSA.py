import pkcs11
import pkcs11.util.rsa
import os
import pickle

from pkcs11 import KeyType, ObjectClass, Mechanism
from pkcs11.util.rsa import encode_rsa_public_key

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5

lib = pkcs11.lib(os.environ['PKCS11_MODULE'])
token = lib.get_token(token_label='Test')

# Open a session on our token
session = token.open(rw=True, user_pin='654321') 
print(session) 

# Generate an RSA keypair in this session
pub, priv = session.generate_keypair(pkcs11.KeyType.RSA, 2048,
                                         store=True,
                                         label="Keypair")
pkcs11.util.rsa.encode_rsa_public_key(pub)

