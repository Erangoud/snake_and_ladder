#use case 3:- The Player then checks for a Option. They are No Play, Ladder or Snake.

import random

def get_option():
    return random.randint(1, 3)  # 1: No Play, 2: Ladder, 3: Snake

def play_turn(player_name, position, rolls_count):
    dice_roll = random.randint(1, 6)
    rolls_count += 1
    print(f"{player_name} rolled a {dice_roll}")

    option = get_option()

    if option == 1:  # No Play
        print(f"{player_name} stays in the same position.")
        position = position

    elif option == 2:  # Ladder
        if position + dice_roll > 100:
            print(f"{player_name} cannot move, would exceed 100.")
            position = position  # Stay in the same position
        else:
            position += dice_roll
            print(f"{player_name} moved forward by {dice_roll}.")

    elif option == 3:  # Snake
        if position - dice_roll < 0:
            position = 0  # Reset to 0
            print(f"{player_name} went back and reset to 0.")
        else:
            position -= dice_roll
            print(f"{player_name} moved backward by {dice_roll}.")

    

