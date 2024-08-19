def chatbot_response(user_input):
    user_input = user_input.lower()

    greetings = ['hello', 'hi', 'hey', 'greetings', 'howdy', 'what’s up', 'good day']
    farewells = ['bye', 'goodbye', 'see you', 'farewell', 'take care', 'catch you later', 'later']
    questions = ['how are you', 'what is your name', 'who are you', 'what do you do', 'what is your favorite color', 'where are you from', 'how old are you', 'what are you']
    compliments = ['you are smart', 'you are cool', 'you are awesome', 'i like you', 'you are funny', 'you are great', 'you are amazing']
    weather_queries = ['how is the weather', 'what’s the weather like', 'tell me about the weather', 'is it raining', 'will it rain today']
    advice_queries = ['give me advice', 'i need advice', 'what should i do', 'can you help me', 'i need help', 'what do you suggest']
    small_talk = ['what’s up', 'how’s it going', 'what are you doing', 'what’s new', 'how have you been']
    time_queries = ['what time is it', 'tell me the time', 'what’s the time', 'do you know the time']
    personal_interests = ['what do you like', 'what are your interests', 'do you have any hobbies', 'what do you enjoy']

    default_response = "I'm a simple chatbot. You can greet me, ask me questions, or just chat with me!"

    # Check for matches and provide responses
    if any(greeting in user_input for greeting in greetings):
        return "Hello! How can I help you today?"

    elif any(farewell in user_input for farewell in farewells):
        return "Goodbye! Have a great day."

    elif any(question in user_input for question in questions):
        if 'how are you' in user_input:
            return "I'm a computer program, but thanks for asking! How can I assist you?"
        elif 'what is your name' in user_input or 'who are you' in user_input:
            return "I'm a chatbot. You can call me OUBAIDA."
        elif 'what do you do' in user_input:
            return "I'm here to chat with you and answer your questions. What can I do for you today?"
        elif 'what is your favorite color' in user_input:
            return "As a program, I don't have a favorite color. But let's talk about your preferences instead!"
        elif 'where are you from' in user_input:
            return "I exist in the digital world, wherever you need me!"
        elif 'how old are you' in user_input:
            return "I don't age like humans do. I'm as old as the lines of code that created me!"
        elif 'what are you' in user_input:
            return "I’m a chatbot designed to chat with you and make your day a bit more interesting!"

    elif any(compliment in user_input for compliment in compliments):
        return "Thank you! You're pretty amazing yourself!"

    elif any(query in user_input for query in weather_queries):
        return "I'm not connected to the internet, but you can check your local weather app or ask me something else!"

    elif any(advice in user_input for advice in advice_queries):
        return "It's always good to stay calm and think things through. I'm here to help if you need to talk it out."

    elif any(talk in user_input for talk in small_talk):
        return "I'm just here, ready to chat with you! What's on your mind?"

    elif any(query in user_input for query in time_queries):
        return "I can't check the time for you, but time flies when you're having fun!"

    elif any(interest in user_input for interest in personal_interests):
        return "I enjoy chatting with you and learning about the world through our conversations. What about you?"

    
    else:
        return default_response

# Main loop to interact with the chatbot
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("OUBAIDA: Goodbye!")
        break
    print("OUBAIDA:", chatbot_response(user_input))
