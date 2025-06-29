from cryptography.fernet import Fernet
from tkinter import filedialog
import os

KEY_FILE = "secret.key"

def get_key():
    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as f:
            f.write(key)
    else:
        with open(KEY_FILE, "rb") as f:
            key = f.read()
    return Fernet(key)

def encrypt_files():
    fernet = get_key()
    file_paths = filedialog.askopenfilenames(title="Select files to encrypt")

    for file_path in file_paths:
        with open(file_path, "rb") as f:
            data = f.read()
        encrypted = fernet.encrypt(data)
        with open(file_path, "wb") as f:
            f.write(encrypted)
    print("Files encrypted successfully.")

def decrypt_files():
    fernet = get_key()
    file_paths = filedialog.askopenfilenames(title="Select files to decrypt")

    for file_path in file_paths:
        with open(file_path, "rb") as f:
            data = f.read()
        try:
            decrypted = fernet.decrypt(data)
            with open(file_path, "wb") as f:
                f.write(decrypted)
        except:
            print(f"Failed to decrypt {file_path} - Possibly already decrypted or wrong key.")
    print("Decryption complete.")
