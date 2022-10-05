import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
# add a shape to the screen
screen.addshape(image)
turtle.shape(image)
turtle.tracer(0)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

guessed_states = []
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50", prompt="What's the next state? ")
    title_cased_answer_state = answer_state.title()

    if title_cased_answer_state in all_states:
        all_states.remove(title_cased_answer_state)
        guessed_states.append(title_cased_answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        # fetch the data row when the data is equal to the user's guess
        state_data = data[data.state == title_cased_answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(title_cased_answer_state, font=("Arial", 6, "normal"))

    if title_cased_answer_state == "Exit":
        # missing_states = []
        # for state in all_states:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("States_to_learn")
        break
    missing_states = []

