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
#Question 1 - Level 1
while answer_level_1 == "y":
    print("let's start the game! To select the right answer, you need to type the same name as it is written on the options.")
    question = input(f"In which continente Brazil is located? \n a) South America \t b) Central America \n c) Africa \t d) Europe \n The answer is:")
    if question == "South America":
        print("\nRight Answer\n")
        score += 1
    else:
        print("Wrong Answer")
        break
#Question 2 - Level 1  
    if score == 1:
        question = input(f"What is the most spoken langague in Brazil? \n a) Brazilian \t b) Spanish \n c) Portuguese \t d) English \n The answer is:")
        if question == "Portuguese":
            print("\nRight Answer\n")
        score += 1
    else:
        print("Wrong Answer! You will need to start all over again :/")
        break
#Question 3 - Level 1  
    if score == 2:
        question = input(f"Which is the most famous event in Brazil? \n a) World Cup \t b) Carnaval \n c) Christmas \t d) Easter \n The answer is:")
        if question == "Carnaval":
            print("\nRight Answer\n")
        score += 1
    else:
        print("Wrong Answer! You will need to start all over again :/")
        break
#Question 4 - Level 1  
    if score == 3:
        question = input(f"In which month the carnavla is celebrated? \n a) February \t b) January \n c) December \t d) March \n The answer is:")
        if question == "February":
            print("\nRight Answer\n")
        score += 1
    else:
        print("Wrong Answer! You will need to start all over again :/")
        break        
#TODO: Create a structure that do the second level, while there is still questions to answer.
#Question 1 - Level 2
while answer_level_2 == "y":
    print("let's start the game! To select the right answer, you need to type the same name as it is written on the options.")
    question = input(f"who wrote the song garota de ipanema? \n a) Caetano Veloso \t b) Chico Buarque \n c) Jorge Ben Jor \t d) Antonio Jobim \n The answer is:")
    if question == "Antonio Jobim":
        print("\nRight Answer\n")
        score += 1
    else:
        print("Wrong Answer")
        break
#Question 2 - Level 2   
    if score == 1:
        question = input(f"Which is the capital of Brazil? \n a) Sao Paulo \t b) Brasilia \n c) Rio de Janeiro \t d) Salvador \n The answer is:")
        if question == "Brasilia":
            print("\nRight Answer\n")
        score += 1
    else:
        print("Wrong Answer! You will need to start all over again :/")
        break
#Question 3 - Level 2   
    if score == 2:
        question = input(f"In which month is Brazil's independece day? \n a) September \t b) July \n c) January \t d) October \n The answer is:")
        if question == "September":
            print("\nRight Answer\n")
        score += 1
    else:
        print("Wrong Answer! You will need to start all over again :/")
        break
#Question 4 - Level 2   
    if score == 3:
        question = input(f"Where the (Farol da Barra) is located? \n a) Buzios \t b) Recife \n c) Rio de Janeiro \t d) Salvador \n The answer is:")
        if question == "Salvador":
            print("\nRight Answer\n")
        score += 1
    else:
        print("Wrong Answer! You will need to start all over again :/")
        break        

#TODO: Create a structure that do the third level, while there is still questions to answer.
#Question 1 - Level 3
while answer_level_3 == "y":
    print("let's start the game! To select the right answer, you need to type the same name as it is written on the options.")
    question = input(f"Who was the most important quilombola warrior? \n a) Zumbi \t b)Palmares \n c) Urubu \t d) Zizeu \n The answer is:")
    if question == "Zumbi":
        print("\nRight Answer\n")
        score += 1
    else:
        print("Wrong Answer")
        break
#Question 2 - Level 3    
    if score == 1:
        question = input(f"Who wrote the Brazil's national anthem? \n a) Dom Pedro II \t b) Carlos Gomes \n c) Francisco Manuel da Silva \t d) Osorio Duque-Estrada \n The answer is:")
        if question == "Francisco Manuel da Silve":
            print("\nRight Answer\n")
        score += 1
    else:
        print("Wrong Answer! You will need to start all over again :/")
        break
#Question 3 - Level 3    
    if score == 2:
        question = input(f"Who was the second president of Brazil? \n a) Campos Sales \t b) Deodoro da Fonseca \n c) Juscelino Kubitschek \t d) Floriano Peixoto \n The answer is:")
        if question == "Floriano Peixoto":
            print("\nRight Answer\n")
        score += 1
    else:
        print("Wrong Answer! You will need to start all over again :/")
        break
#Question 4 - Level 3    
    if score == 3:
        question = int(input(f"What is the size of Brazil in Km2? \n a) 328600 \t b) 3286000 \n c) 3284000 \t d) 328400 \n The answer is:"))
        if question == "3286000":
            print("\nRight Answer\n")
        score += 1
    else:
        print("Wrong Answer! You will need to start all over again :/")
        break


#TODO: Print the results, and ask if he wants to play another game


#TODO: If he decide not to play, print a message with the score again, and tell about the user performace
