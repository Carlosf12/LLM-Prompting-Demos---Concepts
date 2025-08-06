import openai
import os
import json
from dotenv import load_dotenv, find_dotenv

# Load the API key from the .env file
_ = load_dotenv(find_dotenv())

# Initialize the OpenAI client, but point it to the local Ollama server
client = openai.OpenAI(
    base_url='http://localhost:11434/v1',
    api_key='ollama',  # This can be a dummy key as it's not used by Ollama
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
# 4 = Tactic 4 (Few-shot Prompting)
# 5 = Principle 2 - Tactic 1 (Specify steps)
# 6 = Principle 2 - Tactic 2 (Work out solution first)
demo_tactic = 7

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
    print("-" * 20)
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

elif demo_tactic == 5:
    print("--- Running Principle 2: Give the model time to 'think' ---")
    print("--- Tactic 1: Specify the steps required to complete a task ---")
    text = f"""
In a charming village, siblings Jack and Jill set out on \
a quest to fetch water from a hilltop \
well. As they climbed, singing joyfully, misfortune \
struck—Jack tripped on a stone and tumbled \
down the hill, with Jill following suit. \
Though slightly battered, the pair returned home to \
comforting embraces. Despite the mishap, \
their adventurous spirits remained undimmed, and they \
continued exploring with delight.
"""
    prompt_1 = f"""
Perform the following actions:
1 - Summarize the following text delimited by triple \
backticks with 1 sentence.
2 - Translate the summary into French.
3 - List each name in the French summary.
4 - Output a json object that contains the following \
keys: french_summary, num_names.
Separate your answers with line breaks.
Text:
```{text}```
"""
    response = get_completion(prompt_1)
    print("Completion for prompt 1:")
    print(response)
    print("\n" + "=" * 20 + "\n")
    prompt_2 = f"""
Your task is to perform the following actions:
1 - Summarize the following text delimited by
  <> with 1 sentence.
2 - Translate the summary into French.
3 - List each name in the French summary.
4 - Output a json object that contains the
  following keys: french_summary, num_names.
Use the following format:
Text: <text to summarize>
Summary: <summary>
Translation: <summary translation>
Names: <list of names in summary>
Output JSON: <json with summary and num_names>
Text: <{text}>
"""
    response = get_completion(prompt_2)
    print("Completion for prompt 2:")
    print(response)

elif demo_tactic == 6:
    print("--- Running Principle 2, Tactic 2: Work out solution first ---")
    prompt_1 = f"""
Determine if the student's solution is correct or not.

Question:
I'm building a solar power installation and I need help \
working out the financials.
- Land costs $100 / square foot
- I can buy solar panels for $250 / square foot
- I negotiated a contract for maintenance that will cost \
me a flat $100k per year, and an additional $10 / square \
foot
What is the total cost for the first year of operations \
as a function of the number of square feet.

Student's Solution:
Let x be the size of the installation in square feet.
Costs:
1. Land cost: 100x
2. Solar panel cost: 250x
3. Maintenance cost: 100,000 + 100x
Total cost: 100x + 250x + 100,000 + 100x = 450x + 100,000
"""
    response = get_completion(prompt_1)
    print("Completion for prompt 1:")
    print(response)

    print("\n" + "=" * 20 + "\n") # Separator for clarity

    prompt = f"""
Your task is to determine if the student's solution \
is correct or not.
To solve the problem do the following:
- First, work out your own solution to the problem including the final total. 
- Then compare your solution to the student's solution \ 
and evaluate if the student's solution is correct or not. 
Don't decide if the student's solution is correct until 
you have done the problem yourself.

Use the following format:
Question:
```
question here
```
Student's solution:
```
student's solution here
```
Actual solution:
```
steps to work out the solution and your solution here
```
Is the student's solution the same as actual solution \
just calculated:
```
yes or no
```
Student grade:
```
correct or incorrect
```

Question:
```
I'm building a solar power installation and I need help \
working out the financials. 
- Land costs $100 / square foot
- I can buy solar panels for $250 / square foot
- I negotiated a contract for maintenance that will cost \
me a flat $100k per year, and an additional $10 / square \
foot
What is the total cost for the first year of operations \
as a function of the number of square feet.
``` 
Student's solution:
```
Let x be the size of the installation in square feet.
Costs:
1. Land cost: 100x
2. Solar panel cost: 250x
3. Maintenance cost: 100,000 + 100x
Total cost: 100x + 250x + 100,000 + 100x = 450x + 100,000
```
Actual solution:
"""
    response = get_completion(prompt)
    print("Completion for prompt 2:")
    print(response)


elif demo_tactic == 7:
    print("--- Running Tactic 7: Generate Marketing Copy ---")
    
    fact_sheet_chair = """
OVERVIEW
- Part of a beautiful family of mid-century inspired office furniture, 
including filing cabinets, desks, bookcases, meeting tables, and more.
- Several options of shell color and base finishes.
- Available with plastic back and front upholstery (SWC-100) 
or full upholstery (SWC-110) in 10 fabric and 6 leather options.
- Base finish options are: stainless steel, matte black, 
gloss white, or chrome.
- Chair is available with or without armrests.
- Suitable for home or business settings.
- Qualified for contract use.

CONSTRUCTION
- 5-wheel plastic coated aluminum base.
- Pneumatic chair adjust for easy raise/lower action.

DIMENSIONS
- WIDTH 53 CM | 20.87”
- DEPTH 51 CM | 20.08”
- HEIGHT 80 CM | 31.50”
- SEAT HEIGHT 44 CM | 17.32”
- SEAT DEPTH 41 CM | 16.14”

OPTIONS
- Soft or hard-floor caster options.
- Two choices of seat foam densities: 
 medium (1.8 lb/ft3) or high (2.8 lb/ft3)
- Armless or 8 position PU armrests 

MATERIALS
SHELL BASE GLIDER
- Cast Aluminum with modified nylon PA6/PA66 coating.
- Shell thickness: 10 mm.
SEAT
- HD36 foam

COUNTRY OF ORIGIN
- Italy
"""
    
    # --- Prompt without length constraint (for comparison) ---
    prompt_unconstrained = f"""
Your task is to help a marketing team create a 
description for a retail website of a product based 
on a technical fact sheet.

Write a product description based on the information 
provided in the technical specifications delimited by 
triple backticks.

Technical specifications: ```{fact_sheet_chair}```
"""
    print("--- Original Prompt Output (no word limit) ---")
    response_unconstrained = get_completion(prompt_unconstrained)
    print(response_unconstrained)
    print(f"\nWord count: {len(response_unconstrained.split())}")
    print("="*50)
    
    # --- Prompt with length constraint (your new step) ---
    prompt_constrained = f"""
Your task is to help a marketing team create a 
description for a retail website of a product based 
on a technical fact sheet.
​
Write a product description based on the information 
provided in the technical specifications delimited by 
triple backticks.
​
Use at most 50 words.
​
Technical specifications: ```{fact_sheet_chair}```
"""
    print("--- Refined Prompt Output (50-word limit) ---")
    response_constrained = get_completion(prompt_constrained)
    print(response_constrained)
    print(f"\nWord count: {len(response_constrained.split())}")