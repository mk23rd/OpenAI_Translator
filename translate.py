#make chatbot with GPT-4 Turbo api key

import openai

# Set your OpenAI API key
openai.api_key = 'your api key'

def chat_with_gpt4_turbo(prompt):
    response = openai.Completion.create(
        engine="text-gpt4-turbo",  # Use the GPT-4 Turbo engine
        prompt=prompt,
        max_tokens=50  # Adjust as needed
    )
    return response.choices[0].text.strip()

def main():
    print("Welcome to the GPT-4 Turbo Chatbot!")
    print("You can start chatting with the bot. Type 'exit' to quit.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break
        
        # Let GPT-4 Turbo generate a response based on user input
        response = chat_with_gpt4_turbo(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()
