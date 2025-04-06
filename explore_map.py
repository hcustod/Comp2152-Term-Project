# explore_map.py

import random

# Define locations that the player can explore
locations = ['Town', 'Forest', 'Cave']

def start_explore_map():
    """Function to start exploring the map and choose a location."""
    print("\n=== Map Exploration ===")
    print("Choose a location to explore:")

    # List the available locations
    for index, location in enumerate(locations, 1):
        print(f"{index}. {location}")
    
    # Get valid input from the player
    choice = int(input("Enter the number of your chosen location: "))
    
    # Check if the choice is valid
    if 1 <= choice <= len(locations):
        chosen_location = locations[choice - 1]
        print(f"\nYou have chosen to explore the {chosen_location}.")
        # Trigger events based on the location chosen
        handle_location_event(chosen_location)
    else:
        print("Invalid choice. Please choose a valid location.")

def handle_location_event(location):
    """Handle events that occur based on the location."""
    if location == 'Town':
        print("You find a bustling town with shops and people selling goods.")
    elif location == 'Forest':
        print("You enter a dark forest filled with mysterious sounds.")
    elif location == 'Cave':
        print("You venture into a cave and discover hidden treasures!")
