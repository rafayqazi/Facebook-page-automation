import bard

class Chatbot:
    def __init__(self, api_key):
        self.api_key = api_key
        self.bard = bard.Bard(api_key)

    def get_response(self, message):
        response = self.bard.generate_text(message)
        return response

    def run(self):
        while True:
            message = input("Enter your message: ")
            response = self.get_response(message)
            print(response)

if __name__ == "__main__":
    api_key = "YOUR_API_KEY"
    chatbot = Chatbot(api_key)
    chatbot.run()
