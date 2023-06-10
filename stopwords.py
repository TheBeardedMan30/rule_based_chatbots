from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

stop_words = set(stopwords.words("english"))

#print(stop_words)

exercise_type_list = ["indoor run", "outdoor run"]

response = input("Enter exercise type: ")
response_tokenized = word_tokenize(response)

response_list = []

for word in response_tokenized:
    if word not in stop_words:
        response_list.append(word)

print(response_list)

response_match = []

for item in response_list:
    if item in exercise_type_list:
        if item == "run":
            confirm_run = input("I found two possible matches. Which option did you want to choose?\n1. Indoor run\n2. Outdoor run\n3. None")
            if confirm_run == "1":
                print("You have logged an indoor run.")

print(response_match)
print(exercise_type_list)