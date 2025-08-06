import openai
import os
from dotenv import load_dotenv, find_dotenv

#Load the API Key from the .env file
_ = load_dotenv(find_dotenv())

#Initialize the OpenAI Client, but to local Ollama Server
client = openai.OpenAI(
    base_url='http://localhost:11434/v1',
    api_key='ollama'
)

#Define the helper function
def get_completion(prompt, model="llama3"):
    messages = [{"role": "user", "content": prompt}]
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0
    )
    return response.choices[0].message.content

# Product Fact Sheet (for our example)
product_fact_sheet = """
PRODUCT NAME: Wireless Noise-Cancelling Headphones (Model: SoundSphere)

FEATURES:
- Active Noise Cancellation (ANC) with 3 modes (Travel, Office, Ambient)
- Battery life: Up to 40 hours on a single charge (with ANC off)
- Quick-charging: 10-minute charge provides 5 hours of playback
- Bluetooth 5.2 connectivity
- Comfort-fit earcups with breathable memory foam
- Built-in microphone for hands-free calls
- Sound quality: 40mm drivers for rich bass and clear highs
- Weight: 250 grams
- Color options: Midnight Black, Cloud White, Ocean Blue
"""

print("--- Iterative Prompt Development Demo ---")
print("Fact Sheet:")
print(product_fact_sheet)
print("="*50)

# --- ITERATION 1: Simple Request ---
print("--- Prompt 1: Simple product description ---")
prompt_1 = f"""
Write a product description for the SoundSphere headphones based on the fact sheet.
Fact Sheet: {product_fact_sheet}
"""
response_1 = get_completion(prompt_1)
print(response_1)
print("="*50)

# --- ITERATION 2: Add more details and a clear instruction ---
print("--- Prompt 2: Refined request with specific features to highlight ---")
prompt_2 = f"""
Write a marketing blurb for the SoundSphere headphones.
Focus on the Active Noise Cancellation, battery life, and comfortable earcups.
Fact Sheet: {product_fact_sheet}
"""
response_2 = get_completion(prompt_2)
print(response_2)
print("="*50)

# --- ITERATION 3: Add a target audience and tone ---
print("--- Prompt 3: Targeting a specific audience with a specific tone ---")
prompt_3 = f"""
Create a short, catchy marketing description for the SoundSphere headphones.
The tone should be friendly and energetic, targeting music lovers and students.
Highlight the long battery life and excellent sound quality.
Fact Sheet: {product_fact_sheet}
"""
response_3 = get_completion(prompt_3)
print(response_3)
print("="*50)

# --- ITERATION 4: Ask for a specific format and length ---
print("--- Prompt 4: Refining the output with specific constraints ---")
prompt_4 = f"""
Generate a product summary for the SoundSphere headphones.
- Limit the summary to a maximum of 30 words.
- Highlight the Active Noise Cancellation and the quick-charging feature.
- Output the summary as a single sentence.
Fact Sheet: {product_fact_sheet}
"""
response_4 = get_completion(prompt_4)
print(response_4)
print("="*50)

print("\n\nEnd of Demo.")    