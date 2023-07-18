import re
def check_password(password):
    # Check if password meets the length requirement
    if len(password) < 6:
        return False
    # Check if password contains at least one uppercase letter
    if not re.search(r'[A-Z]', password):
        return False
    # Check if password contains at least one lowercase letter
    if not re.search(r'[a-z]', password):
        return False
    # Check if password contains at least one digit
    if not re.search(r'\d', password):
        return False
    # Check if password contains at least one special character
    if not re.search(r'[^A-Za-z0-9]', password):
        return False
    return True
entered_password = input("Enter the password: ")
if check_password(entered_password):
    print("Valid password!")
else:
    print("Invalid password!")