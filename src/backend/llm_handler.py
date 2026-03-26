import openai

class LLMHandler:
    def __init__(self, api_key):
        openai.api_key = api_key

    def generate_response(self, context, documents):
        prompt = self.create_prompt(context, documents)
        response = openai.ChatCompletion.create(
            model='gpt-4',
            messages=[{'role': 'user', 'content': prompt}]
        )
        return response['choices'][0]['message']['content']

    def create_prompt(self, context, documents):
        prompt = f"Legal Context: {context}\n\nDocuments:\n"
        for doc in documents:
            prompt += f"- {doc}\n"
        prompt += '\nPlease provide a response based on the above context and documents.'
        return prompt

# Example usage:
# handler = LLMHandler(api_key='YOUR_API_KEY')
# response = handler.generate_response('Some legal context...', ['Doc 1', 'Doc 2'])
# print(response)