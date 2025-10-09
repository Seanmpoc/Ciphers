import numpy as np

def hillCipherEncrypt(plaintext, keyMatrix):
    """
    Encrypts the plaintext using the Hill Cipher algorithm.

    Args:
        plaintext (str): The plaintext message to encrypt.
        key_matrix (list of lists): The square matrix used as the encryption key.

    Returns:
        str: The encrypted ciphertext.
    """
    # Ensure the key matrix is square
    n = len(keyMatrix)
    for row in keyMatrix:
        if len(row) != n:
            raise ValueError("Key matrix must be square")

    # Convert plaintext to uppercase
    plaintext = ''.join(plaintext.upper())

    # Pad plaintext with 'X' if its length is not a multiple of the matrix size
    while len(plaintext) % n != 0:
        plaintext += 'X'

    # Convert plaintext to unicode values
    plaintextUnicode = [ord(char) - ord('A') for char in plaintext]

    # Divide plaintext into segments of size n
    segments = [plaintextUnicode[i:i + n] for i in range(0, len(plaintextUnicode), n)]

    # Convert key matrix to a NumPy array
    keyMatrix = np.array(keyMatrix)

    # Encrypt each block
    ciphertext = ''
    for segment in segments:
        # Convert block to a NumPy column vector
        blockVector = np.array(segment).reshape(n, 1)

        encryptedVector = np.dot(keyMatrix, blockVector) % 26

        # Convert unicode values back to letters
        ciphertext += ''.join(chr(int(num) + ord('A')) for num in encryptedVector.flatten())

    return ciphertext

if __name__ == "__main__":

    key = [[6, 24], [1, 13]]

    plaintext = "HelloWorld"
    ciphertext = hillCipherEncrypt(plaintext, key)
    print(f"Plaintext: {plaintext}")
    print(f"Ciphertext: {ciphertext}")