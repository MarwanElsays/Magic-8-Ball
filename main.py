def get_user_question():          
    question = input("Ask the magical 8 Ball a question (type 'exit' to quit): ")    
    if question.lower() == "exit":         
        return None         
    return question