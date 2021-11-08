from base64 import b64decode, b64encode

# // Namespace: MX.Core.Crypto.StringCipher
BlockSize: int = 128
Keysize: int = 128
DerivationIterations: int = 1000


def Encrypt(plainText: str, passPhrase: str) -> str:
    pass


def Decrypt(cipherText: str, passPhrase: str) -> str:
    rawCipherText = b64decode(cipherText)


def GenerateRandomEntropy() -> bytes:
    pass


def EncryptStringToBytes(plainText: str, Key: bytes, IV: bytes) -> bytes:
    pass


def DecryptStringFromBytes(cipherText: bytes, Key: bytes, IV: bytes) -> str:
    pass


def AESEncrypt256(Input: str, key: str) -> str:
    pass


def AESDecrypt256(Input: str, key: str) -> bytes:
    pass
