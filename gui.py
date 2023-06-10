from tkinter import *

#=========================Set up window===============================
# sets up default window
root = Tk()

#========================Function declarations========================
# function for greeting the user
def greet_user():
    global greeting

    greeting = Label(root, text = "Welcome to Track Your Moves!\n\nClick the button below to get started")
    greeting.pack(side = TOP, padx = 100, pady = 20)

# function to display start button
def start_button_setup():
    global start_button

    start_button = Button(root, text = "Click to start", command = get_user_name)
    start_button.pack(side = TOP, padx = 100, pady = 20)

# function to display submit button
def display_submit_button():
    global submit_button

    submit_button = Button(root, text = "Submit", command = handle_conversation)
    submit_button.pack(side = TOP, padx = 100, pady = 20)

# function to prompt user for their name
def get_user_name():
    global greeting
    global user_name
    global user_name_prompt
    global start_button

    # removes greeting from display
    greeting.pack_forget()
    # removes start button from display
    start_button.pack_forget()

    user_name_prompt = Label(root, text = "Before we get started logging your exercises, can you please tell me your name?")
    user_name_prompt.pack(side = TOP, padx = 100, pady = 20)
    # uses user_input_field() function to gain user name
    user_name = user_input_field()
    display_submit_button()

# function used for handling conversation and determining pathway
def handle_conversation():
    pass

# function that displays field for user to enter responses
def user_input_field():
    global entry
    
    entry = Entry(root)
    entry.pack(side = TOP, padx = 100, pady = 20)

#===========================Main program==============================
# calls the function to greet the user
greet_user()

# calls function to display start button
start_button_setup()

#==========================Starting the program=======================
# runs the GUI program
root.mainloop()