import random
from src.storage import write_data, read_data

def generate_password(length=12):
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
    return "".join(random.choice(chars) for _ in range(length))

def save_entry(website, username, password):
    data = read_data()  # returns a dict
    data[website] = {
        "username": username,
        "password": password
    }
    write_data(data)  # write_data encrypts and saves

def search_entry(website):
    data = read_data()
    return data.get(website)