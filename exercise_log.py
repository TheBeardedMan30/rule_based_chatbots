import time

from colorama import Fore



class Exercise_Log:

    negative_responses = ['no', 'nah', 'not yet', 'no thanks']
    exit_commands = ['quit', 'stop', 'exit']
    exercise_type_list = ['indoor run', 'outdoor run', 'indoor cycle', 'outdoor cycle', 'swimming laps', 'open ocean swim']
    exercise_log = []


    def __init__(self) -> None:
        pass


    def greet(self):
        self.user_name = input(Fore.GREEN + "Welcome to Track Your Moves! Before we get started logging your exercises, what is your name? " + Fore.WHITE)
        self.proceed = input(Fore.GREEN + f"\nHi, {self.user_name}, would you like to log a new exercise? " + Fore.WHITE)
        if self.proceed in self.negative_responses:
            print(Fore.GREEN + "Ok then, no worries!" + Fore.WHITE)
        else:
            self.handle_conversation()


    def handle_conversation(self):
        print(Fore.GREEN + "\nOk, give me a moment to prepare for logging your new exercise." + Fore.WHITE)
        self.exercise_type = input(Fore.GREEN + "\nWhat type of exercise would you like to log? " + Fore.WHITE)
        if self.exercise_type in self.exercise_type_list:
            print(Fore.GREEN + f"\nSure, I can log an {self.exercise_type} for you. " + Fore.WHITE)
            if self.exercise_type == self.exercise_type_list[0]:
                self.indoor_run()
            elif self.exercise_type == self.exercise_type_list[1]:
                self.outdoor_run()
            elif self.exercise_type == self.exercise_type_list[2]:
                self.indoor_cycle()
            elif self.exercise_type == self.exercise_type_list[3]:
                self.outdoor_cycle()
            elif self.exercise_type == self.exercise_type_list[4]:
                self.swimming_laps()
            elif self.exercise_type == self.exercise_type_list[5]:
                self.open_ocean_swimming()


    def indoor_run(self):
        self.indoor_run_date = self.exercise_date()
        self.indoor_run_date_check = input(Fore.GREEN + f"\nOk, so you completed your {self.exercise_type} on {self.indoor_run_date}. Is that correct? " + Fore.WHITE)
        if self.indoor_run_date_check == "yes":
            print(Fore.GREEN + "\nGreat! Let's move on." + Fore.WHITE)
            self.indoor_run_time = self.exercise_time()
            self.indoor_run_time_check = input(Fore.GREEN + f"\nJust checking: you completed your {self.exercise_type} at {self.indoor_run_time}. Have I got that right? " + Fore.WHITE)
            if self.indoor_run_time_check == "yes":
                print(Fore.GREEN + "\nExcellent! Let's keep going." + Fore.WHITE)
                self.indoor_run_duration = self.exercise_duration()
                self.indoor_run_duration_check = input(Fore.GREEN + f"Confirming: you did an {self.exercise_type} for {self.indoor_run_duration}? " + Fore.WHITE)
                if self.indoor_run_duration_check == "yes":
                    print(Fore.GREEN + "\nGreat, next question!" + Fore.WHITE)
                    self.indoor_run_distance = self.exercise_distance()
                    self.indoor_run_distance_check = input(Fore.GREEN + f"\nOk, so you did an {self.exercise_type} for {self.indoor_run_distance} - is that correct? " + Fore.WHITE)
                    if self.indoor_run_distance_check == "yes":
                        print(Fore.GREEN + "\nAlrighty then!" + Fore.WHITE)
                        self.indoor_run_complete_entry = input(Fore.GREEN + f"The following information will be added to your exercise log:\nDate of {self.exercise_type}: {self.indoor_run_date}\nTime of {self.exercise_type}: {self.indoor_run_time}\nDuration of {self.exercise_type}: {self.indoor_run_duration}\nDistance of {self.exercise_type}: {self.indoor_run_distance}\nAdd this entry to your log? " + Fore.WHITE)
                        if self.indoor_run_complete_entry == "yes":
                            self.update_exercise_log()
                            print(self.exercise_log[-1])

    def outdoor_run(self):
        self.outdoor_run_date = self.exercise_date()
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
                            print(self.exercise_log[-1])


    def exercise_date(self):
        self.exercise_date_completed = input(Fore.GREEN + f"On what date did you complete your {self.exercise_type}? " + Fore.WHITE)
        return self.exercise_date_completed
    
    def exercise_time(self):
        self.exercise_time_completed = input(Fore.GREEN + f"At what time did you complete your {self.exercise_type}? " + Fore.WHITE)
        return self.exercise_time_completed
    
    def exercise_duration(self):
        self.exercise_duration_completed = input(Fore.GREEN + f"What was the duration of your {self.exercise_type}?" + Fore.WHITE)
        return self.exercise_duration_completed
    
    def exercise_distance(self):
        self.exercise_distance_completed = input(Fore.GREEN + f"What distance did you cover during your {self.exercise_type}? " + Fore.WHITE)
        return self.exercise_distance_completed
    
    def update_exercise_log(self):
        # create exercise log list then append the details of the latest exercise to that list
        if self.exercise_type == "indoor run":
            self.indoor_run_log_entry = self.exercise_log.append(Fore.GREEN + f"\nLatest entry\nExercise type: {self.exercise_type}\nDate: {self.indoor_run_date}\nTime: {self.indoor_run_time}\nDuration: {self.indoor_run_duration}\nDistance: {self.indoor_run_distance}" + Fore.WHITE)
            return self.indoor_run_log_entry
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
            return self.open_ocean_swimming_log_entry



new_exercise = Exercise_Log()
new_exercise.greet()

new_exercise_2 = Exercise_Log()
new_exercise_2.greet()