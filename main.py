import random

def play_turn(player_name, position, rolls_count):
    dice_roll = random.randint(1, 6)
    rolls_count += 1


    option = random.randint(1, 3)  # Random option to select the movement
    
    if option == 1:
        position = position

    elif option == 2:
        if position + dice_roll > 100: 
            position = position
        else:
            position += dice_roll

    elif option == 3:
        if position - dice_roll <0:
            position=position
        else:
            position -= dice_roll

    # checking the player is win or not !
    if position == 100:
        print(f"{player_name} reached position 100 and WON the game in {rolls_count} rolls!")
        return position, rolls_count, True  # Player wins
        
    
    return position, rolls_count, False  # No winner yet

p1_position = 0
p2_position = 0
p1_rolls_count = 0
p2_rolls_count = 0
win_flag = False

while  not win_flag:
    p1_position, p1_rolls_count, win_flag = play_turn("eran", p1_position, p1_rolls_count)
    if win_flag:
        break
    p2_position, p2_rolls_count, win_flag = play_turn("sunil", p2_position, p2_rolls_count)
    if win_flag:
        break
    
    print(f"eran Roll_no {p1_rolls_count}: Dice = {random.randint(1, 6)}, Position = {p1_position}")
    print(f"sunil Roll_no {p2_rolls_count}: Dice = {random.randint(1, 6)}, Position = {p2_position}")

