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
text = f"""
You should express what you want a model to do by \
providing instructions that are as clear and \
specific as you can possibly make them. \
This will guide the model towards the desired output, \
and reduce the chances of receiving irrelevant \
or incorrect responses. Don't confuse writing a \
clear prompt with writing a short prompt. \
In many cases, longer prompts provide more clarity \
and context for the model, which can lead to \
more detailed and relevant outputs.
"""
prompt = f"""
Summarize the text delimited by triple backticks \
into a single sentence.
```{text}```
"""
response = get_completion(prompt)
print(response)