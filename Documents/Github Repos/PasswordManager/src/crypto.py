from cryptography.fernet import Fernet
import json

KEY_FILE = "data/key.key"

def load_key():
    with open(KEY_FILE, "rb") as f:
        return f.read()

def encrypt(data: bytes) -> bytes:
    key = load_key()
    f = Fernet(key)
    return f.encrypt(data)

def decrypt(token: bytes) -> bytes:
    key = load_key()
    f = Fernet(key)
    return f.decrypt(token)