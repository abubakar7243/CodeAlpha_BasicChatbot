
import random


def get_reply(message):
    message = message.lower().strip()

    if message in ["hello", "hi", "hey"]:
        return "Hello! Welcome to CodeBot. How can I help you?"

    elif message in ["how are you", "how are you doing"]:
        return "I'm doing great! Thanks for asking. How are you?"

    elif message in ["what is your name", "your name"]:
        return "My name is CodeBot. I'm your personal Python chatbot."

    elif message in ["who created you", "who made you"]:
        return "I was created by a Python programming student."

    elif message in ["what is python", "tell me about python"]:
        return "Python is a popular, beginner-friendly programming language."

    elif message in ["what can you do", "your purpose"]:
        return "I can chat with you and answer simple questions."

    elif message in ["how old are you", "your age"]:
        return "I'm a chatbot, so I don't have an age!"

    elif message in ["thank you", "thanks"]:
        return "You're welcome! Happy to help."

    elif message == "good morning":
        return "Good morning! Have a wonderful day."

    elif message == "good night":
        return "Good night! Sweet dreams."

    elif message in ["what is your favorite color", "favorite color"]:
        return "I like blue! It reminds me of technology."

    elif message in ["tell me a joke", "joke"]:
        jokes = [
            "Why do programmers prefer dark mode? Because light attracts bugs!",
            "Why did the computer go to the doctor? Because it had a virus!",
            "Why do Python programmers wear glasses? Because they cannot C!"
        ]
        return random.choice(jokes)

    elif message in ["help", "commands"]:
        return (
            "Available commands:\n"
            "1. Hello\n"
            "2. How are you\n"
            "3. What is your name\n"
            "4. Who created you\n"
            "5. What is Python\n"
            "6. What can you do\n"
            "7. Tell me a joke\n"
            "8. Good morning\n"
            "9. Thank you\n"
            "10. Bye"
        )

    elif message in ["bye", "goodbye", "exit", "quit"]:
        return "Goodbye! Thanks for chatting with CodeBot. Have a great day!"

    elif message == "":
        return "Please type something so I can respond."

    else:
        return "Sorry, I don't understand that. Type 'help' to see available commands."


def main():
    print("=" * 45)
    print("          WELCOME TO CODEBOT")
    print("=" * 45)
    print("Hello! I'm CodeBot, your Python chatbot.")
    print("Type 'help' to see available commands.")
    print("Type 'bye' to exit the chatbot.")
    print("=" * 45)

    while True:
        try:
            user = input("\nYou: ")
            reply = get_reply(user)

            print("CodeBot:", reply)

            if user.lower().strip() in ["bye", "goodbye", "exit", "quit"]:
                break

        except (KeyboardInterrupt, EOFError):
            print("\nCodeBot: Goodbye! Have a great day!")
            break


if __name__ == "__main__":
    main()
