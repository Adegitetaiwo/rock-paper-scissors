



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
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif player == "p":
        if cpu_values == "r":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif player == "s":
        if cpu_values == "p":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")
