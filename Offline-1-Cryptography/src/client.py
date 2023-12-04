# Import socket module 
import socket			 
import AES
import ECDH
import random
import math
import Crypto.Util.number

# Create a socket object 
s = socket.socket()		 

# Define the port on which you want to connect 
port = 12345			

# connect to the server on local computer 
s.connect(('127.0.0.1', port)) 

# Common parameters
AES_key_length = 128
a = 3
b = 7
gx = 2359680 
gy = 3624763428
p = Crypto.Util.number.getPrime(AES_key_length, randfunc=Crypto.Random.get_random_bytes)
e = p + 1 - int(2 * math.sqrt(p))

# Alice
ka = random.randint(2, e-1)
Ax, Ay = ECDH.doubleAddAlgorithm(a, b, p, gx, gy, ka)

msg = str(a) + "," + str(b) + "," + str(p) + "," + str(gx) + "," + str(gy) + "," + str(Ax) + "," + str(Ay)
s.send(msg.encode())


# receive Bob's public key
msg = s.recv(2048).decode()
[Bx, By] = msg.split(",")
Bx = int(Bx)
By = int(By)


# Generate shared secret
Kx, Ky = ECDH.doubleAddAlgorithm(a, b, p, Bx, By, ka)

print("Alice's public key: ", Ax, Ay)
print("Bob's public key: ", Bx, By)
print("Shared Key: ", Kx, Ky)

msg = "Alice ready to send message"
s.send(msg.encode())

msg = s.recv(2048).decode()
print("Bob's confirmation: ", msg)


plaintext, encryptedMsg, encryptionTime, keyScheduleTime = AES.aes_encrypt(Kx, "Hello Bob")
print("Plaintext : ", plaintext)
print("Encrypted message: ", encryptedMsg)

s.send(encryptedMsg.encode())
s.close()	 
	
