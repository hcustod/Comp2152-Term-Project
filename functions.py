import random
from user import User

def use_loot(belt, health_points):
    good_loot_options = ["Health Potion", "Leather Boots"]
    bad_loot_options = ["Poison Potion"]

    print("    |    !!You see a monster in the distance! So you quickly use your first item:")
    first_item = belt.pop(0)
    if first_item in good_loot_options:
        health_points = min(20, (health_points + 2))
        print("    |    You used " + first_item + " to up your health to " + str(health_points))
    elif first_item in bad_loot_options:
        health_points = max(0, (health_points - 2))
        print("    |    You used " + first_item + " to hurt your health to " + str(health_points))
    else:
        print("    |    You used " + first_item + " but it's not helpful")
    return belt, health_points


def collect_loot(loot_options, belt):
    ascii_image3 = """
                      @@@ @@                
             *# ,        @              
           @           @                
                @@@@@@@@                
               @   @ @% @*              
            @     @   ,    &@           
          @                   @         
         @                     @        
        @                       @       
        @                       @       
        @*                     @        
          @                  @@         
              @@@@@@@@@@@@          
              """
    print(ascii_image3)
    loot_roll = random.choice(range(1, len(loot_options) + 1))
    loot = loot_options.pop(loot_roll - 1)
    belt.append(loot)
    print("    |    Your belt: ", belt)
    return loot_options, belt


def hero_attacks(combat_strength, m_health_points):
    ascii_image = """
                                @@   @@ 
                                @    @  
                                @   @   
               @@@@@@          @@  @    
            @@       @@        @ @@     
           @%         @     @@@ @       
            @        @@     @@@@@     
               @@@@@        @@       
               @    @@@@                
          @@@ @@                        
       @@     @                          
   @@*       @                          
   @        @@                          
           @@                                                    
         @   @@@@@@@                    
        @            @                   
      @              @                  

  """
    print(ascii_image)
    print("    |    Player's weapon (" + str(combat_strength) + ") ---> Monster (" + str(m_health_points) + ")")
    if combat_strength >= m_health_points:
        m_health_points = 0
        print("    |    You have killed the monster")
    else:
        m_health_points -= combat_strength

        print("    |    You have reduced the monster's health to: " + str(m_health_points))
    return m_health_points


def monster_attacks(m_combat_strength, health_points):
    ascii_image2 = """                                                                 
           @@@@ @                            
      (     @*&@  ,                          
    @               %                        
     &#(@(@%@@@@@*   /                       
      @@@@@.                                 
               @       /                    
                %         @                  
            ,(@(*/           %               
               @ (  .@#                 @   
                          @           .@@. @
                   @         ,              
                      @       @ .@          
                             @              
                          *(*  *      
             """
    print(ascii_image2)
    print("    |    Monster's Claw (" + str(m_combat_strength) + ") ---> Player (" + str(health_points) + ")")
    if m_combat_strength >= health_points:
        health_points = 0
        print("    |    Player is dead")
    else:
        health_points -= m_combat_strength
        print("    |    The monster has reduced Player's health to: " + str(health_points))
    return health_points

def inception_dream(num_dream_lvls):
    num_dream_lvls = int(num_dream_lvls)
    if num_dream_lvls == 1:
        print("    |    You are in the deepest dream level now")
        print("    |", end="    ")
        input("Start to go back to real life? (Press Enter)")
        print("    |    You start to regress back through your dreams to real life.")
        return 2
    else:
        return 1 + int(inception_dream(num_dream_lvls - 1))


def save_game(winner, hero_name="", num_stars=0):
    with open("save.txt", "a") as file:
        if winner == "Hero":
            file.write(f"Hero {hero_name} has killed a monster and gained {num_stars} stars.\n")
        elif winner == "Monster":
            file.write("Monster has killed the hero previously\n")


def save_game_v2(current_user):

        # Collect dictionary of stats from user object
        user_stats = current_user.return_stats()

        # Save info to text file
        with open("save.txt", "a") as file:
            file.write(f"hero_name:{current_user.username} | winner:{user_stats['winner']} | stars:{user_stats['stars']} | weapon:{user_stats['weapon']} | loot:{user_stats['loot'][0]}, {user_stats['loot'][1]};\n")
            
            if user_stats["winner"] == "Monster":
                file.write("Monster has killed the hero previously\n")
                
            print("Game saved to file successfully\n\n")

def load_game():
    try:
        with open("save.txt", "r") as file:
            print("    |    Loading from saved file ...")
            lines = file.readlines()
            if lines:
                last_line = lines[-1].strip()
                print(last_line)
                return last_line
    except FileNotFoundError:
        print("No previous game found. Starting fresh.")
        return None

def adjust_combat_strength(combat_strength, m_combat_strength):
    last_game = load_game()
    if last_game:
        if "Hero" in last_game and "gained" in last_game:
            num_stars = int(last_game.split()[-2])
            if num_stars > 3:
                print("    |    ... Increasing the monster's combat strength since you won so easily last time")
                m_combat_strength += 1
        elif "Monster has killed the hero" in last_game:
            combat_strength += 1
            print("    |    ... Increasing the hero's combat strength since you lost last time")
        else:
            print("    |    ... Based on your previous game, neither the hero nor the monster's combat strength will be increased")

# Eric Laudrum:
# Create an account file in accounts.txt
def create_account():
        global current_user
   
        # Wait until an accepted name has been submitted
        accepted_name = False
        while (not accepted_name):
            
            # Enter and Verify Username
            print("What is your name hero?")
            username = input("Please enter a name: ")

            # Initialize user object (without password at first)
            user_object = User(username, "")

            # Check if username is available
            if user_object.username_available():
                break

            print("That name is not available.\n")


        # Enter Verify Password
        password = input("Enter a password: ")
        password_confirmation = input("Confirm your password: ")

        # User successfully confirms password
        if user_object.confirm_passwords_match(password, password_confirmation):
            
            # Assign password to user object
            user_object.password = password

            # Create a user account
            user_object.create_user_account()
            print("Account created.")

            # Set the user object as the current user
            current_user = user_object
            print(f"Welcome {current_user.username}")
        
        else:
            print("Error: Passwords do not match")

        return current_user


# Sign in function
def sign_in():
    global current_user
    
    signed_in = False

    while not signed_in:
        # Input sign in details
        username = input("Enter a username: ")
        password = input("Enter a password: ")

        # Initialize user object
        user_object = User(username, password)
        print("user object created")

        # Sign in successful
        if user_object.verify_login(): 
            
            # Update global variable
            current_user = user_object

            signed_in = True

            # Print Greeting and Stats
            user_object.opening_stats()

        # Sign in failed 
        else:
            print("Sign in failed. Try again!")

    return current_user
