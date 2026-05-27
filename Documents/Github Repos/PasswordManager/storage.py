import os
from crypto import encrypt_data, decrypt_data

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

    return decrypt_data(encrypted)

def write_data(data_dict):
    encrypted = encrypt_data(data_dict)
    with open(VAULT, "wb") as f:
        f.write(encrypted)