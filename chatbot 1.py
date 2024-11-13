import re

# Define the rules and responses in a dictionary
rules = {
    "hello": "Hi there! How can I assist you today?",
    "hi": "Hello! How can I help you?",
    "how are you": "I'm just a bot, but I'm doing great! How about you?",
    "what is your name": "I am a friendly chatbot, created to assist you.",
    "bye": "Goodbye! Have a great day!",
    "default": "Sorry, I didn't understand that. Can you rephrase?"
}

# Function to clean and match the user input
def get_response(user_input):
    # Clean the user input by converting it to lowercase
    user_input = user_input.lower().strip()

    # Check if the user input matches any of the rules
    for pattern in rules:
        if re.search(r'\b' + re.escape(pattern) + r'\b', user_input):
            return rules[pattern]
    
    # Default response if no match is found
    return rules["default"]

# Main chatbot loop
def chatbot():
    print("Chatbot: Hello! I am here to assist you. Type 'bye' to exit.")
    
    while True:
        # Get input from the user
        user_input = input("You: ")
        
        # If the user says 'bye', end the conversation
        if user_input.lower() == "bye":
            print("Chatbot: Goodbye!")
            break
        
        # Get the response based on the input
        response = get_response(user_input)
        print("Chatbot:", response)

# Run the chatbot
if __name__ == "__main__":
    chatbot()
