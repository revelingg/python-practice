#Secure password generator

from day1project import score_checker
import secrets
import string


def gen_pw(length):
    #generates the pw
    SYMBOLS = string.punctuation.replace("/", "")
    alphabet = string.ascii_letters + string.digits + SYMBOLS
    while True:
        pw = "".join(secrets.choice(alphabet) for _ in range(length))
        if (any(c.islower() for c in pw) and any(c.isupper()for c in pw) 
            and any(c.isdigit() for c in pw) and
            any (c in string.punctuation for c in pw)
            ):
            return pw

    
def main():
    #asks
 
    
    while True:
        try:
            length = int(input("What is your desired password length?: "))
            if length >= 8:
                break
            else:
                print("Try again must be at least 8")
            
        except ValueError:
            print("Invalid number")
   
    pw = gen_pw(length)
    print(f"Your password is: {pw}")
    score,missing = score_checker(pw) 
    print(f"Score: {score}/100")
    if missing:
        print("Missing:", ", ".join(missing))
    if length < 12:
        print("Tip: Use 12+ for a perfect score")
        
   
        

    
    
if __name__ == "__main__":
    main()