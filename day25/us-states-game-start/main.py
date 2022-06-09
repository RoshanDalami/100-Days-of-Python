from multiprocessing.connection import answer_challenge
import turtle
import pandas 
screen = turtle.Screen()
screen.title("US State Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data["state"].to_list()


guessed_answer = []

while(len(guessed_answer)<50):
    answer_state = screen.textinput(title=f"{len(guessed_answer)}/50 State Correct",prompt="What's another state name?").title()
   
    if answer_state == "Exit":
        missing_state =[state for state in all_states if state not in guessed_answer]
        # for state in all_states:
        #     if state not in guessed_answer:
        #         missing_state.append(state)

        
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("states_to_learn.csv")
        break
    
    

    if answer_state in all_states:
        guessed_answer.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x),int(state_data.y))
        t.write(answer_state)

# print(answer_state)




