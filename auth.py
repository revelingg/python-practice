
from day1project import score_checker
import os
import json 
import hashlib, secrets
from getpass import getpass


FILENAME = "users.json"

def register(users):
    while True:
        username = input("Username: ").strip().lower()
                
        if not username:
            print("Username can't be empty")
        elif username in users:
            print("That user is already taken try again")
        else:
            break 
                
    score = 0
    while score <50:
            pw = getpass("Password:")
            score,missing = score_checker(pw)
            if score < 50:
                print(f"Score is less than 50 {score}: Needs: {", ".join(missing)}. Try again.")
            else:
              break
    salt = secrets.token_hex(16)
    hashed = hash_password(pw, salt)
            
    users[username] = {"salt": salt, "hash":hashed}
    save_users(users)
    print("Registered!\n")
    
    
def login(users):
    for _ in range(3):
        username = input("Username: ").strip().lower()
        pw = getpass("Password: ")
        
        record = users.get(username) #returns none if it doenst exist
        
        if record is not None:
            attempt = hash_password(pw, record["salt"])
            if secrets.compare_digest(attempt, record["hash"]):
                print("Login Success!")
                return True
        print("Invalid username or passsword, try again.")
    print("Too many attempts")
    return False 


def load_users():
    #checks to see if it exists
    if not os.path.exists(FILENAME):
        return dict()
    
    #reads the file and stores it
    with open(FILENAME, "r") as file:
        return json.load(file)

def save_users(user):
    #saves the user
    with open(FILENAME,"w" ) as file:
        json.dump(user, file, indent=4)
      
def hash_password(pw, salt):
    return hashlib.pbkdf2_hmac("sha256", pw.encode(), salt.encode(), 100_000).hex()
        
def main():
    users = load_users()
    print("Welcome to the Login Sim\n Pick an Action")
    print("Option 1: Register\nOption 2: Login\nOption 3: Quit")
  

    while True:
        choice = (input("What is your choice: "))
        if choice == "1":
            print("Registering....\n\n")
            register(users)
        elif choice == "2":
            login(users)   
        elif choice == "3":
            break
        else: 
            print("Invalid Choice")
        
        
        
                
                
        
if __name__ == "__main__":
    main()