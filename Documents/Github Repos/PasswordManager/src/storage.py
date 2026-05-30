import os
import json
from src.crypto import encrypt, decrypt

VAULT = "data/vault.enc"

def read_data():
    # If vault doesn't exist yet, return empty dict
    if not os.path.exists(VAULT):
        return {}

    with open(VAULT, "rb") as f:
        encrypted = f.read()

    # If file is empty, return empty dict
    if not encrypted.strip():
        return {}

    # decrypt() returns bytes → decode → load JSON
    decrypted_bytes = decrypt(encrypted)
    decrypted_text = decrypted_bytes.decode("utf-8")
    return json.loads(decrypted_text)

def write_data(data_dict):
    # Convert dict → JSON → bytes → encrypt
    json_text = json.dumps(data_dict)
    encrypted = encrypt(json_text.encode("utf-8"))

    with open(VAULT, "wb") as f:
        f.write(encrypted)