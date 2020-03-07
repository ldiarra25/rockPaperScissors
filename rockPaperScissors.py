
import random

keepPlaying = True

while(keepPlaying == True):
    print("Welcome")
    print("First to two wins. Press q if you want to quit. Type in lower case letters only")
    #rock is 1, paper is 2, scissors is 3
   
    scoreComp = 0
    scorePlayer = 0
   
    while(scorePlayer < 2) and (scoreComp < 2):
        choiceComp = random.randint(1,3)
        choicePlayer = input("pick either rock, paper, or scissors!")
       
        if(choicePlayer == "q"):
            keepPlaying = False
            break
        elif((choicePlayer == "rock" ) and (choiceComp == 1)) or ((choicePlayer == "paper" ) and (choiceComp == 2)) or ((choicePlayer == "scissors" ) and (choiceComp == 3)):
            print("You draw")
            print("Computer's Score: ", + scoreComp)
            print("Your Score: ", + scorePlayer)
           
        elif((choicePlayer == "rock" ) and (choiceComp == 2)) or ((choicePlayer == "paper" ) and (choiceComp == 3)) or ((choicePlayer == "scissors" ) and (choiceComp == 1)):
            print("You took an L 9_9")
            scoreComp = scoreComp + 1
            print("Computer's Score: ", + scoreComp)
            print("Your Score: ", + scorePlayer)
        elif((choicePlayer == "rock" ) and (choiceComp == 3)) or ((choicePlayer == "paper" ) and (choiceComp == 1)) or ((choicePlayer == "scissors" ) and (choiceComp == 2)):
            print("you win this round")
            scorePlayer = scorePlayer + 1
            print("Computer's Score: ", + scoreComp)
            print("Your Score: ", + scorePlayer)
        else :
            print("remember to type in lower case letters")
           
    if (scorePlayer == 2):
            print("You win!!!!!")
         
           
    if (scoreComp == 2):
            print("You lose...")
           
    print("Computer's Score: ", + scoreComp , "Your Score: ", + scorePlayer)