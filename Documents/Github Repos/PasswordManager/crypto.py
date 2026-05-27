from cryptography.fernet import Fernet
import json 

KEY_FILE = "data/key.key"

def load_key():
    with open(KEY_FILE, "rb") as f:
        return f.read()
    
def encrypt_data(data):
    key = load_key()
    f = Fernet(key)
    return f.encrypt(json.dumps(data).encode())

def decrypt_data(token):
    key = load_key()
    f = Fernet(key)
    decrypted = f.decrypt(token).decode()
    return json.loads(decrypted)
