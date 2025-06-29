from lock_ui import PatternLockUI
from encrypt import encrypt_files, decrypt_files
from utils import hash_pattern, verify_pattern, load_hashed_pattern, save_hashed_pattern
import tkinter as tk
from tkinter import simpledialog

def on_pattern_complete(input_pattern):
    hashed = hash_pattern(input_pattern)

    if not load_hashed_pattern():
        save_hashed_pattern(hashed)
        print("Pattern set successfully!")
        return

    if verify_pattern(input_pattern):
        action = simpledialog.askstring("Select Action", "Enter D to Decrypt, E to Encrypt, R to Reset Password:").strip().upper()
        if action == 'D':
            decrypt_files()
        elif action == 'E':
            encrypt_files()
        elif action == 'R':
            new = simpledialog.askstring("Reset", "Enter NEW pattern again (e.g., 1-2-3):")
            save_hashed_pattern(hash_pattern(new))
            print("Password reset.")
        else:
            print("Invalid input")
    else:
        print("Wrong pattern!")

root = tk.Tk()
app = PatternLockUI(root, on_pattern_complete)
root.mainloop()
