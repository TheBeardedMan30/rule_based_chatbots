import time
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from colorama import Fore
# imports tkinter library
from tkinter import *



#=============================== Defines new class ====================================
# sets up class that inherits tkinter library
class Exercise_Log(Tk):

    #~~~~~~~~~~~~~~~~~~~~~~ Sets up various lists for use in class ~~~~~~~~~~~~~~~~~~~~
    stop_words = set(stopwords.words("english"))

    negative_responses = ['no', 'nah', 'not yet', 'no thanks']
    exit_commands = ['quit', 'stop', 'exit']
    exercise_type_list = ['indoor run', 'outdoor run', 'indoor cycle', 'outdoor cycle', 'swimming laps', 'open ocean swim']
    exercise_log = []


    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Initialize function ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def __init__(self):
        super().__init__()

        self.initialize_gui()


    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ GUI initialize function ~~~~~~~~~~~~~~~~~~~~~~~~~~
    def initialize_gui(self):
        self.greet()


    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Greet function ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def greet(self):
        self.greeting = Label(self, text = "Welcome to Track Your Moves!\n\nClick the button below to get started")
        self.greeting.pack(side = TOP, padx = 100, pady = 20)
        self.start_button_setup()


    #~~~~~~~~~~~~~~~~~~~~~~~~~~~ Display start button ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def start_button_setup(self):
        self.start_button = Button(self, text = "Click to start", command = self.get_user_name)
        self.start_button.pack(side = TOP, padx = 100, pady = 20)


    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Prompt for user's name ~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def get_user_name(self):
        # removes greeting from display
        self.greeting.pack_forget()
        # removes start button from display
        self.start_button.pack_forget()

        self.user_name_prompt = Label(self, text = "Before we get started logging your exercises, can you please tell me your name?")
        self.user_name_prompt.pack(side = TOP, padx = 100, pady = 20)
        # uses user_input_field() function to start gaining user name
        self.user_name = self.user_input_field()

        # new variable used to determine conversation path
        self.pathway = 1

        self.display_submit_button()


    #~~~~~~~~~~~~~~~~~~~~~~~ Determine if conversation will proceed ~~~~~~~~~~~~~~~~~~
    def confirm_log_proceed(self):
        # displays new user input field to enter response to question above
        self.pathway = 2
        self.start_new_log = self.user_input_field()


    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Display user input field ~~~~~~~~~~~~~~~~~~~~~~~~~
    def user_input_field(self):
        # uses keyword 'Entry()' to create user input field
        self.entry = Entry(self)
        self.entry.pack(side = TOP, padx = 100, pady = 20)


    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Display submit button ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def display_submit_button(self):
        self.submit_button = Button(self, text = "Submit", command = self.handle_conversation)
        self.submit_button.pack(side = TOP, padx = 100, pady = 20)


    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Handle conversation ~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def handle_conversation(self):
        # remove the following items from screen
        self.user_name_prompt.pack_forget()
        self.submit_button.pack_forget()
        self.entry.pack_forget()

        # conditional checks to determine conversation pathways
        # pathway 1 gets username and greets user
        if self.pathway == 1:
            # uses .get() to actually retrieve response from self.entry
            self.user_name = self.entry.get()
            self.display_user_name = Label(self, text = f"Hi, {self.user_name}, would you like to log a new exercise?")
            self.display_user_name.pack(side = TOP, padx = 100, pady = 20)
            self.confirm_log_proceed()
            self.display_submit_button()
        
        # pathway 2 checks if the user wants to log an exercise
        elif self.pathway == 2:
            self.display_user_name.pack_forget()
            self.proceed = self.entry.get()
            # tokenizes user response
            self.proceed_tokenized = word_tokenize(self.proceed)
            self.check_words = 0
            
            # checks if tokens are in negative response list
            for word in self.proceed_tokenized:
                if word in self.negative_responses:
                    self.check_words += 1
                else:
                    pass
            # if any tokens matched negative response list this will run
            
            if self.check_words > 0:
                self.not_proceed = Label(self, text = "Ok then, no worries!")
                self.not_proceed.pack(side = TOP, padx = 100, pady = 20)
                self.check_words = False
            
            # this will run if no negative response matches found
            else:
                self.display_options = Label(self, text = "Great. Let's get started!\n\nWhat type of exercise would you like to log? I have the following options available for you:\n\nRun\n\nCycle\n\nSwim")
                self.display_options.pack(side = TOP, padx = 100, pady = 20)
                self.pathway = 3
                # displays input field for entering type of exercise
                self.enter_exercise_type = self.exercise_type_prompt()
                # display button to submit exercise type
                self.display_submit_button()
        # pathway 3 determines exercise type
        elif self.pathway == 3:
            # determine exercise type and activate necessary pathway
            self.determine_exercise_type()
        # pathway is taken if user confirms they want to log an indoor run
        elif self.pathway ==  4:
            # removes previous text from GUI
            self.confirm_option.pack_forget()
            # retrieves input from user
            self.check_confirmation = self.entry.get()
            # checks if user input matches "yes"; if it does, following code will run
            if self.check_confirmation.lower() == "yes":
                self.indoor_run_check = True
                self.outdoor_run_check = False
                self.handle_indoor_run_conversation()
            elif self.check_confirmation.lower() == "no":
                self.indoor_run_check = False
                self.outdoor_run_check = True
                self.handle_outdoor_run_conversation()
        elif self.pathway == 5:
            self.exercise_date_completed.pack_forget()
            self.get_date = self.entry.get()
            if self.indoor_run_check == True:
                if self.indoor_run_pathway == 1:
                    self.indoor_run_pathway = 2
                    self.indoor_run()
            elif self.outdoor_run_check == True:
                if self.outdoor_run_pathway == 1:
                    self.outdoor_run_pathway = 2
                    self.outdoor_run()
        elif self.pathway == 6:
            self.exercise_time_completed.pack_forget()
            self.get_time = self.entry.get()
            if self.indoor_run_check == True:
                if self.indoor_run_pathway == 2:
                    self.indoor_run_pathway = 3
                    self.indoor_run()
            elif self.outdoor_run_check == True:
                if self.outdoor_run_pathway == 2:
                    self.outdoor_run_pathway = 3
                    self.outdoor_run()
        elif self.pathway == 7:
            self.exercise_duration_completed.pack_forget()
            self.get_duration = self.entry.get()
            self.indoor_run_pathway = 4
            self.indoor_run()
        elif self.pathway == 8:
            self.exercise_distance_completed.pack_forget()
            self.get_distance = self.entry.get()
            self.indoor_run_pathway = 5
            self.indoor_run()
        elif self.pathway == 9:
            self.indoor_run_complete_entry.pack_forget()
            self.confirm_log = self.entry.get()
            if self.confirm_log.lower() == "yes":
                self.update_exercise_log()
                self.entry_added = Label(self, text = f"The entry has been added to your exercise log.\n\n{self.exercise_log[-1]}")
                self.entry_added.pack(side = TOP, padx = 100, pady = 20)
        elif self.pathway == 10:
            # removes previous text from GUI
            self.confirm_option.pack_forget()
            # retrieves input from user
            self.check_confirmation = self.entry.get()
            # checks if user input matches "yes"; if it does, following code will run
            if self.check_confirmation.lower() == "yes":
                self.confirmed_run = Label(self, text = "Sure, I can log an indoor cycle for you.")
                self.confirmed_run.pack(side = TOP, padx = 100, pady = 20)
                # sets exercise_type to "indoor run" to enable reusable string
                self.exercise_type = "indoor cycle"
                self.indoor_cycle_pathway = 1
                self.indoor_cycle()

    
    # ****** work on getting these functions to handle each exercise type log conversation
    def handle_indoor_run_conversation(self):
        self.confirmed_run = Label(self, text = "Sure, I can log an indoor run for you.")
        self.confirmed_run.pack(side = TOP, padx = 100, pady = 20)
        # sets exercise_type to "indoor run" to enable reusable string
        self.exercise_type = "indoor run"
        self.indoor_run_pathway = 1
        self.indoor_run()

    def handle_outdoor_run_conversation(self):
        self.confirmed_run = Label(self, text = "Alright, lets log an outdoor run.")
        self.confirmed_run.pack(side = TOP, padx = 100, pady = 20)
        self.exercise_type = "outdoor run"
        self.outdoor_run_pathway = 1
        self.outdoor_run()


    #~~~~~~~~~~~~~~~~~~~~~~~~~~ Entry field for exercise type ~~~~~~~~~~~~~~~~~~~~~~~
    def exercise_type_prompt(self):
        self.user_input_field()


    #~~~~~~~~~~~~~~~~~~~~~~ Analyse input to determine exercise type ~~~~~~~~~~~~~~~~
    def determine_exercise_type(self):
        # assigns user input to variable
        self.exercise_type = self.entry.get()
        # tokenizes user input
        self.exercise_type_tokenized = word_tokenize(self.exercise_type)
        # creates empty list
        self.user_response_list = []
        # calls function that assigns words from tokens that are not stop words
        self.user_response_match = self.user_response()

        # starts check of each word in self.user_response_match
        for word in self.user_response_match:
            # runs this code if the word 'run' is found within analysed user response
            if word == "run":
                # remove exercise options text
                self.display_options.pack_forget()
                self.confirm_option = Label(self, text = "I found a possible match.\n\nDo you want to log an indoor run?")
                self.confirm_option.pack(side = TOP, padx = 100, pady = 20)
                # displays text field to enter confirmation of exercise type
                self.enter_confirmation = self.user_input_field()
                self.pathway = 4
                # displays button to submit confirmation
                self.display_submit_button()
            elif word == "cycle":
                self.display_options.pack_forget()
                self.confirm_option = Label(self, text = "I found a possible match.\n\nDo you want to log an indoor cycle?")
                self.confirm_option.pack(side = TOP, padx = 100, pady = 20)
                self.enter_confirmation = self.user_input_field()
                self.pathway = 4
                self.display_submit_button()


    #~~~~~~~~~~~~~~~~~~~~~~~~~ Strip stop words from user response ~~~~~~~~~~~~~~~~~~
    def user_response(self):
            for word in self.exercise_type_tokenized:
                if word not in self.stop_words:
                    self.user_response_list.append(word)
            return self.user_response_list

    """"  
                elif self.confirm_option.lower() == "no":
                    self.confirm_option = input(Fore.GREEN + f"\nOk, did you want to log an outdoor cycle? " + Fore.WHITE)
                    if self.confirm_option.lower() == "yes":
                        print(Fore.GREEN + "\nSure, I can log an outdoor cycle for you." + Fore.WHITE)
                        self.exercise_type = "outdoor cycle"
                        self.outdoor_cycle()
                    else:
                        print(Fore.GREEN + "\nSorry, something has gone wrong.")
            elif word == "laps":
                self.confirm_option = input(Fore.GREEN + f"\nI found a possible match - do you want to log swimming laps? " + Fore.WHITE)
                if self.confirm_option.lower() == "yes":
                    print(Fore.GREEN + "\nSure, I can log swimming laps for you." + Fore.WHITE)
                    self.exercise_type = "swimming laps"
                    self.swimming_laps()
                else:
                    print(Fore.GREEN + "\nSorry, something has gone wrong.")
            elif word == "ocean":
                self.confirm_option = input(Fore.GREEN + f"\nI found a possible match - do you want to log an open ocean swim? " +Fore.WHITE)
                if self.confirm_option.lower() == "yes":
                    print(Fore.GREEN + "\nSure, I can log an open ocean swim for you." + Fore.WHITE)
                    self.exercise_type = "open ocean swim"
                    self.open_ocean_swimming()
                else:
                    print(Fore.GREEN + "\nSorry, something has gone wrong.") """
    

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Logging indoor run ~~~~~~~~~~~~~~~~~~~~~~~~~~
    def indoor_run(self):
        if self.indoor_run_pathway == 1:
            self.indoor_run_date = self.exercise_date()
        elif self.indoor_run_pathway == 2:
            self.indoor_run_time = self.exercise_time()
        elif self.indoor_run_pathway == 3:
            self.indoor_run_duration = self.exercise_duration()
        elif self.indoor_run_pathway == 4:
            self.indoor_run_distance = self.exercise_distance()
        elif self.indoor_run_pathway == 5:
            self.indoor_run_complete_entry = Label(self, text = f"The following information will be added to your exercise log:\n\nDate of {self.exercise_type}: {self.get_date}\nTime of {self.exercise_type}: {self.get_time}\nDuration of {self.exercise_type}: {self.get_duration}\nDistance of {self.exercise_type}: {self.get_distance}\n\nWould you like to add this entry to your log?")
            self.indoor_run_complete_entry.pack(side = TOP, padx = 100, pady = 20)
            self.confirm_entry = self.user_input_field()
            self.pathway = 9
            self.display_submit_button()

    
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Logging outdoor run ~~~~~~~~~~~~~~~~~~~~~~~~~
    def outdoor_run(self):
        if self.outdoor_run_pathway == 1:
            self.outdoor_run_date = self.exercise_date()
        elif self.outdoor_run_pathway == 2:
            self.outdoor_run_time = self.exercise_time()
        elif self.outdoor_run_pathway == 3:
            self.outdoor_run_duration = self.exercise_duration()
        """"
        self.outdoor_run_date_check = input(Fore.GREEN + f"\nOk, so you completed your {self.exercise_type} on {self.outdoor_run_date}. Is that correct? " + Fore.WHITE)
        if self.outdoor_run_date_check == "yes":
            print(Fore.GREEN + "\nGreat! Let's move on." + Fore.WHITE)
            self.outdoor_run_time = self.exercise_time()
            self.outdoor_run_time_check = input(Fore.GREEN + f"\nJust checking: you completed your {self.exercise_type} at {self.outdoor_run_time}. Have I got that right? " + Fore.WHITE)
            if self.outdoor_run_time_check == "yes":
                print(Fore.GREEN + "\nExcellent! Let's keep going." + Fore.WHITE)
                self.outdoor_run_duration = self.exercise_duration()
                self.outdoor_run_duration_check = input(Fore.GREEN + f"Confirming: you did an {self.exercise_type} for {self.outdoor_run_duration}? " + Fore.WHITE)
                if self.outdoor_run_duration_check == "yes":
                    print(Fore.GREEN + "\nGreat, next question!" + Fore.WHITE)
                    self.outdoor_run_distance = self.exercise_distance()
                    self.outdoor_run_distance_check = input(Fore.GREEN + f"\nOk, so you did an {self.exercise_type} for {self.outdoor_run_distance} - is that correct? " + Fore.WHITE)
                    if self.outdoor_run_distance_check == "yes":
                        print(Fore.GREEN + "\nAlrighty then!" + Fore.WHITE)
                        self.outdoor_run_complete_entry = input(Fore.GREEN + f"The following information will be added to your exercise log:\nDate of {self.exercise_type}: {self.outdoor_run_date}\nTime of {self.exercise_type}: {self.outdoor_run_time}\nDuration of {self.exercise_type}: {self.outdoor_run_duration}\nDistance of {self.exercise_type}: {self.outdoor_run_distance}\nAdd this entry to your log? " + Fore.WHITE)
                        if self.outdoor_run_complete_entry == "yes":
                            self.update_exercise_log()
                            print(self.exercise_log[-1])
    """
    

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Gain exercise date ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def exercise_date(self):
        # removes previous text
        self.confirmed_run.pack_forget()
        # prompt user for exercise date
        self.exercise_date_completed = Label(self, text = f"On what date did you complete your {self.exercise_type}? ")
        self.exercise_date_completed.pack(side = TOP, padx = 100, pady = 20)
        self.enter_date = self.user_input_field()
        self.pathway = 5
        self.display_submit_button()


    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Gain exercise time ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def exercise_time(self):
        self.exercise_time_completed = Label(self, text = f"At what time did you begin your {self.exercise_type}?")
        self.exercise_time_completed.pack(side = TOP, padx = 100, pady = 20)
        self.enter_time = self.user_input_field()
        self.pathway = 6
        self.display_submit_button()


    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Gain exercise duration ~~~~~~~~~~~~~~~~~~~~~~~~~~
    def exercise_duration(self):
        self.exercise_duration_completed = Label(self, text = f"How many minutes did your {self.exercise_type} go for?")
        self.exercise_duration_completed.pack(side = TOP, padx = 100, pady = 20)
        self.enter_duration = self.user_input_field()
        self.pathway = 7
        self.display_submit_button()


    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Gain exercise distance ~~~~~~~~~~~~~~~~~~~~~~~~~
    def exercise_distance(self):
        self.exercise_distance_completed = Label(self, text = f"What distance did you cover during your {self.exercise_type}?")
        self.exercise_distance_completed.pack(side = TOP, padx = 100, pady = 20)
        self.enter_distance = self.user_input_field()
        self.pathway = 8
        self.display_submit_button()


    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Update exercise log ~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def update_exercise_log(self):
        if self.exercise_type == "indoor run":
            self.indoor_run_log_entry = self.exercise_log.append(Fore.GREEN + f"Exercise type: {self.exercise_type}\nDate: {self.get_date}\nTime: {self.get_time}\nDuration: {self.get_duration}\nDistance: {self.get_distance}" + Fore.WHITE)
            
            """
        elif self.exercise_type == "outdoor run":
            self.outdoor_run_log_entry = self.exercise_log.append(Fore.GREEN + f"\nLatest entry\nExercise type: {self.exercise_type}\nDate: {self.outdoor_run_date}\nTime: {self.outdoor_run_time}\nDuration: {self.outdoor_run_duration}\nDistance: {self.outdoor_run_distance}" + Fore.WHITE)
            return self.outdoor_run_log_entry
        elif self.exercise_type == "indoor cycle":
            self.indoor_cycle_log_entry = self.exercise_log.append(Fore.GREEN + f"\nLatest entry\nExercise type: {self.exercise_type}\nDate: {self.indoor_cycle_date}\nTime: {self.indoor_cycle_time}\nDuration: {self.indoor_cycle_duration}\nDistance: {self.indoor_cycle_distance}" + Fore.WHITE)
            return self.indoor_cycle_log_entry
        elif self.exercise_type == "outdoor cycle":
            self.outdoor_cycle_log_entry = self.exercise_log.append(Fore.GREEN + f"\nLatest entry\nExercise type: {self.exercise_type}\nDate: {self.outdoor_cycle_date}\nTime: {self.outdoor_cycle_time}\nDuration: {self.outdoor_cycle_duration}\nDistance: {self.outdoor_cycle_distance}" + Fore.WHITE)
            return self.outdoor_cycle_log_entry
        elif self.exercise_type == "swimming laps":
            self.swimming_laps_log_entry = self.exercise_log.append(Fore.GREEN + f"\nLatest entry\nExercise type: {self.exercise_type}\nDate: {self.swimming_laps_date}\nTime: {self.swimming_laps_time}\nDuration: {self.swimming_laps_duration}\nDistance: {self.swimming_laps_duration}" + Fore.WHITE)
            return self.swimming_laps_log_entry
        elif self.exercise_type == "open ocean swim":
            self.open_ocean_swimming_log_entry = self.exercise_log.append(Fore.GREEN + f"\nLatest entry\nExercise type: {self.exercise_type}\nDate: {self.open_ocean_swimming_date}\nTime: {self.open_ocean_swimming_time}\nDuration: {self.open_ocean_swimming_duration}\nDistance: {self.open_ocean_swimming_distance}" + Fore.WHITE)
            return self.open_ocean_swimming_log_entry """

    """
    def indoor_cycle(self):
        self.indoor_cycle_date = self.exercise_date()
        self.indoor_cycle_date_check = input(Fore.GREEN + f"\nOk, so you completed your {self.exercise_type} on {self.indoor_cycle_date}. Is that correct? " + Fore.WHITE)
        if self.indoor_cycle_date_check == "yes":
            print(Fore.GREEN + "\nGreat! Let's move on." + Fore.WHITE)
            self.indoor_cycle_time = self.exercise_time()
            self.indoor_cycle_time_check = input(Fore.GREEN + f"\nJust checking: you completed your {self.exercise_type} at {self.indoor_cycle_time}. Have I got that right? " + Fore.WHITE)
            if self.indoor_cycle_time_check == "yes":
                print(Fore.GREEN + "\nExcellent! Let's keep going." + Fore.WHITE)
                self.indoor_cycle_duration = self.exercise_duration()
                self.indoor_cycle_duration_check = input(Fore.GREEN + f"Confirming: you did an {self.exercise_type} for {self.indoor_cycle_duration}? " + Fore.WHITE)
                if self.indoor_cycle_duration_check == "yes":
                    print(Fore.GREEN + "\nGreat, next question!" + Fore.WHITE)
                    self.indoor_cycle_distance = self.exercise_distance()
                    self.indoor_cycle_distance_check = input(Fore.GREEN + f"\nOk, so you did an {self.exercise_type} for {self.indoor_cycle_distance} - is that correct? " + Fore.WHITE)
                    if self.indoor_cycle_distance_check == "yes":
                        print(Fore.GREEN + "\nAlrighty then!" + Fore.WHITE)
                        self.indoor_cycle_complete_entry = input(Fore.GREEN + f"The following information will be added to your exercise log:\nDate of {self.exercise_type}: {self.indoor_cycle_date}\nTime of {self.exercise_type}: {self.indoor_cycle_time}\nDuration of {self.exercise_type}: {self.indoor_cycle_duration}\nDistance of {self.exercise_type}: {self.indoor_cycle_distance}\nAdd this entry to your log? " + Fore.WHITE)
                        if self.indoor_cycle_complete_entry == "yes":
                            self.update_exercise_log()
                            print(self.exercise_log[-1])


    def outdoor_cycle(self):
        self.outdoor_cycle_date = self.exercise_date()
        self.outdoor_cycle_date_check = input(Fore.GREEN + f"\nOk, so you completed your {self.exercise_type} on {self.outdoor_cycle_date}. Is that correct? " + Fore.WHITE)
        if self.outdoor_cycle_date_check == "yes":
            print(Fore.GREEN + "\nGreat! Let's move on." + Fore.WHITE)
            self.outdoor_cycle_time = self.exercise_time()
            self.outdoor_cycle_time_check = input(Fore.GREEN + f"\nJust checking: you completed your {self.exercise_type} at {self.outdoor_cycle_time}. Have I got that right? " + Fore.WHITE)
            if self.outdoor_cycle_time_check == "yes":
                print(Fore.GREEN + "\nExcellent! Let's keep going." + Fore.WHITE)
                self.outdoor_cycle_duration = self.exercise_duration()
                self.outdoor_cycle_duration_check = input(Fore.GREEN + f"Confirming: you did an {self.exercise_type} for {self.outdoor_cycle_duration}? " + Fore.WHITE)
                if self.outdoor_cycle_duration_check == "yes":
                    print(Fore.GREEN + "\nGreat, next question!" + Fore.WHITE)
                    self.outdoor_cycle_distance = self.exercise_distance()
                    self.outdoor_cycle_distance_check = input(Fore.GREEN + f"\nOk, so you did an {self.exercise_type} for {self.outdoor_cycle_distance} - is that correct? " + Fore.WHITE)
                    if self.outdoor_cycle_distance_check == "yes":
                        print(Fore.GREEN + "\nAlrighty then!" + Fore.WHITE)
                        self.outdoor_cycle_complete_entry = input(Fore.GREEN + f"The following information will be added to your exercise log:\nDate of {self.exercise_type}: {self.outdoor_cycle_date}\nTime of {self.exercise_type}: {self.outdoor_cycle_time}\nDuration of {self.exercise_type}: {self.outdoor_cycle_duration}\nDistance of {self.exercise_type}: {self.outdoor_cycle_distance}\nAdd this entry to your log? " + Fore.WHITE)
                        if self.outdoor_cycle_complete_entry == "yes":
                            self.update_exercise_log()
                            print(self.exercise_log[-1])


    def swimming_laps(self):
        self.swimming_laps_date = self.exercise_date()
        self.swimming_laps_date_check = input(Fore.GREEN + f"\nOk, so you were {self.exercise_type} on {self.swimming_laps_date}. Is that correct? " + Fore.WHITE)
        if self.swimming_laps_date_check == "yes":
            print(Fore.GREEN + "\nGreat! Let's move on." + Fore.WHITE)
            self.swimming_laps_time = self.exercise_time()
            self.swimming_laps_time_check = input(Fore.GREEN + f"\nJust checking: you were {self.exercise_type} at {self.swimming_laps_time}. Have I got that right? " + Fore.WHITE)
            if self.swimming_laps_time_check == "yes":
                print(Fore.GREEN + "\nExcellent! Let's keep going." + Fore.WHITE)
                self.swimming_laps_duration = self.exercise_duration()
                self.swimming_laps_duration_check = input(Fore.GREEN + f"Confirming: you were {self.exercise_type} for {self.swimming_laps_duration}? " + Fore.WHITE)
                if self.swimming_laps_duration_check == "yes":
                    print(Fore.GREEN + "\nGreat, next question!" + Fore.WHITE)
                    self.swimming_laps_distance = self.exercise_distance()
                    self.swimming_laps_distance_check = input(Fore.GREEN + f"\nOk, so you swam laps for {self.swimming_laps_distance} - is that correct? " + Fore.WHITE)
                    if self.swimming_laps_distance_check == "yes":
                        print(Fore.GREEN + "\nAlrighty then!" + Fore.WHITE)
                        self.swimming_laps_complete_entry = input(Fore.GREEN + f"The following information will be added to your exercise log:\nDate of {self.exercise_type}: {self.swimming_laps_date}\nTime of {self.exercise_type}: {self.swimming_laps_time}\nDuration of {self.exercise_type}: {self.swimming_laps_duration}\nDistance of {self.exercise_type}: {self.swimming_laps_distance}\nAdd this entry to your log? " + Fore.WHITE)
                        if self.swimming_laps_complete_entry == "yes":
                            self.update_exercise_log()
                            print(self.exercise_log[-1])


    def open_ocean_swimming(self):
        self.open_ocean_swimming_date = self.exercise_date()
        self.open_ocean_swimming_date_check = input(Fore.GREEN + f"\nOk, so you were {self.exercise_type} on {self.open_ocean_swimming_date}. Is that correct? " + Fore.WHITE)
        if self.open_ocean_swimming_date_check == "yes":
            print(Fore.GREEN + "\nGreat! Let's move on." + Fore.WHITE)
            self.open_ocean_swimming_time = self.exercise_time()
            self.open_ocean_swimming_time_check = input(Fore.GREEN + f"\nJust checking: you were {self.exercise_type} at {self.open_ocean_swimming_time}. Have I got that right? " + Fore.WHITE)
            if self.open_ocean_swimming_time_check == "yes":
                print(Fore.GREEN + "\nExcellent! Let's keep going." + Fore.WHITE)
                self.open_ocean_swimming_duration = self.exercise_duration()
                self.open_ocean_swimming_duration_check = input(Fore.GREEN + f"Confirming: you were {self.exercise_type} for {self.open_ocean_swimming_duration}? " + Fore.WHITE)
                if self.open_ocean_swimming_duration_check == "yes":
                    print(Fore.GREEN + "\nGreat, next question!" + Fore.WHITE)
                    self.open_ocean_swimming_distance = self.exercise_distance()
                    self.open_ocean_swimming_distance_check = input(Fore.GREEN + f"\nOk, so you swam laps for {self.open_ocean_swimming_distance} - is that correct? " + Fore.WHITE)
                    if self.open_ocean_swimming_distance_check == "yes":
                        print(Fore.GREEN + "\nAlrighty then!" + Fore.WHITE)
                        self.open_ocean_swimming_complete_entry = input(Fore.GREEN + f"The following information will be added to your exercise log:\nDate of {self.exercise_type}: {self.open_ocean_swimming_date}\nTime of {self.exercise_type}: {self.open_ocean_swimming_time}\nDuration of {self.exercise_type}: {self.open_ocean_swimming_duration}\nDistance of {self.exercise_type}: {self.open_ocean_swimming_distance}\nAdd this entry to your log? " + Fore.WHITE)
                        if self.open_ocean_swimming_complete_entry == "yes":
                            self.update_exercise_log()
                            print(self.exercise_log[-1])"""
    

new_exercise = Exercise_Log()
new_exercise.mainloop()