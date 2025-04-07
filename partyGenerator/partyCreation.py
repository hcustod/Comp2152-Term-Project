from partyGenerator.models import Hero

MAX_PARTY_SIZE = 3

def generate_party():
    while True:
        party = []
        print("**************************************************************************************")
        print("\nWelcome to Party Creation!")

        # Robust input validation for party size
        party_size = None
        while party_size is None:
            try:
                value = input(f"How many heroes would you like to create? (1 to {MAX_PARTY_SIZE}): ").strip()
                if not value.isdigit():
                    raise ValueError("Input must be a number.")
                party_size = int(value)
                if party_size < 1 or party_size > MAX_PARTY_SIZE:
                    raise ValueError(f"Please enter a number between 1 and {MAX_PARTY_SIZE}.")
            except ValueError as ve:
                print(f"Invalid input: {ve}")
                party_size = None

        for i in range(party_size):
            while True:
                print(f"\nCreating Hero {i + 1}...")
                name = input("Enter a name for your hero: ").strip()
                if not name:
                    print("Name cannot be empty. Please try again.")
                    continue

                hero = Hero(name)
                print(f"{hero.name} was born a {hero.species}.")

                print("Applying sign and species effects...")
                apply_bonuses(hero)
                hero.display_info()

                confirm = input("Are you happy with this character? (y/n): ").strip().lower()
                while confirm not in ['y', 'n']:
                    confirm = input("Please enter 'y' or 'n': ").strip().lower()

                if confirm == 'y':
                    party.append(hero)
                    break
                else:
                    print("Re-rolling this hero...")

        print("\n************************************* Party Overview *************************************")
        print("\n".join([
            f"{h.name}: {h.species} + {h.sign} -> {h.sign_description}"
            f"\nHP: {h.health_points}, STR: {h.combat_strength}"
            for h in party
        ]))


        reroll = input("\nWould you like to reroll the entire party? (y/n): ").strip().lower()
        while reroll not in ['y', 'n']:
            reroll = input("Please enter 'y' or 'n': ").strip().lower()

        if reroll != 'y':
            break

    return party


def apply_bonuses(hero):
    hp = hero.health_points
    str_ = hero.combat_strength

    if hero.sign == "The Warden":
        if hero.species in ["Human", "Elf", "Dwarf", "Fae"]:
            if hp >= 18 and str_ >= 5:
                hero.health_points = min(20, hp + 1)
                hero.combat_strength = min(6, str_ + 1)
                print("The Warden channels power to those already strong. Bonuses softened.")
            else:
                hero.health_points = min(20, hp + 3)
                hero.combat_strength = min(6, str_ + 1)
                print("The Warden grants vitality to your hero.")
        elif hero.species == "Orc":
            hero.health_points = max(0, hp - 1)
            hero.combat_strength = min(6, str_ + 2)
            print("The Warden rejects brutish power. Orc gains strength, loses health.")

    elif hero.sign == "The Seer":
        if hero.species == "Elf":
            hero.health_points = max(1, hp - 1)
            print("Elven vision comes at a price. -1 HP.")
        else:
            print("Visions flicker in your mind. No stat change.")

    elif hero.sign == "The Reaper":
        if hero.species == "Orc":
            hero.combat_strength = min(6, str_ + 2)
            print("The Reaper feeds the Orc's thirst. +2 Strength.")

    elif hero.sign == "The Phoenix":
        if hero.species == "Fae":
            import random
            roll = random.choice([-2, 4])
            hero.health_points = max(1, min(20, hp + roll))
            msg = "The Fae flares with rebirth." if roll > 0 else "The Fae burns before rising."
            print(f"{msg} {'+' if roll > 0 else ''}{roll} HP.")

    elif hero.sign == "The Architect":
        if hero.species == "Elf" and hp >= 18 and str_ >= 5:
            hero.health_points = 20
            hero.combat_strength = 6
            print("Inside you the memories of a thousand dreamers awaken. You are the Architect of the Dream.")
        else:
            print("Blueprints of destiny shift inside you. No stat bonus yet.")

    elif hero.sign == "The Vagabond":
        if hero.species == "Human":
            hero.combat_strength = min(6, str_ + 1)
            print("The Vagabond teaches streetwise strikes. +1 Strength.")
        elif hero.species == "Fae":
            hero.health_points = min(20, hp + 2)
            print("The Vagabond dances in shadows. +2 HP.")

    elif hero.sign == "The Juggernaut":
        if hero.species == "Dwarf":
            hero.health_points = min(20, hp + 4)
            print("The Juggernaut blesses your sturdy frame. +4 HP.")
        else:
            hero.health_points = min(20, hp + 2)
            hero.combat_strength = max(1, str_ - 1)
            print("The Juggernaut empowers your defense but slows your swing. +2 HP, -1 STR.")

    elif hero.sign == "The Serpent":
        if str_ <= 3:
            hero.combat_strength = min(6, str_ + 2)
            print("The Serpent coils and strikes. +2 STR for the weak.")
        else:
            hero.health_points = max(1, hp - 1)
            print("Poison courses through your veins. -1 HP.")
