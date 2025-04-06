

import user
from user import User

current_user = None

# ---------------------------------------------------------------   Main Menu
print("\n1. Play Now!")
print("2. Sign in")
print("3. Create an account\n")
menu_selection = str(input("Please select an option: [1, 2, 3]"))


match menu_selection:
    case "1":
        print("\n[1] Play Now! ")
        
        # Create a guest user_object
        current_user = User("Guest", "")
        
    case "2":
        print("\n[2] Sign in")

        # Assign user object returned by sign in function to current
        current_user = functions.sign_in()

    case "3":
        print("\n[3] Create an account]")

        # Assign user object returned by create account function to current
        current_user = functions.create_account()
        


