import turtle
import pandas

#Creating a turtle screen object
screen = turtle.Screen()


#creating our Turtle object with circle shape
timmy = turtle.Turtle(shape = "circle")
timmy.shapesize(stretch_wid= 0.2, stretch_len= 0.2)        #Changing the shape size
timmy.penup()
timmy.hideturtle()


#Providing our screen a nice title
screen.title("Guess the States and UTs")                      

image = "india.gif"


#Adding image of map of India in our turtle screen
screen.addshape(image)
turtle.shape(image)


#Getting all the states and uts data as Dataframe from created csv file
state_csv = "India_states & UTs.csv"
state_df = pandas.read_csv(state_csv)

state_uts_list = state_df["Name"].to_list()         #Getting the state and uts name column as series and coverting it to a list


#Taking inputs from user in turtle screen
count = 0
while count < len(state_uts_list):

    user_input = screen.textinput(title = f"{count}/37 States and UTs correct", prompt = "Enter any State or Union territory name:\n(Type 'Exit' to close the game)").title()

    if user_input in state_uts_list:            #Checking if the entered string in really a state or UT
        

        state_name_row = state_df[state_df["Name"] == user_input]           #Creating a Dataframe with x and y coords for the enter string

        coord_x_list = state_name_row["X"].to_list()             #Extracting the x coords as a series and then converting it to list
        for i in coord_x_list:                                   #Converting the element 
            coord_x = i                                          #in list to an int

        coord_y_list = state_name_row["Y"].to_list()             #Similarly, extracting the y coords
        for i in coord_y_list:
            coord_y = i

        count += 1

    #Writing the correctly guessed state name onto the map
        timmy.setposition(coord_x, coord_y)
        timmy.color("red")
        timmy.write(user_input)


    #Creating a way to close the turtle screen with a specific keyword.
    if user_input == "Exit":
        break


screen.mainloop()         #This will allow the screen to stay put even only way to close is to close the whole screen
                          #use when exitonclick() is not enough