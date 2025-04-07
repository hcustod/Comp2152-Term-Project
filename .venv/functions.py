import random

def hero_attacks(hero, monster):
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

    if hasattr(hero, 'special_ability') and hero.special_ability:
        chance = random.random()
        if chance < 0.7:
            damage = hero.combat_strength + 3
            print("Hero uses evolved attack! Stronger attack!")
        else:
            damage = 0
            print("Hero's evolved ability missed!")
    else:
        damage = hero.combat_strength

    if damage >= monster.health_points:
        monster.health_points = 0
        print("The Hero has defeated the Monster!")
    else:
        monster.health_points -= damage
        print(f"The Monster's health is now {monster.health_points}")


def monster_attacks(monster, hero):
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

    damage = monster.combat_strength
    if damage >= hero.health_points:
        hero.health_points = 0
        print("The Hero has been defeated!")
    else:
        hero.health_points -= damage
        print(f"The Hero's health is now {hero.health_points}")


def display_status(hero, monster):
    print("\n=== Evolution Status ===")
    print(f"Hero - Level: {hero.level}, Combat Strength: {hero.combat_strength}, Special Ability: {'Yes' if hero.special_ability else 'No'}")
    print(f"Monster - Level: {monster.level}, Combat Strength: {monster.combat_strength}, Evolved: {'Yes' if monster.evolved else 'No'}")
    print("========================\n")


def fight_sequence(hero, monster):
    while hero.health_points > 0 and monster.health_points > 0:
        hero_attacks(hero, monster)
        if monster.health_points == 0:
            hero.wins.append("win")
            recent_wins = [w for w in hero.wins[-3:] if w == "win"]
            if len(recent_wins) >= 2 and not hero.special_ability:
                choice = input("Hero is eligible to evolve. Evolve now? (y/n): ").strip().lower()
                if choice == 'y':
                    hero.evolve()

            display_status(hero, monster)
            return "Hero Wins"

        monster_attacks(monster, hero)
        if hero.health_points == 0:
            monster.survivals.append("survived")
            recent_survivals = [s for s in monster.survivals[-3:] if s == "survived"]
            if len(recent_survivals) >= 2 and not monster.evolved:
                choice = input("Monster is eligible to evolve. Evolve now? (y/n): ").strip().lower()
                if choice == 'y':
                    monster.evolve()

            display_status(hero, monster)
            return "Monster Wins"

    return None


def save_game(monsters_killed):
    try:
        with open("game_save.txt", "w") as file:
            file.write(str(monsters_killed) + "\n")
    except Exception as e:
        print(f"Error saving game: {e}")


def load_game():
    try:
        with open("game_save.txt", "r") as file:
            return int(file.readline().strip())
    except (FileNotFoundError, ValueError):
        return 0
