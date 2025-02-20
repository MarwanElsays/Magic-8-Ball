import random

responses = [
    "Yes, definitely!",
    "No, not now.",
    "Ask again later.",
    "It is certain.",
    "Very doubtful.",
    "Outlook is good.",
    "Better not tell you now.",
    "Concentrate and ask again."
]

def get_random_response():
    return random.choice(responses)

def get_user_question():          
    question = input("Ask the magical 8 Ball a question (type 'exit' to quit): ")    
    if question.lower() == "exit":         
        return None         
    return question

def display_response(response):
    print("\n🔮 The Magic 8-Ball says:", response, "\n")