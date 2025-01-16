from cryptography.fernet import Fernet

"""
# commented out as it only needs to be run once to create the key
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
"""


def load_encrypt_key():
    with open("key.key", "rb") as file:
        encrypt_key = file.read()
        return encrypt_key


def add():
    username = input("Username: ")
    password = input("Password: ")

    with open("password.txt", "a") as f:
        f.write(f"{username}|{fer.encrypt(password.encode()).decode()}\n")


def view():
    try:
        with open("password.txt", "r") as file:
            for line in file.readlines():
                data = line.rstrip()
                username, password = data.split("|")
                print("Username:", username, "| Password:", password)
                fer.decrypt(password.encode().decode())
    except FileNotFoundError:
        print("No password file found\n")


master_pwd = input("What is the master password? ")
key = load_encrypt_key() + master_pwd.encode()
fer = Fernet(key)


while True:
    mode = input("1. Add new password\n2. View existing passwords\n3. Quit\n")
    if mode == "1":
        add()
    elif mode == "2":
        view()
    elif mode == "3":
        exit()
    else:
        print("Invalid mode")
        continue
