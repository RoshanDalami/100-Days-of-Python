from ast import Global
from pickle import TRUE
import logo 
import game_data 
import random

#TODO: retrive the data from the game_data.py and compare 
# Ask the user choose which one have more followers.
# if User guess it correctly than go for next guess and increase score by 1 for every correct guess.
# if User guess incorrect terminate the program and show the final score.
 
print(logo.logo)

score = 0
guess = True



def guess():
    randomNumber1=random.randint(0,len(game_data.data))
    randomNumber2=random.randint(0,len(game_data.data))

    dict1 = game_data.data[randomNumber1]
    dict2 = game_data.data[randomNumber2]
    #Retriving value for First
    name1 = dict1["name"]
    follower_count1 = dict1["follower_count"]
    description1 = dict1["description"]
    country1 = dict1["country"]

    #Retriving value for second
    name2 = dict2["name"]
    follower_count2 = dict2["follower_count"]
    description2 = dict2["description"]
    country2 = dict2["country"]

    global guess
    global score
    print(f"Compare A: {name1} a {description1} from {country1}")
    print(follower_count1)
    print(logo.vs)
    print(f"Against B: {name2} a {description2} from {country2}")
    print(follower_count2)
    
    
    choice = input("Who has a more follower ? Type A or B:  ").upper()
    if(choice == "A" and (follower_count1 > follower_count2)):
        score = score +1
    if(choice == "A" and (follower_count1 < follower_count2)):
        guess = False
        print(f"Your Score is {score}")

    if(choice == "B" and (follower_count1 < follower_count2)):
        score = score +1
    if(choice == "B" and (follower_count1 > follower_count2)):
        guess = False
        print(f"Your Score is {score}")
    
while(guess != False):
    guess()

