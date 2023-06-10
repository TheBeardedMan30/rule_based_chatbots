import os
import time

negative_responses = ["no", "nah", "not yet"]
print(negative_responses) # prints the whole list

negative_responses.append("yes") # adds 'yes' to the end of the list
print(negative_responses) # prints the updated list

print(negative_responses[-1]) # prints the last item
print(negative_responses[-2]) # prints the second last item
print(negative_responses[0]) # prints the first item
print(negative_responses[1]) # prints the second item
print(negative_responses[0:3]) # prints the first three items

time.sleep(1)

#os.system("cls" if os.name == "nt" else "clear")