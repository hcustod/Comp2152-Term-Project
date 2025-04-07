import random
import functions

small_dice = list(range(1, 7))

def run_combat(party, monster, belt, monsters_killed=0):
    print("    ------------------------------------------------------------------")
    print("    |    You meet the monster. FIGHT!!")

    print("    |", end="    ")
    input("Roll to see who strikes first (Press Enter)")
    party_roll = random.choice(small_dice)
    monster_roll = random.choice(small_dice)

    print(f"    |    Party rolls: {party_roll}")
    print(f"    |    Monster rolls: {monster_roll}")

    party_turn = party_roll >= monster_roll
    print("    |    Party strikes first!" if party_turn else "    |    Monster strikes first!")

    while monster.health_points > 0 and any(hero.health_points > 0 for hero in party):
        if party_turn:
            for hero in [h for h in party if h.health_points > 0]:
                print("    |", end="    ")
                input(f"{hero.name} attacks the monster! (Press Enter)")
                monster.health_points = functions.hero_attacks(hero, hero.combat_strength, monster.health_points)

                if monster.health_points <= 0:
                    print(f"Monster defeated by {hero.name}!")
                    hero.wins.append("win")
                    recent_wins = [w for w in hero.wins[-3:] if w == "win"]
                    if len(recent_wins) >= 2 and not hero.special_ability:
                        choice = input(f"{hero.name} is eligible to evolve. Evolve now? (y/n): ").strip().lower()
                        if choice == 'y':
                            hero.evolve()
                    break
        else:
            strikes = 2 if random.random() < 0.3 else 1
            for _ in range(strikes):
                alive_heroes = [h for h in party if h.health_points > 0]
                if not alive_heroes:
                    break
                target = random.choice(alive_heroes)
                print("    |", end="    ")
                input(f"Monster strikes {target.name}! (Press Enter)")
                damage = monster.combat_strength
                target.health_points = max(0, target.health_points - damage)
                print(f"{target.name} took {damage} damage. HP is now {target.health_points}")

                if target.health_points == 0:
                    monster.survivals.append("survived")
                    recent_survivals = [s for s in monster.survivals[-3:] if s == "survived"]
                    if len(recent_survivals) >= 2 and not monster.evolved:
                        choice = input("Monster is eligible to evolve. Evolve now? (y/n): ").strip().lower()
                        if choice == 'y':
                            monster.evolve()

        for hero in party:
            if hero.health_points > 0:
                display_status(hero, monster)

        party_turn = not party_turn
        print("    ------------------------------------------------------------------")

    winner = "Heroes" if monster.health_points == 0 else "Monster"
    heroes_alive = [h for h in party if h.health_points > 0]

    if winner == "Heroes":
        monsters_killed += 1
        num_stars = 3 if len(heroes_alive) == len(party) else 2 if heroes_alive else 1
    else:
        num_stars = 0

    return winner, num_stars, monsters_killed


def display_status(hero, monster):
    print("\n=== Evolution Status ===")
    print(f"Hero - Level: {hero.level}, Combat Strength: {hero.combat_strength}, Special Ability: {'Yes' if hero.special_ability else 'No'}")
    print(f"Monster - Level: {monster.level}, Combat Strength: {monster.combat_strength}, Evolved: {'Yes' if monster.evolved else 'No'}")
    print("========================\n")

