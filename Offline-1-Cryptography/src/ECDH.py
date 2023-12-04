import random
import math
import Crypto.Util.number
import sys
import time


def bigMod(x, y, mod):
    if (y == 0):
        return 1

    p = bigMod(x, y // 2, mod) % mod
    p = (p * p) % mod

    if y % 2 == 1:
        p = (p * x) % mod

    return p


def modInverse(x, mod):
    return bigMod(x, mod-2, mod)


def pointGenFromS(x1, y1, x2, y2, p, s):
    x3 = s*s - x1 - x2
    y3 = s*(x1-x3) - y1
    return x3 % p, y3 % p


def pointAddition(x1, y1, x2, y2, p):
    s = (y2-y1) * modInverse(x2-x1, p)
    s = s % p
    return pointGenFromS(x1, y1, x2, y2, p, s)


def pointDoubling(x1, y1, a, p):
    s = (3*x1*x1 + a) * modInverse(2*y1, p)
    s = s % p
    return pointGenFromS(x1, y1, x1, y1, p, s)


def doubleAddAlgorithm(a, b, p, x, y, d):
    tx = x
    ty = y
    # bin returns 0bxxxxx, so we remove the first 2 chars and msb
    d = bin(d)[3:]
    for i in d:
        tx, ty = pointDoubling(tx, ty, a, p)
        if i == '1':
            tx, ty = pointAddition(tx, ty, x, y, p)
    return tx, ty



a = 3
b = 7
x = 2359680 
y = 3624763428

def benchmark(nbits, iteration):
    timeA = timeB = timeR = 0
    for i in range(iteration):

        p=Crypto.Util.number.getPrime(nbits, randfunc=Crypto.Random.get_random_bytes)
        e = p + 1 - int(2 * math.sqrt(p))

        ka = random.randint(2, e-1)
        kb = random.randint(2, e-1)


        startTime = time.time()
        A = doubleAddAlgorithm(a, b, p, x, y, ka)
        timeA += time.time() - startTime

        startTime = time.time()
        B = doubleAddAlgorithm(a, b, p, x, y, kb)
        timeB += time.time() - startTime


        startTime = time.time()
        R = doubleAddAlgorithm(a, b, p, x, y, ka*kb)
        timeR += time.time() - startTime


    timeA = timeA / iteration * 1000
    timeB = timeB / iteration * 1000
    timeR = timeR / iteration * 1000


    return timeA, timeB, timeR

if __name__ == "__main__":
    print("---------------------------------------------")
    print("    |          Computation Time For         |")
    print(" K  -----------------------------------------")
    print("    |      A     |      B     |shared key R |")
    print("---------------------------------------------")


    timeA, timeB, timeR = benchmark(128, 5)
    print(f'128 | {timeA:10.6f} | {timeB:10.6f} | {timeR:10.6f}  |')
    timeA, timeB, timeR = benchmark(192, 5)
    print(f'192 | {timeA:10.6f} | {timeB:10.6f} | {timeR:10.6f}  |')
    timeA, timeB, timeR = benchmark(256, 5)
    print(f'256 | {timeA:10.6f} | {timeB:10.6f} | {timeR:10.6f}  |')
    print("---------------------------------------------")






