🔐Pattern Lock Encryption System🔐
A visually interactive desktop application built with Python and Tkinter that enables secure encryption and decryption of multiple files using a custom-drawn pattern lock instead of a text-based password.
✨Features:
*-* Pattern Based Security - Lock and unlock files with a 3x3 grid pattern instead of a traditional password.
*-* Multiple-File Support  -Encrypt and decrypt multiple files in one go.
*-* Encrypted Storage - Files are Safely Encrypted using the Fernet Modules from the 'Cryptography' Package.
*-* Hashed Pattern - Patterns are hashed and stored in a `.txt` file to avoid plain-text security risks.
*-* Pattern Strength Indicator - Visual feedback on the complexity of your drawn pattern.
*-* Reset Pattern Option -  Securely update your pattern after re-entering the existing one.
*-* D/E/R Modes - Choose to Decrpyt/Encrypt/Reset the Password after succesfull Pattern Entry
Tech Stack: Python 3(Language), Tinker(GUI FrameWork), Fernet-From 'Cryptography' Package (Encryption) .
Getting Started?-
1>. CLONE Repository -

git clone https://github.com/Ekshithsai/Encryption.git

cd Encryption
2>. Install Dependencies -

pip install -r req.txt

3.Run the App

python main.py

<_>Boom <_>

📂File Structure :

├── encrypt.py            # Encryption/decryption logic
├── lock_ui.py            # UI for drawing the pattern
├── main.py               # Entry point
├── utils.py              # Utilities (pattern hash handling, pattern check)
├── pattern_hash.txt      # Stores hashed pattern securely
├── req.txt               # Required packages
├── screenshots/          # Folder to store UI screenshots




