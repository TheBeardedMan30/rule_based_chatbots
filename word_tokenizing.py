from nltk.tokenize import word_tokenize


def customer_service_officer():
    print("Hello, I'm sorry to hear you're not having a positive experience. One moment and I will try to assist you.")

def determine_sentiment():
    negative_sentiment = ["angry", "bad", "upset", "broken"]

    user_response = input("What can I help you with today?")
    user_response_tokenized = word_tokenize(user_response)

    negative_sentiment_count = 0

    for word in user_response_tokenized:
        if word in negative_sentiment:
            negative_sentiment_count += 1
        else:
            pass

    if negative_sentiment_count > 0:
        customer_service_officer()

determine_sentiment()