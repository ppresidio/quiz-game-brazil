"""
Name: quiz_game.py
 Author: Pedro Paulo Presidio
 Created: 1/22/24
 Purpose: A quiz game about Brazil
"""
#--------------CONSTANTS/variables------------------
DASHES = 50
question = 0
score = 0
#---------------GAME TITEL---------------
print("-" * DASHES)
print("The Brazilian quiz game :0")
print("-" * DASHES)
#------------------INPUT-----------------
#TODO:Print the difficult levels
print("For this game we will have 3 difficulties:")
print("Level 1 - Just easy questions")
print("Level 2 - General knowledge about Brazil")
print("Level 3 - This one is hard even for Brazilians")


#TODO:Recive the level of difficult that the user wants
difficult_level = int(input("Select which of the levels you want to play 1, 2 or 3: "))

#TODO:Create the variables to save the score and the amount of questions in each category.

question = 0 #To recieve the answers on the form of string 
score = 0 #To increase the running total of points

#TODO:Create the conditions to check which level the user choose
if difficult_level == 1:
    answer_level_1 = input("You choose the level 1, ready to play?\n(y/n)")

elif difficult_level == 2:
    answer_level_2 = input("You choose the level 2, ready to play?\n(y/n)")

elif difficult_level == 2:
    answer_level_3 = input("You choose the level 2, ready to play?\n(y/n)")

else:
    print("please enter your choice as said on the text")
    
#TODO: Create a structure that do the first level, while there is still questions to answer.
#Question 1
while answer_level_1 == "y":
    print("let's start the game! To select the right answer, you need to type the same name as it is written on the options.")
    question = input(f"In which continente Brazil is located? \n a) South America \t b) Central America \n c) Africa \t d) Europe \n The answer is:")
    if question == "South America":
        print("\nRight Answer\n")
        score += 1
    else:
        print("Wrong Answer")
        break
#Question 2    
    if score == 1:
        question = input(f"What is the most spoken langague in Brazil? \n a) Brazilian \t b) Spanish \n c) Portuguese \t d) English \n The answer is:")
        if question == "Portuguese":
            print("\nRight Answer\n")
        score += 1
    else:
        print("Wrong Answer! You will need to start all over again :/")
        break
#TODO: Create a structure that do the second level, while there is still questions to answer.


#TODO: Create a structure that do the third level, while there is still questions to answer.


#TODO: Print the results, and ask if he wants to play another game


#TODO: If he decide not to play, print a message with the score again, and tell about the user performace

