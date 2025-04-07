import random
from hero import Hero
from monster import Monster
from functions import fight_sequence, save_game, load_game
import os
import platform

def main():
    print("OS:", os.name)
    print("Python Version:", platform.python_version())

    monsters_killed = load_game()

    print("\nWelcome to Hero vs Monster!")
    print(f"Total monsters killed so far: {monsters_killed}\n")

    hero = Hero()
    monster = Monster()

    while True:
        result = fight_sequence(hero, monster)

        if result == "Hero Wins":
            monsters_killed += 1
            print("Hero victory!")
        elif result == "Monster Wins":
            print("Monster wins.")

        play_again = input("\nDo you want to fight again? (y/n): ").strip().lower()
        if play_again != 'y':
            save_game(monsters_killed)
            print("Game saved. Goodbye!")
            break

        hero.health_points = random.randint(20, 30)
        monster.health_points = random.randint(20, 30)

if __name__ == "__main__":
    main()
