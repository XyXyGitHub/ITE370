# ============================
# SIMPLE LOGIN SYSTEM
# ============================

# Reviewer (Hiligaynon):
# Simple authentication example lang ini.
# May stored nga email kag hashed password.
# Kung sala ang password, maggwa error.

import hashlib

# ============================
# STORED USER (SIMULATION LANG)
# ============================

stored_email = "admin@gmail.com"

# Ginahash naton ang password para indi plain text
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

stored_password = hash_password("12345")  # original password is 12345

# ============================
# LOGIN FUNCTION
# ============================

def login():
    email = input("Enter Email: ")
    password = input("Enter Password: ")

    # Input Validation
    if email == "" or password == "":
        print("Error: All fields are required.")
        return

    # Authentication check
    if email == stored_email and hash_password(password) == stored_password:
        print("Login Successful ✅")
    else:
        # Error Handling
        # Reviewer:
        # Indi ginapakita kung ano gid ang sala (email or password)
        # para mas secure ang system.
        print("Error: Invalid email or password ❌")

# ============================
# RUN LOGIN
# ============================

login()