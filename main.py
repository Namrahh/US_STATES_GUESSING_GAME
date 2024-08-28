import turtle
import pandas

screen = turtle.Screen()
screen.setup(500, 500)
screen.title("States Guessing Game")
screen.tracer(0)
image = "blank_states_img.gif"
screen.addshape(image)

# Create a turtle object for displaying the image
image_turtle = turtle.Turtle()
image_turtle.shape(image)

# Create a separate turtle object for writing state names
writer_turtle = turtle.Turtle()
writer_turtle.hideturtle()
writer_turtle.penup()

states = pandas.read_csv("50_states.csv")
states_list = states.state.to_list()
state_x_coords = states.x.to_list()
state_y_coords = states.y.to_list()

guessed_states = []

game_over = False
while not game_over:
    screen.update()
    if len(guessed_states) < 50:
        guess_input = screen.textinput("Guess the State", "Enter a state name (or 'exit' to quit): ").strip().capitalize()
    if guess_input.lower() == 'exit':
        break

    if guess_input in states_list and guess_input not in guessed_states:
        coords = states[states.state == guess_input]
        writer_turtle.goto(int(coords.iloc[0].x) - 10, int(coords.iloc[0].y))
        writer_turtle.write(
            arg=f"{guess_input.capitalize()}", font=("Courier", 8, "normal")
        )
        guessed_states.append(guess_input)

    if len(guessed_states) == len(states_list):
        writer_turtle.write("You have guessed all 50 states!")
        game_over = True

    missing_states = [state for state in states_list if state not in guessed_states]
    pandas.DataFrame(missing_states).to_csv("States_to_learn.csv")
screen.mainloop()