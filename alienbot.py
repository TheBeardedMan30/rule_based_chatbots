# importing regex and random libraries
import re, random



class AlienBot:
    # potential negative responses
    negative_responses = ("no", "nope", "nah", "naw", "not a chance", "sorry")
    # keywords for exiting the conversation
    exit_commands = ("quit", "pause", "exit", "goodbye", "bye", "later", "cya", "seeya", "g2g", "gtg")
    # random starter questions
    random_questions = (
        "Why are you here? ",
        "Are there many humans like you? ",
        "What do you consume for sustenance? ",
        "Is there intelligent life on this planet? ",
        "Does Earth have a leader? ",
        "What planets have you visited? ",
        "What technology do you have on this planet? "
    )


    def __init__(self) -> None:
        self.alienbabble = {"describe_planet_intent": r".*\s*your planet.*", "answer_why_intent": r"why\sare.*", "cubed_intent": r".*\s*cube.*number (\d+)"}
        

    def greet(self):
        self.name = input("What is your name? ")
        
        will_help = input(f"Greetings, {self.name}, I am Zog. I'm not from this planet; my homeworld is Zogtron. Will you help me learn about your planet? ")

        if will_help in self.negative_responses:
            print("Ok, fine. You will be the first to be vaporised...")
            return
        
        self.chat()

    
    def make_exit(self, reply):
        for exit_command in self.exit_commands:
            if exit_command in reply:
                print("Alrighty then. To the vaporiser you go!")
                return True


    def chat(self):
        reply = input(random.choice(self.random_questions)).lower()
        while not self.make_exit(reply):
            reply = input(self.match_reply(reply))


    def match_reply(self, reply):
        for key, values in self.alienbabble.items():
            intent = key
            regex_pattern = values

            found_match = re.match(regex_pattern, reply)

            if found_match and intent == "describe_planet_intent":
                return self.describe_planet_intent()
            elif found_match and intent == "answer_why_intent":
                return self.answer_why_intent()
            elif found_match and intent == "cubed_intent":
                return self.cubed_intent(found_match.groups()[0])
            else:
                return self.no_match_intent()


    def describe_planet_intent(self):
        responses = ("My planet is a utopia of diverse organisms and species. ", "I am from Opidipus, the capital of the Wayward Galaxies. ")
        return random.choice(responses)
    

    def answer_why_intent(self):
        responses = ("I come in peace. ", "I am here to collect data on your planet and its inhabitants. ", "I heard the coffee is good. ")
        return random.choice(responses)
    

    def cubed_intent(self, number):
        number = int(number)
        cubed_number = number*number*number
        return (f"The cube of {number} is {cubed_number}. Isn't that cool? ")
    

    def no_match_intent(self):
        responses = ("Please tell me more. ", "Tell me more! ", "Why do you say that? ", "I see. Can you elaborate? ", "Interesting. Can you tell me more? ", "I see. How do you think? ", "Why? ", "How do you think I feel when you say that? ")
        return random.choice(responses)
    


Zog = AlienBot()
Zog.greet()