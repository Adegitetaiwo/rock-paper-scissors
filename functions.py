



# 
def check_winner(player:str, cpu_values:str):
    """
    This module will check for a winner among the two players User (You) and Computer (CPU)
    and would return the outcome.
    Parameters
    -----------
    player: string
    cpu_values: string

    """
    if player == cpu_values:
        print(f"Both players selected {player.capitalize()}. It's a tie!")
    elif player == "r":
        if cpu_values == "s":
            print("Rock beats Scissors! You Win!")
        else:
            print("Paper beats Rock! You Lose.")
    elif player == "p":
        if cpu_values == "r":
            print("Paper beats Rock! You Win!")
        else:
            print("Scissors cuts paper! You Lose.")
    elif player == "s":
        if cpu_values == "p":
            print("Scissors beats Paper! You Win!")
        else:
            print("Rock beats Scissors! You Lose.")
