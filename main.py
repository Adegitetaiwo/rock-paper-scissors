
# This is a rock, paper, scissors game python script
# import in-built modules
import random

# import custom modules
import functions


# welcome greeting
print("You're Welcome, This is a Rock, Paper, and Scissors Game. \n \
       Kindly pay attention to detail as you play. Happy Playing.")


# continue in loop until user would no longer wants to play
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
    
    # validate Player Entry
    if player.capitalize() not in actions_values:
        print("You've entered an invalid item, you are \n \
            expected to only select either (R, P, or S), Try again. \n")
        continue

    # print palyer and cpu moves
    print(f"Player ({actions_database[player]}) : CPU ({actions_database[cpu_values]})")

    # this function was from a module "funtions"
    # check and return winning status (Won, Lose or Tie)
    functions.check_winner(player, cpu_values)

    # Ask User if they would play again in other 
    # to break for continue in the loop.
    # the capital N means defualt value

    play_again = input("Would you love to Play again? (y/N): ")
    if play_again.lower() == "y" or play_again.lower() == "yes":
        continue
    else:
        print("Game Over!")
        break