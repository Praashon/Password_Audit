import re
import string
import secrets

MIN_LENGTH = 14
SPECIAL_CHARS = string.punctuation

def analyse_strength(password):
    score = 0

    if len(password) >= MIN_LENGTH:
        score += 1
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"\d", password):
        score += 1
    if re.search(r"[" + re.escape(SPECIAL_CHARS) +r"]", password):
        score += 1

    return score

def generate_secured_password(length = 18):
    alphabet = string.ascii_letters + string.digits + SPECIAL_CHARS
    while True:
        password = ''.join(secrets.choice(alphabet) for _ in range (length))

        if(any(c.islower() for c in password)
           and any(c.isupper() for c in password)
           and sum(c.isdigit() for c in password)
           and any (c in SPECIAL_CHARS for c in password)):
            return password
        

while True:
    print("---Password Auditor---\n")
    user_input = input("Enter the Password to test (or q to quit): ")

    if user_input.lower() == "q":
        print("\nExiting Program. Stay Secure!")
        break
    
    strength_score = analyse_strength(user_input)

    if strength_score == 4:
        print("\nExcellent! Your Password Is Secure :)")
    else:
        print(f"\nOpps! Your Password got {strength_score}/4 Checks!")
        print("\nIt's Super Vulnerable!")

        ask_user = input("\nWould you like to Generate a Strong Password (y/n): ")
        if ask_user.lower() in ["yes", "y"]:
            print("\n---GENERATING---")
            suggested_password = generate_secured_password()
            print(f"\nSuggested Password: {suggested_password}\n")
        else:
            print("\nThank You For Using Password Audit!\n")
            continue