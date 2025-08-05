import openai
import os
import json # You'll need this to handle the JSON output
from dotenv import load_dotenv, find_dotenv

# Load the API key from the .env file
_ = load_dotenv(find_dotenv())

# Initialize the OpenAI client, but point it to the local Ollama server
client = openai.OpenAI(
    base_url = 'http://localhost:11434/v1',
    api_key = 'ollama', # This can be a dummy key as it's not used by Ollama
)

# Define the helper function
def get_completion(prompt, model="llama3"):
    messages = [{"role": "user", "content": prompt}]
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0
    )
    return response.choices[0].message.content

# --- Demo Setup: Choose which tactic to run ---
# Change this number to run a different demo tactic.
# 1 = Tactic 1 (Delimiters)
# 2 = Tactic 2 (Structured Output)
# 3 = Tactic 3 (Conditional Logic)
demo_tactic = 4

# --- Prompting Principles Demos ---

if demo_tactic == 1:
    print("--- Running Tactic 1: Use delimiters ---")
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

elif demo_tactic == 2:
    print("--- Running Tactic 2: Ask for a structured output ---")
    prompt = f"""
Generate a list of three made-up book titles along \
with their authors and genres.
Provide them in JSON format with the following keys:
book_id, title, author, genre.
"""
    response = get_completion(prompt)
    print(response)

    # You can also parse the JSON to prove it's valid
    try:
        data = json.loads(response)
        print("\nSuccessfully parsed JSON output:")
        print(data)
    except json.JSONDecodeError:
        print("\nFailed to parse JSON output.")
        
elif demo_tactic == 3:
    print("--- Running Tactic 3: Conditional Logic ---")
    
    text_1 = f"""
Making a cup of tea is easy! First, you need to get some \
water boiling. While that's happening, \
grab a cup and put a tea bag in it. Once the water is \
hot enough, just pour it over the tea bag. \
Let it sit for a bit so the tea can steep. After a \
few minutes, take out the tea bag. If you \
like, you can add some sugar or milk to taste. \
And that's it! You've got yourself a delicious \
cup of tea to enjoy.
"""
    prompt = f"""
You will be provided with text delimited by triple quotes.
If it contains a sequence of instructions, \
re-write those instructions in the following format:

Step 1 - ...
Step 2 - …
…
Step N - …

If the text does not contain a sequence of instructions, \
then simply write "No steps provided."

\"\"\"{text_1}\"\"\"
"""
    response = get_completion(prompt)
    print("Completion for Text 1:")
    print(response)

    print("-" * 20) # Separator for clarity

    text_2 = f"""
The sun is shining brightly today, and the birds are \
singing. It's a beautiful day to go for a \
walk in the park. The flowers are blooming, and the \
trees are swaying gently in the breeze. People \
are out and about, enjoying the lovely weather. \
Some are having picnics, while others are playing \
games or simply relaxing on the grass. It's a \
perfect day to spend time outdoors and appreciate the \
beauty of nature.
"""
    prompt = f"""
You will be provided with text delimited by triple quotes.
If it contains a sequence of instructions, \
re-write those instructions in the following format:

Step 1 - ...
Step 2 - …
…
Step N - …

If the text does not contain a sequence of instructions, \
then simply write "No steps provided."

\"\"\"{text_2}\"\"\"
"""
    response = get_completion(prompt)
    print("Completion for Text 2:")
    print(response)
elif demo_tactic == 4:
    print("--- Running Tactic 4: Few-shot Prompting ---")
    
    prompt = f"""
Your task is to answer in a consistent style.

<child>: Teach me about patience.

<grandparent>: The river that carves the deepest \
valley flows from a modest spring; the \
grandest symphony originates from a single note; \
the most intricate tapestry begins with a solitary thread.

<child>: Teach me about resilience.
"""
    response = get_completion(prompt)
    print(response)