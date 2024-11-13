def chatbot_response(user_input):
    # Normalize the input to lower case for easier comparison
    user_input = user_input.lower()

    # Decision tree
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I assist you today?"
    elif "how are you" in user_input:
        return "I'm just a program, but thanks for asking! How about you?"
    elif "help" in user_input:
        return "Sure! What do you need help with?"
    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Have a great day!"
    else:
        return "I'm not sure how to respond to that. Can you ask something else?"

# Example interaction
user_input = input("You: ")
response = chatbot_response(user_input)
print("Chatbot:", response)
