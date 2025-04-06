from partyGenerator.models.monster import Monster
from dreamLevels import run_dream_levels
import random
import functions

small_dice = list(range(1, 7))

def run_combat(party, monster, belt):
    print("    ------------------------------------------------------------------")
    print("    |    You meet the monster. FIGHT!!")

    # Roll once before combat loop
    print("    |", end="    ")
    input("Roll to see who strikes first (Press Enter)")
    party_roll = random.choice(small_dice)
    monster_roll = random.choice(small_dice)

    print(f"    |    Party rolls: {party_roll}")
    print(f"    |    Monster rolls: {monster_roll}")

    # Party wins ties
    party_turn = party_roll >= monster_roll

    if party_turn:
        print("    |    Party strikes first!")
    else:
        print("    |    Monster strikes first!")

    # Main combat loop
    while monster.health_points > 0 and any(hero.health_points > 0 for hero in party):

        if party_turn:
            # List comprehension
            for hero in [h for h in party if h.health_points > 0]:
                if hero.health_points <= 0:
                    continue
                print("    |", end="    ")
                input(f"{hero.name} attacks the monster! (Press Enter)")
                monster.health_points = functions.hero_attacks(hero.combat_strength, monster.health_points)
                if monster.health_points <= 0:
                    print(f"Monster defeated by {hero.name}!")
                    break
        else:
            strikes = 2 if random.random() < 0.3 else 1
            for _ in range(strikes):
                alive_heroes = [hero for hero in party if hero.health_points > 0]
                if not alive_heroes:
                    break
                target = random.choice(alive_heroes)
                print("    |", end="    ")
                input(f"Monster strikes {target.name}! (Press Enter)")
                target.health_points = functions.monster_attacks(monster.combat_strength, target.health_points)
                if target.health_points <= 0:
                    print(f"{target.name} has fallen!")

        # Flip turns
        party_turn = not party_turn

        print("    ------------------------------------------------------------------")

    winner = "Heroes" if monster.health_points <= 0 else "Monster"

    # List comprehension
    heroes_alive = [h for h in party if h.health_points > 0]

    if winner == "Heroes":
        if len(heroes_alive) == len(party):
            num_stars = 3
        elif len(heroes_alive) > 0:
            num_stars = 2
        else:
            num_stars = 1
    else:
        num_stars = 0

    return winner, num_stars
