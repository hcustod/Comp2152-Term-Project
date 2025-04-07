import os

class User:
    # Initialize User object
    def __init__(self, username, password):
        self.username = username
        self.password = password

        # Create a stats dictionary to hold game stats
        self.stats = {
            "hero_name":"",
            "weapon":"",
            "loot":[],
            "stars":"",
            "winner":""
        }

    # Delete User object
    def __del__(self):
         print("User object is being deleted...")

    # Return string
    def __str__(self):
        return f"User(username={self.username})"
    
    def return_stats(self):
        return self.stats
         

    # Create and log user account information
    def create_user_account(self):
        # Create accounts.txt if it doesn't already exist 
        if not os.path.exists("accounts.txt"):
            with open("accounts.txt", "w") as file:
                print("Creating accounts.txt file...")

        # Append account information to file
        with open("accounts.txt", "a+") as file:
            print("Appending to accounts.txt...")
            file.writelines(f"{self.username}::{self.password}\n")

    # Check availability of username
    def username_available(self):
        # Check if file exists
        if not os.path.exists("accounts.txt"):    
            # If no file exists, all usernames are available
            return True
        
        with open("accounts.txt", "r") as file:
            print("Checking availability of username...")
            
            # Iterate through account file
            for line in file.readlines():
                # print(f"line.strip(): {line.strip()}\n")

                # Collect the first position of [username, password]
                username_on_file = line.strip().split("::")[0]
                

                # Account name is not available
                if(username_on_file == self.username):
                    print(f"\nI'm sorry, we already have a {self.username}. Do you go by any other name?\n")
                    return False
                
            print(f"Welcome aboard {self.username}! ") 
            return True
        
    # Verify user's password matches the second entry
    def confirm_passwords_match(self, password, confirm_password):
        if password == confirm_password:
            return True
        else:
            print("Error: Password do not match")
            return False
            

    # Verify login attempt
    def verify_login(self):
        # Verify accounts file exists.
        if not os.path.exists("accounts.txt"):
            print("Error: Accounts could not be found.")
            return False
        
        # Open and iterate through the accounts file
        with open("accounts.txt", "r") as file:
        
            for line in file.readlines():
                    
                #print(f"line in file.readlines: >>{line}<<")
                # Collect username and password variables
                username_on_file = line.strip().split("::")[0]
                password_on_file = line.strip().split("::")[1]

                # Return true when a match is found
                if(self.username == username_on_file and self.password == password_on_file):
                    print("Account verified.")
                    return True
                
            # No accounts match username and password
            print("Error: Invalid username or password.")
            return False


    # Update stats dictionary
    def update_stats(self, key, value):

        # Append value to stat line
        if key in self.stats and value is not None:
            if type(key) is str:
                self.stats[key] = value

            elif type(key) is int:
                self.stats[key] = value

            elif type(key) is list: 
                self.stats[key].extend(value)

        else:
            print(f"Error: Stats could not be updated")




    # Display user stats
    def show_playing_card(self):
        print("\n\n////////////////////////////////////////////")
        print("               Game results")
        print(f"        {self.username}")
        for key, value in self.stats.items():
            print(f"{key}------------------{value}")

        print("\n////////////////////////////////////////////\n\n")


    # Analyzing stats
    def opening_stats(self):
        if not os.path.exists("save.txt"):
            print("error: accounts.txt could not be found")
            return
        
        wins = 0
        losses = 0
        stars = 0

        with open("save.txt", "r") as file:
            # Read one file entry
            for line in file.readlines():

                # For debug only
                #print("line in save.txt: ", line.strip())

                # Verify it is a line that carries stats
                if "Monster has killed" in line:
                    continue
                    
                # Initialize an empty dictionary to hold user_stats
                user_stats = {}
                
                # Split the line into separate categories
                for category in line.split(" | "):
                    
                    # Split the categories into key and value
                    item = category.split(":")

                    item_key = item[0].strip()
                    item_value = item[1].strip()

                    # Add to dictionary for handling
                    user_stats[item_key] = item_value

                # If the user does not match, continue
                if (user_stats['hero_name'] == self.username):
                    stars += int(user_stats['stars'])
                
                    if(user_stats['winner'] == 'Hero'):
                        wins += 1
                    elif(user_stats['winner'] == 'Monster'):
                        losses += 1

        hero_intro = f"Introducing.....\n"

       
        if(wins + losses == 0):
            hero_intro += ", a brand new contender has entered the arena."
             
        else:
            # User has a winning record
            if(wins > losses):
                if(losses >= 0 and losses < 4):
                    
                    hero_intro += ", a new Hero to the group looking to make their mark. It's... "
                elif(losses >= 4 and losses < 10):
                    hero_intro += ", the Hero other Heroes have said to look out for as up and coming.. "
                else:
                    hero_intro += ", your Hero's favourite Hero, the lengendary.... "
            elif(wins <= losses):
                if(losses < 3):
                    hero_intro += ", a new Hero who can dish it out as well as they can take it. It's... "
                elif(losses >= 3 and losses < 6):
                    hero_intro += ", a Hero with something to prove.."
                elif(losses >= 6 and losses < 10):
                    hero_intro += ", a scrappy young vet who's never THAT down and out. It's..."
                else:
                    hero_intro += ", the great equalizer.... It's.. "


            if(self.username == 'Guest'):
                hero_intro = "representing all the people who don't feel comfortable\n sharing their personal information with us.... it's "

            games_played = wins+losses
            if(games_played >= 1):
                win_loss_percent = wins / games_played * 100
                avg_stars = stars / games_played * 100


                print("====================================================================")
                print(f"                          {self.username}")
                print("====================================================================")

                print(f"{hero_intro}{self.username}")

                print(f"\nTotal wins: {wins}")
                print(f"Total losses: {losses}")
                print(f"Win/Loss {win_loss_percent}%") 

                print(f"Total stars: {stars}")
                print(f"Average stars: {avg_stars}")

                print("====================================================================")

            else:
                print("You will have stats available next game.")
            
                    
                
    