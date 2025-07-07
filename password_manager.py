from cryptography.fernet import Fernet
import json
import os

# === Generate and Save the Encryption Key ===
def create_master_key():
    secret_key = Fernet.generate_key()
    with open("master.key", "wb") as key_file:
        key_file.write(secret_key)

# === Load the Master Encryption Key ===
def get_master_key():
    return open("master.key", "rb").read()

# === Encrypt the Password using the Key ===
def encrypt_text(plain_text, key):
    return Fernet(key).encrypt(plain_text.encode()).decode()

# === Decrypt the Password using the Key ===
def decrypt_text(encrypted_text, key):
    return Fernet(key).decrypt(encrypted_text.encode()).decode()

# === Save New Account Details ===
def save_account(site_name, user_email, user_password, key):
    encrypted_password = encrypt_text(user_password, key)
    credentials = {}

    if os.path.exists("accounts.json"):
        with open("accounts.json", "r") as file:
            credentials = json.load(file)

    credentials[site_name] = {
        "email": user_email,
        "password": encrypted_password
    }

    with open("accounts.json", "w") as file:
        json.dump(credentials, file, indent=4)

# === Display All Stored Accounts ===
def show_all_accounts(key):
    if not os.path.exists("accounts.json"):
        print("No saved accounts found.")
        return

    with open("accounts.json", "r") as file:
        credentials = json.load(file)

    for site, details in credentials.items():
        try:
            decrypted_password = decrypt_text(details['password'], key)
            print(f"📌 {site} | {details['email']} | {decrypted_password}")
        except:
            print(f"⚠️ {site} | {details['email']} | [Invalid decryption key]")

# === Main Menu for User Interaction ===
def main():
    if not os.path.exists("master.key"):
        print("🔐 No master key found. Creating one now...")
        create_master_key()

    master_key = get_master_key()

    while True:
        print("\nWhat would you like to do?")
        print("1️⃣  Add a new account")
        print("2️⃣  View all saved accounts")
        print("3️⃣  Exit")

        user_choice = input("👉 Enter your choice (1/2/3): ")

        if user_choice == "1":
            site = input("Enter the site or app name: ")
            email = input("Enter your email or username: ")
            password = input("Enter your password: ")
            save_account(site, email, password, master_key)
            print("✅ Account saved!")
        elif user_choice == "2":
            show_all_accounts(master_key)
        elif user_choice == "3":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
