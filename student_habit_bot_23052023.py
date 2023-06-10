import time
import os



class Habit_Bot:
    # Defining lists for later use
    negative_response = ["no", "nah", "nope"]
    positive_response = ["yes", "yeah", "yep", "yas"]
    reading = ["reading", "reading more", "read"]
    meditation = ["meditating", "meditation"]
    sleep = ["sleeping", "sleep more", "sleep", "shut eye"]
    stop = ["pause", "stop"]


    # Creating instance (self)
    def __int__(self):
        pass


    # Greeting user and starting conversation
    def greet(self):
        # Clearing terminal to prepare for clean execution of program and easy reading - I like this!
        os.system("cls" if os.name == "nt" else "clear")

        greeting = input("Hello! I'm your personal Habit bot trainer. I'm here to help build any habit you want. Are you ready?")
        # Checking whether the users input corresponds to any of the strings outlined in list above.
        if greeting .lower() .strip() in self.negative_response: # I like that you've stripped the whitespace from the input and transformed to lower case for easier processing
            os.system("cls" if os.name == "nt" else "clear")
            print("I'm sorry to hear that, I'm here whenever you are ready to jump in! \nRemember: 'It's a lot more than mind over matter. It takes relentless self-discipline to schedule suffering into your day, every day.' - David Goggins")
            input ("Just press continue when you are ready")
            # calling greet() function again to loop back to the start and run program again - good way of keeping the program active
            self.greet()
        # Same thing here
        elif greeting .lower() .strip() in self.positive_response:
            ("Good to hear!")
            self.name()
        # Saftey net for incorrect inputs
        elif greeting .lower() .strip() in self.stop:
            self.stop1()
        else:
            os.system("cls" if os.name == "nt" else "clear")
            print("Incorrect input")
            time.sleep(2)
            self.greet()

    # Ask for name
    def name(self):
        global user_name # you can take this out of here - you can access user_name by calling it self.user_name then referring to it as self.user_name when calling it in other functions with the same value that it gets set in here.
        user_name = input("Firsty, let's get acquainted with eachother. You already know me, I'm PHB, Perosnal Habit Builder. But I don't know your name. What is it?")
        self.habit_choice()

    # Cross road which will now split off into any habit the user chooses
    def habit_choice(self): 
        habit_choice = input(f"Great {user_name}. Good to meet you. Let's get right into it. \nWhat habit would you like to build?")
        if habit_choice .lower() .strip() in self.reading:
            self.reading_plan_input()
        elif habit_choice .lower() .strip() in self.meditation:
            self.meditation_plan()
        elif habit_choice .lower() .strip() in self.sleep:
            self.sleep_plan()
        elif habit_choice .lower() .strip() in self.stop:
            self.stop1()
        else:
            os.system("cls" if os.name == "nt" else "clear")
            print("Incorrect input")
            time.sleep(2)
            self.habit_choice()
    
    # Sleeping Habit
    def sleep_plan(self):
        print("Great! Too often sleeping becomes an overlooked component of health today. Let's fix that!")
        print(f"To create a sleeping plan perfect for you, {user_name}, I just need to ask a few questions.")
        custom_sleep = input("Firstly, would you like to set a custom sleep amount?")
        if custom_sleep .lower() .strip() in self.positive_response:
            self.custom_sleep_plan()
        elif custom_sleep .lower() .strip() in self.negative_response:
            self.create_sleep_plan()
        else: 
            os.system("cls" if os.name == "nt" else "clear")
            print("Incorrect input")
            time.sleep(2)
            self.sleep_plan()

    # If the user just wants to set a custom sleep amount
    def custom_sleep_plan(self):
        global sleep_amount # same here - call your variable self.sleep_amount then you will be able to call it in other functions with the same value it gets set here
        input_sleep_amount = input("How long do you sleep for?")
        if input_sleep_amount .isdigit() == False:
            print("That is not a number, dumbass.") # brilliant. Savage, but brilliant. Probably should reword before the conference though.
            self.custom_sleep_plan()
        sleep_amount = int(input_sleep_amount)

    # Calculates how much the user needs using their age
    def create_sleep_plan(self):
        input_age = input("How old are you? (Years)")
        if input_age.isdigit() == False: # good use of the .isdigit() function, very efficient way of checking for correct input.
            print("That is not a number, dumbass")
            self.create_sleep_plan() 
        age = int(input_age)
        if age <= 1:
            sleep_amount = ("12-16 Hours")
        if age <= 2:
            sleep_amount = ("11-14 Hours")
        if age <= 5:
            sleep_amount = ("10-13 Hours")
        if age <= 12:
            sleep_amount = ("9-12 Hours")
        if age <= 18:
            sleep_amount = ("8-10 Hours")
        if age <= 60:
            sleep_amount = ("7 or More Hours")
        if age <= 64:
            sleep_amount = ("7-9 Hours")
        if age >= 65:
            sleep_amount = ("7-8 Hours")
        print(sleep_amount)  

    # Meditation Habit
    def meditation_plan(self):
        print("Alright sounds good, so important to slow down sometimes, especially in today's always busy society.")
     
    # Reading habit that creates a week by week plan for reading time
    def reading_plan_input(self):
        print("Alright great! Thats a great habit to start building. First I have to ask you a few questions to help me create a plan that best suits you.")
        how_read_now_input = input("How long do you read for per day?(Minutes)")
        if how_read_now_input.isdigit() == False:
            print("That is not a number, dumbass")
            self.reading_plan_input()
        else:
            how_read_want_input = input("How long do you want to read for per day? (Minutes)")
            if how_read_want_input.isdigit() == False:
                print("That is not a number, dumbass")
                self.reading_plan_input()
            else:
                how_long_input = input("How long do you have to reach your goal? (Weeks)")
                if how_long_input.isdigit() == False:
                    print("That is not a number, dumbass")
                    self.reading_plan_input()
    
        how_long = int(how_long_input)
        how_read_now = int(how_read_now_input)
        how_read_want = int(how_read_want_input)

        plan = (how_read_want - how_read_now)

        result = (plan/how_long)

        days = (how_long*7)

        # Assigning a modular variable for each week that can be displayed if needed
        # Probably not the most efficient solution but IDK how to use loops :)
        week_1 = round((result + how_read_now))
        week_2 = round((result*2 + how_read_now))
        week_3 = round((result*3 + how_read_now))
        week_4 = round((result*4 + how_read_now))
        week_5 = round((result*5 + how_read_now))
        week_6 = round((result*6 + how_read_now))
        week_7 = round((result*7 + how_read_now))
        week_8 = round((result*8 + how_read_now))
        week_9 = round((result*9 + how_read_now))
        week_10 = round((result*10 + how_read_now))
        week_11 = round((result*11 + how_read_now))
        week_12 = round((result*12 + how_read_now))
 
        # Checking to see how many weeks the user wants and only displaying needed weeks
        print("Here is your schedule. You should aim to read this amount every day for each week:")
        if how_long >= 1:
            print(f"Week 1: {week_1} Minutes")
        if how_long >= 2:
            print(f"Week 2: {week_2} Minutes")
        if how_long >= 3:
            print(f"Week 3: {week_3} Minutes")
        if how_long >= 4:
            print(f"Week 4: {week_4} Minutes")
        if how_long >= 5:
            print(f"Week 5: {week_5} Minutes")
        if how_long >= 6:
            print(f"Week 6: {week_6} Minutes")
        if how_long >= 7:
            print(f"Week 7: {week_7} Minutes")
        if how_long >= 8:
            print(f"Week 8: {week_8} Minutes")
        if how_long >= 9:
            print(f"Week 9: {week_9} Minutes")
        if how_long >= 10:
            print(f"Week 10: {week_10} Minutes")
        if how_long >= 11:
            print(f"Week 11: {week_11} Minutes")
        if how_long >= 12:
            print(f"Week 12: {week_12} Minutes")
        if how_long >= 13:
            print("That is too many weeks")

        print("Now we have a basic plan. Are there any changes you would like to make?\nWe can adjust your plan to account for any days that you do not have time to read.")
        print(days)

    def stop1(self):
        print("Stop right there criminal scum!")


# Actually calling the functions (Creating a variable for the class)
bot = Habit_Bot()
bot.greet()