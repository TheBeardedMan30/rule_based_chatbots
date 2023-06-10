import re, random



#Functions (def ....) do specific things, whereas classes (class...) are specific things.
#The class below is a chunk of code containing functions that is designed to carry out multiple sets of instructions (an object created by the user).
#Declares class (object) called SupportBot.
class SupportBot:
    #Tuple (finite ordered list of elements) of negative responses
    negative_responses = ("nothing", "don't", "stop", "sorry", "nevermind")
    #Tuple of commands user can input to exit the SupportBot object
    exit_commands = ("quit", "pause", "exit", "goodbye", "bye", "later", "cya", "seeya")


    #_init_ is a constructor in object oriented concepts. Called when an object is created from the class and allows class to initialise its attributes.
    #'self' variable represents the instance of the class, allows us to access the attributes and methods of the class.
    #More info here: https://micropyramid.com/blog/understand-self-and-__init__-method-in-python-class/
    def __init__(self):
        #Class variable, dictionary with strings for regular expression matching - **currently issues with this when trying to pay bill
        #. at start means there can be any character there except new line
        #.* at end means there can be any number of other characters there except new line
        #Improve these matching_phrases regex by using things like 'help paying my bill' or how do i pay my bill' so they are very different to wanting to pay
        #self.matching_phrases = {'how_to_pay_bill': [r'.*how to.*pay bills.*', r'.*how to.*pay my bill.*'], r'pay_bill': [r'.*want to.*pay my bill.*', r'.*need to.*pay my bill.*']}
        self.matching_phrases = {"how_to_pay_bill": [r'.+help.+paying bills.*', r'.+how to.+pay my bill.*'], r'pay_bill': [r'.*want to pay my bill.*the.*account number.*is (\d+)', r'.*need to.*pay my bill.*the.*account number.*is (\d+)', r'.*want to pay my bill.*my.*account number.*is (\d+)', r'.*need to.*pay my bill.*my.*account number is (\d+)']}

        
    #Defines the 'welcome' function that runs after _init_ has allocated attributes.
    def welcome(self):
        name = input("Hi, I'm a customer support representative. Welcome to Codecademy Bank. Before we can help you, I need some information from you. What is your first name and last name? ")
        #f...{} is interpolation - inserting previously used variables at point where {} occur in strings. Must have f at start of input / print statement.
        will_help = input(f"Okay {name}, what can I help you with? ")

        if will_help in self.negative_responses:
            print("Okay, confusing, but have a great day!")
            return
        
        #Calls handle_conversation function and continues conversing with user.
        self.handle_conversation(will_help)


    #Function that acts as central function for continually handling responses for as long as user asks questions.
    #Accepts one argument / parameter - 'reply'
    def handle_conversation(self, reply):
        print("Conversation is being handled")
        #Checks value of the reply, and will continue with same response until reply is stop
        while not self.make_exit(reply):
            reply = self.match_reply(reply)

    
    #Function that checks whether user response contains word from exit_commands tuple
    def make_exit(self, reply):
        for exit_command in self.exit_commands:
            if exit_command in reply:
                print("Ok, have a great day!")
                return True
        return False

                
    #Function used to match user utterances (inputs) to suitable replies
    def match_reply(self, reply):
        #iterates over each item in self.matching_phrases dictionary (accesses dictionary and goes over each key and each value attached to that key)
        for key, values in self.matching_phrases.items():
            #iterate over matching patterns in current list of regex expressions (accesses each value in dictionary and performs action with the regex expressions (regex_pattern) it finds there)
            for regex_pattern in values:
                #use for debugging - shows what regex_patterns are matching to user input
                print(regex_pattern)
                #re.match() function checks if current regex_pattern matches user utterance (reply)
                found_match = re.match(regex_pattern, reply)
                #Conditional checks if found_match is True and if it matches one of the regular expressions
                if found_match and key == "how_to_pay_bill":
                    #accesses self.how_to_pay_bill_intent() and returns value from it
                    return self.how_to_pay_bill_intent()
                elif found_match and key == "pay_bill":
                    #accesses self.pay_bill_intent() and returns value stored in first group from it
                    return self.pay_bill_intent(found_match.groups()[0])
        #Runs this return input statement if found_match is False
        return input("I did not understand you. Can you please ask your question differently? ")

    
    #accessed when match_reply() finds user input matching the regular expressions attached to this
    def how_to_pay_bill_intent(self):
        #this is the response, or entity, that is passed back
        return input("You can pay your bill a couple of ways. 1) online at bill.codecademybank.com or 2) you can pay your bill right now with me. Can I help you with anything else? ")
    

    #accessed when match_reply() finds user input matching the regular expressions attached to this
    def pay_bill_intent(self, account_number = None):
        print(account_number)
        #this is the response, or entity, that is passed back
        return input(f"The account with number {account_number} was paid off. What else can I help you with? ")



SupportConversation = SupportBot()
SupportConversation.welcome()