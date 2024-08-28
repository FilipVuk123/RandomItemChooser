#!/usr/bin/python3


import secrets
import sys

def choose_random_item(items):
    """
    Chooses a random item from the provided list of items.

    Parameters:
    items (list): A list of items to choose from.

    Returns:
    any: A randomly chosen item from the list.
    """
    if not items:
        return "The list is empty. Please provide a list with at least one item."

    chosen_item = secrets.choice(items)
    return chosen_item

if __name__ == "__main__":
    # Check if any items are provided as arguments
    if len(sys.argv) < 2:
        print("Please provide a list of items as program arguments.")
        sys.exit(1)
    
    # Extract the list of items from the command-line arguments
    item_list = sys.argv[1:]

    # Choose a random item from the list
    selected_item = choose_random_item(item_list)
    
    print(f"The randomly selected item is: {selected_item}")
