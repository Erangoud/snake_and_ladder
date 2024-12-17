#use case 6:-Report the number of times the dice was played to win the game and also the position after every die role
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

    if position == 100: # use case 5
        print(f"{player_name} reached position 100 and WON the game in {rolls_count} rolls!")
        return position, rolls_count, True  # Player wins
    
    return position, rolls_count, False  # the number  of counts returning


def start_game():
    player_position = 0
    rolls_count = 0
    win_flag = False

    while not win_flag:
        player_position, rolls_count, win_flag = play_turn("Player", player_position, rolls_count) # the number  of counts returning
        print(f"Player Roll #{rolls_count}: Position = {player_position}")

start_game()