import random
import functions
from partyGenerator.partyCreation import generate_party
from fightSystem import run_combat
from partyGenerator.models.monster import Monster
from dreamLevels import run_dream_levels

small_dice_options = list(range(1, 7))
big_dice_options = list(range(1, 21))
weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear Bomb"]

monster_powers = {
    "Fire Magic": 2,
    "Freeze Time": 4,
    "Super Hearing": 6
}


def main():
    print(r"""**************************************************************************************

     ____                             _   _                                     
    |  _ \ _ __ ___  __ _ _ __ ___   | | | | __ _ _ __ ___  _ __ ___   ___ _ __ 
    | | | | '__/ _ \/ _` | '_ ` _ \  | |_| |/ _` | '_ ` _ \| '_ ` _ \ / _ \ '__|
    | |_| | | |  __/ (_| | | | | | | |  _  | (_| | | | | | | | | | | |  __/ |   
    |____/|_|  \___|\__,_|_| |_| |_| |_| |_|\__,_|_| |_| |_|_| |_| |_|\___|_|      

**************************************************************************************""")

    party = generate_party()
    monster = Monster()

    loot_options = ["Health Potion", "Poison Potion", "Secret Note", "Leather Boots", "Flimsy Gloves"]
    belt = []

    for _ in range(2):
        loot_options, belt = functions.collect_loot(loot_options, belt)

    belt.sort()

    for i, hero in enumerate(party):
        if i == 0:
            belt, hero.health_points = functions.use_loot(belt, hero.health_points)

    print("    |", end="    ")
    input("Roll the dice for your weapon (Press enter)")
    weapon_roll = random.choice(small_dice_options)
    print("    |", end="    ")
    print(f"You rolled {weapon_roll} for your weapon.")

    weapon_name = weapons[weapon_roll - 1]
    first_hero = party[0]
    first_hero.combat_strength = min(6, (first_hero.combat_strength + weapon_roll))
    print("    |    The hero's weapon is " + weapon_name)

    functions.adjust_combat_strength(first_hero.combat_strength, monster.combat_strength)

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

    if weapon_name != "Fist":
        print("    |    --- Thank goodness you didn't roll the Fist...")

    print("    |", end="    ")
    input("Analyze the roll (Press enter)")
    print("    |    --- You are matched in strength: " + str(monster.combat_strength == first_hero.combat_strength))
    print(
        "    |    --- You have a strong player: " + str((first_hero.combat_strength + first_hero.health_points) >= 15))

    print("    |", end="    ")
    input("Roll for Monster's Magic Power (Press enter)")
    print("""
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
    """)
    power_roll = random.choice(list(monster_powers.keys()))
    monster.combat_strength += min(6, monster.combat_strength + monster_powers[power_roll])
    print("    |    The monster's combat strength is now " + str(
        monster.combat_strength) + " using the " + power_roll + " magic power")

    print("\n    ------------------------------------------------------------------")
    print("    |    Just before you engage in combat, a dreamy haze falls upon you...")
    num_dream_lvls = run_dream_levels(party, monster)
    if num_dream_lvls > 0:
        print("    |    You feel yourself spiraling into a dream within a dream...")
        _ = functions.inception_dream(num_dream_lvls)

    run_combat(party, monster, belt)

if __name__ == "__main__":
    main()
