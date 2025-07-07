# 🔐 Password Manager (CLI)

A simple and secure command-line Password Manager built in Python using **Fernet encryption**.

## 🚀 Features
- Add, encrypt, and store passwords
- View stored credentials securely
- Encrypt/decrypt using a master key
- JSON-based storage

## 🛠 Technologies
- Python
- Cryptography (Fernet)
- JSON

## 📦 How to Run

1. Install dependencies:
```
pip install cryptography
```

2. Run the script:
```
python password_manager.py
```

3. Follow the menu to store or view passwords.

> ⚠️ Note: Keep your `key.key` safe! If lost, you won't be able to decrypt your passwords.

## 📁 Files
- `password_manager.py` – Main script
- `key.key` – Master key (auto-generated)
- `passwords.json` – Encrypted storage (auto-generated)
- `requirements.txt` – Required Python packages

---
Made with ❤️ by Sanket Sharma