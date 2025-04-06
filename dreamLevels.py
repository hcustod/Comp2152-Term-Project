def run_dream_levels(party, monster):
    while True:
        try:
            print("    |", end="    ")
            num_dream_lvls = input("How many dream levels do you want to go down? (Enter a number 0-3): ")
            if num_dream_lvls.strip() == "":
                raise ValueError("Empty input")

            num_dream_lvls = int(num_dream_lvls)

            if not (0 <= num_dream_lvls <= 3):
                raise ValueError("Out of range")

            break

        except ValueError:
            print("Number entered must be a whole number between 0-3 inclusive, try again")

    if num_dream_lvls > 0:
        for hero in party:
            hero.health_points = max(0, hero.health_points - num_dream_lvls)
        monster.health_points += num_dream_lvls
        print(f"\nYou descend {num_dream_lvls} dream level(s). All heroes lose {num_dream_lvls} HP. Monster gains {num_dream_lvls} HP.")

    return num_dream_lvls
