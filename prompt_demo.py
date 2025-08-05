import openai
import os
from dotenv import load_dotenv, find_dotenv

#Load the API key from the .env file
_= load_dotenv(find_dotenv())

#Initialize the OpenAI client
client = openai.OpenAI(
    base_url = 'http://localhost:11434/v1',
    api_key = 'ollama',
)

#Add helper function
def get_completion(prompt, model="llama3"):
    messages = [{"role": "user", "content": prompt}]
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0
    )
    return response.choices[0].message.content

#Example usage
prompt_text = "What is the capital of France?"
response = get_completion(prompt_text)
print(response)