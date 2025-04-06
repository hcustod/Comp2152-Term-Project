import random
from explore_map import start_explore_map
import functions

def get_valid_input(prompt, valid_range, error_message):
    """Handles input validation."""
    while True:
        user_input = input(prompt)
        if user_input.isdigit() and int(user_input) in valid_range:
            return int(user_input)
        else:
            print(error_message)

def attack(attack_strength, health_points):
    """Simulates an attack on health points based on strength."""
    damage = random.randint(1, attack_strength)
    health_points -= damage
    print(f"Attack damage: {damage}, Remaining health: {health_points}")
    return health_points

def main_game():
    # Define Dice, Weapons, Loot, etc.
    small_dice_options = list(range(1, 7))
    big_dice_options = list(range(1, 21))
    weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear Bomb"]
    loot_options = ["Health Potion", "Poison Potion", "Secret Note", "Leather Boots", "Flimsy Gloves"]
    belt = []
    monster_powers = {
        "Fire Magic": 2,
        "Freeze Time": 4,
        "Super Hearing": 6
    }

    # Get valid combat strength input
    combat_strength = get_valid_input("Enter your combat Strength (1-6): ", range(1, 7), "Please enter a valid combat strength between 1 and 6.")
    m_combat_strength = get_valid_input("Enter the monster's combat Strength (1-6): ", range(1, 7), "Please enter a valid monster combat strength between 1 and 6.")

    # Weapon roll
    print("    ------------------------------------------------------------------")
    print("    |", end="    ")
    input("Roll the dice for your weapon (Press enter)")

    # Weapon Roll ASCII Art
    ascii_image5 = """
              , %               .           
   *      @./  #         @  &.(         
  @        /@   (      ,    @       # @ 
  @        ..@#% @     @&*#@(         % 
   &   (  @    (   / /   *    @  .   /  
     @ % #         /   .       @ ( @    
                 %   .@*                
               #         .              
             /     # @   *              
                 ,     %                
            @&@           @&@        
            """
    print(ascii_image5)
    
    weapon_roll = random.choice(small_dice_options)
    combat_strength = min(6, combat_strength + weapon_roll)
    print("    |    The hero's weapon is " + str(weapons[weapon_roll - 1]))

    # Adjust combat strength
    functions.adjust_combat_strength(combat_strength, m_combat_strength)

    print("    ------------------------------------------------------------------")
    print("    |", end="    ")
    input("Analyze the Weapon roll (Press enter)")
    print("    |", end="    ")
    if weapon_roll <= 2:
        print("--- You rolled a weak weapon, friend")
    elif weapon_roll <= 4:
        print("--- Your weapon is meh")
    else:
        print("--- Nice weapon, friend!")

    if weapons[weapon_roll - 1] != "Fist":
        print("    |    --- Thank goodness you didn't roll the Fist...")

    # Loot collection
    print("    ------------------------------------------------------------------")
    print("    |", end="    ")
    input("Roll the dice for your health points (Press enter)")
    health_points = random.choice(big_dice_options)
    print("    |    Player rolled " + str(health_points) + " health points")

    print("    |", end="    ")
    input("Roll the dice for the monster's health points (Press enter)")
    m_health_points = random.choice(big_dice_options)
    print("    |    Player rolled " + str(m_health_points) + " health points for the monster")

    print("    ------------------------------------------------------------------")
    print("    |    !!You find a loot bag!! You look inside to find 2 items:")
    print("    |", end="    ")
    input("Roll for first item (enter)")

    loot_options, belt = functions.collect_loot(loot_options, belt)

    print("    ------------------------------------------------------------------")
    print("    |", end="    ")
    input("Roll for second item (Press enter)")
    loot_options, belt = functions.collect_loot(loot_options, belt)

    print("    |    You're super neat, so you organize your belt alphabetically:")
    belt.sort()
    print("    |    Your belt: ", belt)

    belt, health_points = functions.use_loot(belt, health_points)

    print("    ------------------------------------------------------------------")
    print("    |", end="    ")
    input("Analyze the roll (Press enter)")
    print("    |    --- You are matched in strength: " + str(combat_strength == m_combat_strength))
    print("    |    --- You have a strong player: " + str((combat_strength + health_points) >= 15))

    # Monster's Magic Power
    print("    |", end="    ")
    input("Roll for Monster's Magic Power (Press enter)")

    # Monster Power ASCII Art
    ascii_image4 = """
                @%   @                       
         @     @                        
             &                          
      @      .                          

     @       @                    @     
              @                  @      
      @         @              @  @     
       @            ,@@@@@@@     @      
         @                     @        
            @               @           
                 @@@@@@@                
                                      """
    print(ascii_image4)

    power_roll = random.choice(list(monster_powers.keys()))
    m_combat_strength += monster_powers[power_roll]
    print("    |    The monster's combat strength is now " + str(m_combat_strength) + " using the " + power_roll + " magic power")

    # Dream levels interaction
    num_dream_lvls = -1
    while (num_dream_lvls < 0 or num_dream_lvls > 3):
        print("    |", end="    ")
        num_dream_lvls = input("How many dream levels do you want to go down? (Enter a number 0-3)")

        if ((num_dream_lvls == "")):
            num_dream_lvls = -1
            print("Number entered must be a whole number between 0-3 inclusive, try again")
        else:
            num_dream_lvls = int(num_dream_lvls)

            if ((num_dream_lvls < 0) or (num_dream_lvls > 3)):
                num_dream_lvls = -1
                print("Number entered must be a whole number between 0-3 inclusive, try again")
            elif (not num_dream_lvls == 0):
                health_points -= 1
                crazy_level = functions.inception_dream(num_dream_lvls)
                combat_strength += crazy_level
                print("combat strength: " + str(combat_strength))
                print("health points: " + str(health_points))
        print("num_dream_lvls: ", num_dream_lvls)

    # Battle Setup
    print("    ------------------------------------------------------------------")
    print("    |    You meet the monster. FIGHT!!")
    while m_health_points > 0 and health_points > 0:
        print("    |", end="    ")
        input("Roll to see who strikes first (Press Enter)")

        attack_roll = random.choice(small_dice_options)
        if not (attack_roll % 2 == 0):
            print("    |", end="    ")
            input("You strike (Press enter)")
            m_health_points = functions.hero_attacks(combat_strength, m_health_points)
            if m_health_points == 0:
                num_stars = 3
            else:
                print("    |", end="    ")
                print("------------------------------------------------------------------")
                input("    |    The monster strikes (Press enter)!!!")
                health_points = functions.monster_attacks(m_combat_strength, health_points)
                if health_points == 0:
                    num_stars = 1
                else:
                    num_stars = 2
        else:
            print("    |", end="    ")
            input("The Monster strikes (Press enter)")
            health_points = functions.monster_attacks(m_combat_strength, health_points)
            if health_points == 0:
                num_stars = 1
            else:
                print("    |", end="    ")
                print("------------------------------------------------------------------")
                input("The hero strikes!! (Press enter)")
                m_health_points = functions.hero_attacks(combat_strength, m_health_points)
                if m_health_points == 0:
                    num_stars = 3
                else:
                    num_stars = 2

    # Determine winner and stars
    if(m_health_points <= 0):
        winner = "Hero"
    else:
        winner = "Monster"

    tries = 0
    input_invalid = True
    while input_invalid and tries in range(5):
        print("    |", end="    ")
        hero_name = input("Enter your Hero's name (in two words)")
        name = hero_name.split()
        if len(name) != 2:
            print("    |    Please enter a name with two parts (separated by a space)")
            tries += 1
        else:
            if not name[0].isalpha() or not name[1].isalpha():
                print("    |    Please enter an alphabetical name")
                tries += 1
            else:
                short_name = name[0][0:2:1] + name[1][0:1:1]
                print("    |    I'm going to call you " + short_name + " for short")
                input_invalid = False

    # Save the game
    if not input_invalid:
        stars_display = "*" * num_stars
        print("    |    Hero " + short_name + " gets <" + stars_display + "> stars")
        functions.save_game(winner, hero_name=short_name, num_stars=num_stars)


if __name__ == "__main__":
    while True:
        print("\n=== Main Menu ===")
        print("1. Start Battle")
        print("2. Explore Map")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            main_game()
        elif choice == "2":
            start_explore_map()  # Call the updated function
        elif choice == "3":
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice. Try again.")
