import numpy as np

def hillCipherEncrypt(plainText, keyMatrix):
    """
    Encrypts the plainText using the Hill Cipher algorithm.

    Args:
        plainText (str): The plainText message to encrypt.
        keyMatrix (list of lists): The square matrix used as the encryption key.

    Returns:
        str: The encrypted cipherText.
    """
    # Ensure the key matrix is square
    n = len(keyMatrix)
    for row in keyMatrix:
        if len(row) != n:
            raise ValueError("Key matrix must be square")

    # Convert plainText to uppercase
    plainText = ''.join(plainText.upper())

    # Pad plainText with 'X' if its length is not a multiple of the matrix size
    while len(plainText) % n != 0:
        plainText += 'X'

    # Convert plainText to unicode values
    plainTextUnicode = [ord(char) - ord('A') for char in plainText]

    # Divide plainText into segments of size n
    segments = [plainTextUnicode[i:i + n] for i in range(0, len(plainTextUnicode), n)]

    # Convert key matrix to a NumPy array
    keyMatrix = np.array(keyMatrix)

    # Encrypt each block
    cipherText = ''
    for segment in segments:
        # Convert block to a NumPy column vector
        blockVector = np.array(segment).reshape(n, 1)

        encryptedVector = np.dot(keyMatrix, blockVector) % 26

        # Convert unicode values back to letters
        cipherText += ''.join(chr(int(num) + ord('A')) for num in encryptedVector.flatten())

    return cipherText

def modularInverse(matrix, modulus):
    """
    Computes the modular inverse of a matrix under a given modulus.

    Args:
        matrix (np.ndarray): The square matrix to invert.
        modulus (int): The modulus.

    Returns:
        np.ndarray: The modular inverse of the matrix.
    """
    determinant = int(round(np.linalg.det(matrix)))  # Compute determinant
    determinantMod = determinant % modulus  # Determinant mod 26

    # Compute modular multiplicative inverse of the determinant
    determinantInv = pow(determinantMod, -1, modulus)

    # Compute adjugate matrix
    matrixModInv = (
        determinantInv * np.round(determinant * np.linalg.inv(matrix)).astype(int) % modulus
    )

    return matrixModInv % modulus

def hillCipherDecrypt(cipherText, keyMatrix):
    """
    Decrypts the cipherText using the Hill Cipher algorithm.

    Args:
        cipherText (str): The cipherText message to decrypt.
        keyMatrix (list of lists): The square matrix used as the encryption key.

    Returns:
        str: The decrypted plainText.
    """
    # Ensure the key matrix is square
    n = len(keyMatrix)
    for row in keyMatrix:
        if len(row) != n:
            raise ValueError("Key matrix must be square")

    # Convert key matrix to a NumPy array
    keyMatrix = np.array(keyMatrix)

    # Compute the modular inverse of the key matrix
    keyMatrixInv = modularInverse(keyMatrix, 26)

    # Convert cipherText to numerical values (A=0, B=1, ..., Z=25)
    cipherTextNumbers = [ord(char) - ord('A') for char in cipherText]

    # Divide cipherText into blocks of size n
    blocks = [cipherTextNumbers[i:i + n] for i in range(0, len(cipherTextNumbers), n)]

    # Decrypt each block
    plainText = ''
    for block in blocks:
        # Convert block to a NumPy column vector
        blockVector = np.array(block).reshape(n, 1)

        # Multiply inverse key matrix with block vector and take modulo 26
        decryptedVector = np.dot(keyMatrixInv, blockVector) % 26

        # Convert numerical values back to letters
        plainText += ''.join(chr(int(num) + ord('A')) for num in decryptedVector.flatten())

    return plainText

if __name__ == "__main__":
    key = [[3, 3], [2, 5]]  # Key matrix

    choice = ''

    while choice not in ['E', 'D']:
        choice = input("Do you want to (E)ncrypt or (D)ecrypt? ").strip().upper()
        if choice == 'E':
            plainText = input("Enter the plainText to encrypt: ").strip()
            cipherText = hillCipherEncrypt(plainText, key)
            print(f"PlainText: {plainText}")
            print(f"CipherText: {cipherText}")
        elif choice == 'D':
            cipherText = input("Enter the cipherText to decrypt: ").strip()
            plainText = hillCipherDecrypt(cipherText, key)
            print(f"CipherText: {cipherText}")
            print(f"Decrypted PlainText: {plainText}")
        else:
            print("Invalid choice. Please enter 'E' to encrypt or 'D' to decrypt.")