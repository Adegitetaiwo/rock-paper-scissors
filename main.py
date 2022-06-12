# This is a rock, paper, scissors game python script
import random

print("You're Welcome, This is a Rock, Paper, and Scissors Game. \n \
    Kindly pay attention to detail as you play. Happy Playing.")
while True:
    # ask player to start and save to a variable
    player = input("Enter any of your choice (R, P, S): ").lower()
    
    # possible player and computer outcome
    actions_values = ["R", "P", "S"]
    cpu_values = random.choice(actions_values).lower()

    actions_database = {
        actions_values[0].lower() : "Rock",
        actions_values[1].lower() : "Paper",
        actions_values[2].lower() : "Scissors"
    }
    if player.capitalize not in actions_values:
        print("You've entered an invalid item, you are \n \
            expected to only select either (R, P, or S), Try again. \n")
        continue

    # print palyer and cpu moves
    print(f"Player ({actions_database[player]}) : CPU ({actions_database[cpu_values]})")


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

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break