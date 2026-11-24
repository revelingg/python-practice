#This is a password strength checker point based systme

#11/24/26
import sys
import string
from getpass import getpass


COMMON_PASSWORDS = {
    "password", "password1", "password123", "123456", "12345678",
    "123456789", "1234567890", "qwerty", "qwerty123", "abc123",
    "letmein", "welcome", "admin", "admin123", "iloveyou",
    "monkey", "dragon", "football", "baseball", "sunshine",
    "princess", "login", "master", "shadow", "trustno1",
    "passw0rd", "starwars", "111111", "000000", "changeme",
}




def has_digit(pw):
    return any(char.isdigit() for char in pw)
    

def is_common(pw):
    return  pw.lower()  in COMMON_PASSWORDS
    
def has_lower(pw):
    return any(char.islower() for char in pw)

def has_upper(pw):
    return  any(char.isupper() for char in pw)
    
def symbol(pw):
    return any(char in string.punctuation for char in pw)


def score_checker(pw):
    missing = []
    score = 0
    if is_common(pw):
            
            return 0, ["Common Password"]
            
    if len(pw) >= 8:
            score += 20
    else:
            missing.append("Length 8+")
        
    if len(pw) >= 12:
            score += 15
    else:
            missing.append("Length 12+")
            
    if has_upper(pw):
            score += 15
    else:
            missing.append("upper")
    if has_lower(pw):
                score += 15
    else:
            missing.append("lower")
    if has_digit(pw):
            score += 15
    else:
            missing.append("digits")
        
    if symbol(pw):
            score += 20
    else:
            missing.append("symbol")
            
    return score, missing
if __name__ == "__main__":

    pw = getpass("Enter your password: ") 
    score,missing = score_checker(pw)
    
    #Ratings
    if score <= 49:
        rating = "Weak"
    elif score <= 79:
        rating = "Okay"
    else:
        rating = "Strong"
    
    print("Missing:", ", ".join(missing) if missing else "nothing")
    print(f"Score: {score}/100 {rating}")