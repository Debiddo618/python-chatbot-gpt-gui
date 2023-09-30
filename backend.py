import openai

class Chatbot:
    def __init__(self):
        openai.api_key = "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"

    def get_response(self,user_input):
        response = openai.Completion.create(
            engine = "text-davinci-003",
            prompt=user_input,
            max_tokens=3000,
            temperature=0.5
        ).choices[0].text
        return response

if __name__ == "__main__":
    chatbot = Chatbot()
    response = chatbot.get_response("Popular anime 2023")
    print(response)