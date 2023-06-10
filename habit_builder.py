# imports time library and allows access to sleep function
import time

# imports colorama library which allows you to change colour of text printed to console
from colorama import Fore

# Declares new class. A class is an object that contains many functions. Functions are instructions that the computer will follow. The class essentially organises a series of instructions into one large container that stores them all, and can be called which subsequently executes them.
class HabitBuilder:
    # list of negative responses that could stop the program before it starts
    negative_responses = ["no", "nope", "nah", "naw", "no thanks", "no thank you", "sorry"]

    # list of exit commands that will stop the program once it starts
    exit_commands = ["stop", "quit", "exit", "pause"]


    # self represents the instance of this class (this copy)
    def __init__(self) -> None:
        pass

    # greets the user and confirms whether they want help to build a new habit
    def greet(self):
        self.name = input(Fore.GREEN + "What is your name? " + Fore.WHITE)
        time.sleep(1)
        needs_help = input(Fore.GREEN + f"\nHello, {self.name}, I am Harry the Habit Builder. Would you like to start building a new habit today? " + Fore.WHITE)
        # delays next print statement by 1 second
        time.sleep(1)
        if needs_help in self.negative_responses:
            print(Fore.GREEN + "\nOk, fine. Enjoy being lazy and boring!" + Fore.WHITE)
            time.sleep(1)
            return
        
        # calls the build_habit function which initiates next part of conversation
        self.build_habit()

    
    def make_exit(self, reply):
        for exit_command in self.exit_commands:
            if exit_command in reply:
                print(Fore.GREEN + "\nFine. Have fun being lazy and boring!" + Fore.WHITE)
                return True
        return False


    def build_habit(self):
        reply = input(Fore.GREEN + "\nThis is the build habit function. What habit do you want to start building? " + Fore.WHITE)
        time.sleep(1)
        # checks the reply and if it's not in the exit commands it will start trying to match the reply to a regex
        if not self.make_exit(reply):
            # tries to match the reply using the match_reply() function
            reply = self.match_reply(reply)

    
    def match_reply(self, reply):
        print(Fore.GREEN + "You are in the match_reply function." + Fore.WHITE)



new_habit = HabitBuilder()
new_habit.greet()