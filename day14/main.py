import logo 
import game_data 
from random import randint

#TODO: retrive the data from the game_data.py and compare 
# Ask the user choose which one have more followers.
# if User guess it correctly than go for next guess and increase score by 1 for every correct guess.
# if User guess incorrect terminate the program and show the final score.
 
print(logo.logo)
randomNumber1=randint(0,len(game_data.data))
randomNumber2=randint(0,len(game_data.data))

score = 0

dict1 = game_data.data[randomNumber1]
dict2 = game_data.data[randomNumber2]
#Retriving value for First
name1 = dict1["name"]
follower_count1 = dict1["follower_count"]
description1 = dict1["description"]
country1 = dict1["country"]
name2 = dict2["name"]
#Retriving value for second
follower_count2 = dict2["follower_count"]
description2 = dict2["description"]
country2 = dict2["country"]
def compare():
    print(f"Compare A: {name1},a {description1},from {country1}")
    print(logo.vs)

    print(f"Against B : {name2} , a {description2} , from {country2}")


