# first of all import the socket library
import socket
import AES
import ECDH
import random
import math


# next create a socket object
s = socket.socket()
print("Socket successfully created")

# reserve a port on your computer in our
# case it is 12345 but it can be anything
port = 12345

# Next bind to the port
# we have not typed any ip in the ip field
# instead we have inputted an empty string
# this makes the server listen to requests
# coming from other computers on the network
s.bind(('', port))
print("socket binded to %s" % (port))

# put the socket into listening mode
s.listen(5)
print("socket is listening")

# a forever loop until we interrupt it or
# an error occurs
while True:

    # Establish connection with client.
    c, addr = s.accept()
    print('Got connection from', addr)

    # receive
    msg = c.recv(2048).decode()

    a, b, p, gx, gy, Ax, Ay = map(int, msg.split(","))

    # Bob
    e = p + 1 - int(2 * math.sqrt(p))
    kb = random.randint(2, e-1)
    Bx, By = ECDH.doubleAddAlgorithm(a, b, p, gx, gy, kb)

    # send Bob's public key to Alice
    msg = str(Bx) + "," + str(By)

    c.send(msg.encode())

    # Generate shared secret
    Kx, Ky = ECDH.doubleAddAlgorithm(a, b, p, Ax, Ay, kb)

    print("Alice's public key: ", Ax, Ay)
    print("Bob's public key: ", Bx, By)
    print("Shared Key: ", Kx, Ky)

    msg = "Bob ready to receive message"
    c.send(msg.encode())

    msg = c.recv(2048).decode()
    print("Alice's confirmation: ", msg)

    # receive encrypted message
    msg = c.recv(2048).decode()
    decryptedMsg, decryptionTime = AES.aes_decrypt(Kx, msg)

    print("Decrypted message: ", decryptedMsg)

    # Close the connection with the client
    c.close()

    # Breaking once connection closed
    break
