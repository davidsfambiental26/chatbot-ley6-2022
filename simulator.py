class Ley2022Chatbot:
    def __init__(self):
        self.introduction = "Welcome to the Ley 7/2022 Chatbot! I can assist you with information regarding Ley 7/2022."
        self.instructions = "You can ask me questions like 'What is Ley 7/2022?' or 'What are the implications of Ley 7/2022?'"

    def get_response(self, question):
        responses = {
            "What is Ley 7/2022?": "Ley 7/2022 is a legislation that aims to...",
            "What are the implications of Ley 7/2022?": "The implications include...",
            "Who does Ley 7/2022 affect?": "Ley 7/2022 affects..."
        }
        return responses.get(question, "I'm not sure about that. Please ask another question.")

    def simulate_conversation(self):
        print(self.introduction)
        print(self.instructions)
        while True:
            question = input("You: ")
            if question.lower() in ['exit', 'quit']:
                print("Chatbot: Thank you for chatting. Goodbye!")
                break
            response = self.get_response(question)
            print(f"Chatbot: {response}")


if __name__ == "__main__":
    chatbot = Ley2022Chatbot()
    chatbot.simulate_conversation()