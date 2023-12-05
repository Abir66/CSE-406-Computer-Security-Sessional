
from BitVector import *
import time
Sbox = (
    0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76,
    0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0,
    0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15,
    0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75,
    0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84,
    0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF,
    0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8,
    0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2,
    0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73,
    0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB,
    0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79,
    0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08,
    0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A,
    0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E,
    0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF,
    0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16,
)

InvSbox = (
    0x52, 0x09, 0x6A, 0xD5, 0x30, 0x36, 0xA5, 0x38, 0xBF, 0x40, 0xA3, 0x9E, 0x81, 0xF3, 0xD7, 0xFB,
    0x7C, 0xE3, 0x39, 0x82, 0x9B, 0x2F, 0xFF, 0x87, 0x34, 0x8E, 0x43, 0x44, 0xC4, 0xDE, 0xE9, 0xCB,
    0x54, 0x7B, 0x94, 0x32, 0xA6, 0xC2, 0x23, 0x3D, 0xEE, 0x4C, 0x95, 0x0B, 0x42, 0xFA, 0xC3, 0x4E,
    0x08, 0x2E, 0xA1, 0x66, 0x28, 0xD9, 0x24, 0xB2, 0x76, 0x5B, 0xA2, 0x49, 0x6D, 0x8B, 0xD1, 0x25,
    0x72, 0xF8, 0xF6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xD4, 0xA4, 0x5C, 0xCC, 0x5D, 0x65, 0xB6, 0x92,
    0x6C, 0x70, 0x48, 0x50, 0xFD, 0xED, 0xB9, 0xDA, 0x5E, 0x15, 0x46, 0x57, 0xA7, 0x8D, 0x9D, 0x84,
    0x90, 0xD8, 0xAB, 0x00, 0x8C, 0xBC, 0xD3, 0x0A, 0xF7, 0xE4, 0x58, 0x05, 0xB8, 0xB3, 0x45, 0x06,
    0xD0, 0x2C, 0x1E, 0x8F, 0xCA, 0x3F, 0x0F, 0x02, 0xC1, 0xAF, 0xBD, 0x03, 0x01, 0x13, 0x8A, 0x6B,
    0x3A, 0x91, 0x11, 0x41, 0x4F, 0x67, 0xDC, 0xEA, 0x97, 0xF2, 0xCF, 0xCE, 0xF0, 0xB4, 0xE6, 0x73,
    0x96, 0xAC, 0x74, 0x22, 0xE7, 0xAD, 0x35, 0x85, 0xE2, 0xF9, 0x37, 0xE8, 0x1C, 0x75, 0xDF, 0x6E,
    0x47, 0xF1, 0x1A, 0x71, 0x1D, 0x29, 0xC5, 0x89, 0x6F, 0xB7, 0x62, 0x0E, 0xAA, 0x18, 0xBE, 0x1B,
    0xFC, 0x56, 0x3E, 0x4B, 0xC6, 0xD2, 0x79, 0x20, 0x9A, 0xDB, 0xC0, 0xFE, 0x78, 0xCD, 0x5A, 0xF4,
    0x1F, 0xDD, 0xA8, 0x33, 0x88, 0x07, 0xC7, 0x31, 0xB1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xEC, 0x5F,
    0x60, 0x51, 0x7F, 0xA9, 0x19, 0xB5, 0x4A, 0x0D, 0x2D, 0xE5, 0x7A, 0x9F, 0x93, 0xC9, 0x9C, 0xEF,
    0xA0, 0xE0, 0x3B, 0x4D, 0xAE, 0x2A, 0xF5, 0xB0, 0xC8, 0xEB, 0xBB, 0x3C, 0x83, 0x53, 0x99, 0x61,
    0x17, 0x2B, 0x04, 0x7E, 0xBA, 0x77, 0xD6, 0x26, 0xE1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0C, 0x7D,
)

Mixer = [
    [BitVector(hexstring="02"), BitVector(hexstring="03"), BitVector(hexstring="01"), BitVector(hexstring="01")],
    [BitVector(hexstring="01"), BitVector(hexstring="02"), BitVector(hexstring="03"), BitVector(hexstring="01")],
    [BitVector(hexstring="01"), BitVector(hexstring="01"), BitVector(hexstring="02"), BitVector(hexstring="03")],
    [BitVector(hexstring="03"), BitVector(hexstring="01"), BitVector(hexstring="01"), BitVector(hexstring="02")]
]

InvMixer = [
    [BitVector(hexstring="0E"), BitVector(hexstring="0B"), BitVector(hexstring="0D"), BitVector(hexstring="09")],
    [BitVector(hexstring="09"), BitVector(hexstring="0E"), BitVector(hexstring="0B"), BitVector(hexstring="0D")],
    [BitVector(hexstring="0D"), BitVector(hexstring="09"), BitVector(hexstring="0E"), BitVector(hexstring="0B")],
    [BitVector(hexstring="0B"), BitVector(hexstring="0D"), BitVector(hexstring="09"), BitVector(hexstring="0E")]
]



numOfRounds = {
    128: 10,
    192: 12,
    256: 14
}
AES_key_length = 128
roundKeys = []

rc = []
rc1 = BitVector(intVal=1, size=8)
rc2 = BitVector(intVal=2, size=8)
rc11B = BitVector(intVal=0x11B, size=9)

for i in range(11):
    rc.append(rc1)
    rc1 = rc1.gf_multiply_modular(rc2, rc11B, 8)





# ======================== DEBUGGING ========================
def printHexArray(array):
    for i in array:
        print(i.get_hex_string_from_bitvector(), end=" ")
    print("")

def printHexMatrix(matrix):
    for i in matrix:
        printHexArray(i)
        # if i % 4 == 0 then print new line
        if (matrix.index(i) + 1) % 4 == 0:
            print("")
    print("")

# ======================== Helper ========================
def substitute(bitVector, sub=Sbox):
    s = sub[bitVector.intValue()]
    return BitVector(intVal=s, size=8)

def arrayXor(array1, array2):
    newArray = []
    for i in range(len(array1)):
        newArray.append(array1[i] ^ array2[i])
    return newArray

def text2Hex(text):
    hexArray = []
    for i in text:
        hexArray.append(BitVector(textstring=i))
    return hexArray

def hex2Text(hexArray):
    text = ""
    for i in hexArray:
        text += i.get_bitvector_in_ascii()
    return text


def arrayToColumnMatrix(array):
    hexMatrix = []
    for i in range(4):
        row = []
        for j in range(4):
            row.append(array[i + j * 4])
        hexMatrix.append(row)
    return hexMatrix

def columnMatrixToArray(matrix):
    hexArray = []
    for i in range(4):
        for j in range(4):
            hexArray.append(matrix[j][i])
    return hexArray

def arrayXor(array1, array2):
    newArray = []
    for i in range(len(array1)):
        newArray.append(array1[i] ^ array2[i])
    return newArray

def xor_strings(str1, str2):
    xored = ''.join(chr(ord(a) ^ ord(b)) for a, b in zip(str1, str2))
    return xored

# ======================== AES ops ========================
def matrixXor(matrix1, matrix2):
    newMatrix = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[i])):
            row.append(matrix1[i][j] ^ matrix2[i][j])
        newMatrix.append(row)
    return newMatrix

def matrixSubstitute(matrix, sub=Sbox):
    newMatrix = []
    for i in range(len(matrix)):
        row = []
        for j in range(len(matrix[i])):
            row.append(substitute(matrix[i][j], sub))
        newMatrix.append(row)
    return newMatrix

def shiftRows(matrix):
    newMatrix = []
    newMatrix.append(matrix[0][:])
    newMatrix.append(matrix[1][1:] + matrix[1][:1])
    newMatrix.append(matrix[2][2:] + matrix[2][:2])
    newMatrix.append(matrix[3][3:] + matrix[3][:3])
    return newMatrix

def inverseShiftRows(matrix):
    newMatrix = []
    newMatrix.append(matrix[0][:])
    newMatrix.append(matrix[1][-1:] + matrix[1][:-1])
    newMatrix.append(matrix[2][-2:] + matrix[2][:-2])
    newMatrix.append(matrix[3][-3:] + matrix[3][:-3])
    return newMatrix


def mixColumn(matrix, mixer=Mixer):
    newMatrix = []
    b11B = BitVector(intVal=0x11B, size=9)
    for i in range(len(mixer)):
        row = []
        for j in range(len(mixer[i])):
            num = BitVector(intVal = 0, size = 8)
            for k in range(len(mixer[i])):
                num ^= matrix[k][j].gf_multiply_modular(mixer[i][k], b11B, 8)
            row.append(num)
        newMatrix.append(row)
    return newMatrix


def keygen(key):

    if type(key) == str:
        bv = BitVector(textstring=key)
        length = bv.length()
        
        if length < AES_key_length:
            bv.pad_from_left(AES_key_length - length)

        elif length > AES_key_length:
            bv = bv[0:AES_key_length]

    
    elif type(key) == int:
        bv = BitVector(intVal=key)
        length = bv.length()

        if length < AES_key_length:
            bv.pad_from_left(AES_key_length - length)
        
        elif length > AES_key_length:
            bv = bv[0:AES_key_length]


    hexArray = [bv[i*8:i*8+8] for i in range(len(bv)//8)]

    words = [hexArray[i*4:i*4+4] for i in range(len(hexArray)//4)]
    nk = len(words)

    
    # rc = BitVector(intVal=1, size=8)
    # rc2 = BitVector(intVal=2, size=8)
    # rc11B = BitVector(intVal=0x11B, size=9)

    # # Pre computed for faster execution
    
    rc_cnt=0
    requiredWords = numOfRounds[AES_key_length] * 4 + 4
    for i in range(nk, requiredWords):
        g = words[i-1]

        if i % nk == 0:
            g = g[1:] + g[:1] # left shift
            g = [substitute(i) for i in g] # substitute
            g[0] = g[0] ^ rc[rc_cnt] # add round constant
            # rc = rc.gf_multiply_modular(rc2, rc11B, 8)
            rc_cnt += 1

        
        elif nk > 6 and i % nk == 4:
            g = [substitute(i) for i in g]

        words.append(arrayXor(words[i-nk], g))
        
    roundKeys.clear()
    for i in range(0, len(words), 4):
        word = words[i] + words[i+1] + words[i+2] + words[i+3]
        roundKeys.append(arrayToColumnMatrix(word))


def aes_encrypt_block(hexArray):
    # hexArray = text2Hex(plaintext)
    state = arrayToColumnMatrix(hexArray)
    
    # intial round
    state = matrixXor(state, roundKeys[0])

    # middle rounds
    for i in range(1, numOfRounds[AES_key_length]):
        state = matrixSubstitute(state)
        state = shiftRows(state)
        state = mixColumn(state)
        state = matrixXor(state, roundKeys[i])
        # printHexMatrix(state)

    # last round
    state = matrixSubstitute(state)
    state = shiftRows(state)
    state = matrixXor(state, roundKeys[-1])
    # printHexMatrix(state)
    
    encryptedHexArray = columnMatrixToArray(state)
    encryptedText = hex2Text(encryptedHexArray)
    return encryptedHexArray

def aes_decrypt_block(ciphertext):
    state = arrayToColumnMatrix(ciphertext)

    invRoundKeys = roundKeys[:]
    invRoundKeys.reverse()

    # initial round
    state = matrixXor(state, invRoundKeys[0])

    for i in range(1, len(roundKeys)-1):
        state = inverseShiftRows(state)
        state = matrixSubstitute(state, InvSbox)
        state = matrixXor(state, invRoundKeys[i])
        state = mixColumn(state, InvMixer)
    
    state = inverseShiftRows(state)
    state = matrixSubstitute(state, InvSbox)
    state = matrixXor(state, invRoundKeys[-1])

    decryptedHexArray = columnMatrixToArray(state)
    return decryptedHexArray


def aes_encrypt(key, plaintext, mode=128, returnBytes=False):
    
    AES_key_size = mode
    
    start_time = time.time()
    keygen(key)
    keyScheduleTime = time.time() - start_time

    start_time = time.time()
    
    hexArray = []
    if type(plaintext) == str:
        hexArray = text2Hex(plaintext)
    elif type(plaintext) == bytes:
        hexArray = [BitVector(intVal=i, size=8) for i in plaintext]
    

    requiredPadding = 16 - len(hexArray) % 16
    if requiredPadding != 0:
        hexArray += [BitVector(intVal=requiredPadding, size=8)] * requiredPadding
    else :
        hexArray += [BitVector(intVal=0, size=8)] * 16


    # CBC
    randomIV = BitVector(intVal = 0)
    randomIV = randomIV.gen_random_bits(128)
    
    # encrypt
    encrypted = [randomIV[i*8:i*8+8] for i in range(len(randomIV)//8)]
    encryptedBlock = encrypted[:16]
    for i in range(0, len(hexArray), 16):
        block = hexArray[i:i+16]
        block = [block[i] ^ encryptedBlock[i] for i in range(len(block))]
        encryptedBlock = aes_encrypt_block(block)
        encrypted += encryptedBlock

    encryptionTime = time.time() - start_time

    if returnBytes == False:
        encrypted = hex2Text(encrypted)

    return hex2Text(hexArray), encrypted, encryptionTime, keyScheduleTime


def aes_decrypt(key, ciphertext, mode=128, returnBytes=False):
    
    AES_key_size = mode
    keygen(key)
   
    start_time = time.time()

    if type(ciphertext) == str:
        ciphertext = text2Hex(ciphertext)
    else:
        ciphertext = [BitVector(intVal=i, size=8) for i in ciphertext]
        
        
    # CBC
    decryptedText = []
    prevBlock = ciphertext[:16]
    for i in range(16, len(ciphertext), 16):
        block = ciphertext[i:i+16]
        decryptedBlock = aes_decrypt_block(block)
        decryptedText += [prevBlock[i] ^ decryptedBlock[i] for i in range(len(prevBlock))]
        prevBlock = block

    # remove padding

    required_padding = int(decryptedText[-1])
    if required_padding != 0:
        decryptedText = decryptedText[:-required_padding]
    else:
        decryptedText = decryptedText[:-16]

    decryptionTime = time.time() - start_time


    if returnBytes == False:
        decryptedText = hex2Text(decryptedText)

    return decryptedText, decryptionTime

def aes_encrypt_file(key, input_file, output_file, mode=128):
    plaintext = open(input_file, "rb").read()
    paddedPlaintext, ciphertext, encyptionTime, keyScheduleTime = aes_encrypt(key, plaintext, mode, True)
    f = open(output_file, "wb")
    for i in ciphertext:
        i.write_to_file(f)
    f.close()

    return encyptionTime

def aes_decrypt_file(key, input_file, output_file, mode=128):
    ciphertext = open(input_file, "rb").read()
    decryptedText, decryptionTime = aes_decrypt(key, ciphertext, mode, True)
    f = open(output_file, "wb")
    for i in decryptedText:
        i.write_to_file(f)
    f.close()

    return decryptionTime



def plainTextOp(key, plaintext, mode):

    paddedPlaintext, ciphertext, encyptionTime, keyScheduleTime = aes_encrypt(key, plaintext, mode)
    decryptedText, decryptionTime = aes_decrypt(key, ciphertext, mode)
    
    print("Key:")
    print("In ASCII :", key)
    print("In HEX: ", end="")
    printHexArray(text2Hex(key))
    print()

    print("Plain Text:")
    print("In ASCII :", paddedPlaintext)
    print("In HEX: ", end="")
    printHexArray(text2Hex(paddedPlaintext))
    print()

    print("Ciphered Text:")
    print("In HEX: ", end="")
    printHexArray(text2Hex(ciphertext))
    print("In ASCII :", ciphertext)
    print()

    print("Deciphered Text:")
    print("In HEX: ", end="")
    print(type(decryptedText))
    printHexArray(text2Hex(decryptedText))
    print("In ASCII :", decryptedText)
    print()

    start_time = time.time()
    keygen(key)
    keyScheduleTime = time.time() - start_time
    

    print("Execution Time Details:")
    print("Key Schedule Time:", keyScheduleTime*1000, "ms")
    print("Encryption Time:", encyptionTime*1000, "ms")
    print("Decryption Time:", decryptionTime*1000, "ms")


def main():

    mode = 128
    print("AES Encryption and Decryption")
    print("----------------------------")
    print("Select Mode:")
    print("1. 128-bit")
    print("2. 192-bit")
    print("3. 256-bit")
    print("")
    mode_choice = int(input("Enter your choice: "))

    if mode_choice == 1:
        mode = 128
    elif mode_choice == 2:
        mode = 192
    elif mode_choice == 3:
        mode = 256


    print("Select : ")
    print("1. Plain Text example")
    print("2. File encryption")
    print("3. File decryption")

    choice = int(input("Enter your choice: "))
    print("")
    key = input("Enter the key: ")

    
    if choice == 1:
        plaintext = input("Enter the plaintext: ")
        plainTextOp(key, plaintext, mode)

    elif choice == 2:
        filename = input("Enter the filename: ")
        encyptionTime = aes_encrypt_file(key, filename, filename + ".enc")
        
        print("Encryption Successful!")
        print("Encryption Time:", encyptionTime*1000, "ms")

    elif choice == 3:
        filename = input("Enter the filename: ")

        outputFile = filename.split(".")
        outputFileName = outputFile[0] + "_decrypted"
        
        if len(outputFile) > 1:
            outputFileName += "." + outputFile[1]
        
        decryptionTime = aes_decrypt_file(key, filename, outputFileName)

        print("Decryption Successful!")
        print("Decryption Time:", decryptionTime*1000, "ms")

    

if __name__ == "__main__":
    main()
    








