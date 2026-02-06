# ===========================================================================
#                                    ROCK PAPER SCISSOR GAME
# # ==========================================================================
import random
options = [ "Rock" , "Paper" , "Scissors"]
computer_score = 0
player_score = 0 
tie_count = 0

while  True:
    player = input ("Enter Rock , Paper , Scissors | (Write End to end the Game) : ").capitalize()
    if player == "End":
            print(f"\nFinal Scores:\nComputer Score: {computer_score}\nPlayer Score: {player_score}")
            if player_score > computer_score:
                print(f"Congratulation! You Won by Score {player_score - computer_score}")
            elif player_score < computer_score:
                print(f"Computer Won by Score {computer_score - player_score}")
            else:
                print(F"Game Tie..")
            with open("game_scores.txt" , "a") as file :
                file.write(f"\n--- GAME ENDED ---\nFinal Score You: {player_score}, Computer: {computer_score}, Ties: {tie_count}\n\n")
                print("Result are also save to file game_scores.txt.\n")
            break
            
    elif player not in options:
        print("Invalid input. Please enter Rock, Paper, or Scissors.")
        continue

    computer = random.choice(options)

    if player == computer:
        tie_count += 1
        print("It's a Tie.")
        print(f"Tie Count is {tie_count}\n")
        with open("game_scores.txt", "a") as file:
            file.write(f"\nPlayer: {player}, Computer: {computer}, Result: TIE, Score = You: {player_score}, Computer: {computer_score}, Ties: {tie_count}\n")

        continue   # continue to the next round, with new random computer move
    elif player == "Rock":
        if computer == "Paper" :
            computer_score += 1
            print(f"YOU LOSE. {computer} covers {player}.")
            print(f"Player Score is : {player_score} and Computer Score is : {computer_score}\n")
            with open("game_scores.txt", "a") as file:
                file.write(f"\nPlayer: {player}, Computer: {computer}, Result: Computer WIN, Score = You: {player_score}, Computer: {computer_score}, Ties: {tie_count}\n")
                
        else:
            player_score +=1
            print(f"YOU WIN. {player} smashes {computer}")
            print(f"Player Score is : {player_score} | Computer Score is : {computer_score}\n")
            with open("game_scores.txt", "a") as file:
                file.write(f"\nPlayer: {player}, Computer: {computer}, Result: YOU WIN, Score = You: {player_score}, Computer: {computer_score}, Ties: {tie_count}\n")

    

                
    elif player == "Paper":
        if computer == "Scissors":
            computer_score += 1
            print(f"YOU LOSE. {computer} cuts {player}.")
            print(f"Player Score is : {player_score} | Computer Score is : {computer_score}\n")
            with open("game_scores.txt", "a") as file:
                file.write(f"\nPlayer: {player}, Computer: {computer}, Result: Computer WIN, Score = You: {player_score}, Computer: {computer_score}, Ties: {tie_count}\n")
                
        else:
            player_score +=1
            print(f"YOU WIN. {player} covers {computer}")
            print(f"Player Score is : {player_score} | Computer Score is : {computer_score}\n")
            with open("game_scores.txt", "a") as file:
                file.write(f"\nPlayer: {player}, Computer: {computer}, Result: YOU WIN, Score = You: {player_score}, Computer: {computer_score}, Ties: {tie_count}\n")


                
    elif player == "Scissors":
        if computer == "Rock":
            computer_score += 1
            print(f"YOU LOSE. {computer} smashes {player}.")
            print(f"Player Score is : {player_score} and Computer Score is : {computer_score}\n")
            with open("game_scores.txt", "a") as file:
                file.write(f"\nPlayer: {player}, Computer: {computer}, Result: Computer WIN, Score = You: {player_score}, Computer: {computer_score}, Ties: {tie_count}\n")

                
        else:
            player_score +=1 
            print(f"YOU WIN. {player} cuts {computer}")
            print(f"Player Score is : {player_score} and Computer Score is : {computer_score}\nTie Count is : {tie_count}\n")      
            with open("game_scores.txt", "a") as file:
                file.write(f"\nPlayer: {player}, Computer: {computer}, Result: YOU WIN, Score = You: {player_score}, Computer: {computer_score}, Ties: {tie_count}\n")