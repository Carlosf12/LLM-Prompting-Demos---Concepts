import openai
import os
from dotenv import load_dotenv, find_dotenv
from rich.console import Console
from rich.panel import Panel

# Load the API key from the .env file
_ = load_dotenv(find_dotenv())

# Initialize the rich console for formatted output
console = Console()

# Initialize the OpenAI client, but point it to the local Ollama server
client = openai.OpenAI(
    base_url='http://localhost:11434/v1',
    api_key='ollama',  # This can be a dummy key as it's not used by Ollama
)

# Define the helper function to get a completion from the LLM
def get_completion(prompt, model="llama3"):
    """
    Sends a prompt to the specified model and returns the text response.
    """
    messages = [{"role": "user", "content": prompt}]
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0
    )
    return response.choices[0].message.content

# Helper function to display the prompt and response in a formatted panel
def display_output(title, prompt, response):
    """
    Displays the title, prompt, and response using rich panels for clarity.
    """
    console.print(
        Panel(
            f"[bold green]PROMPT:[/bold green]\n{prompt}\n\n[bold blue]RESPONSE:[/bold blue]\n{response}",
            title=f"[bold yellow]{title}[/bold yellow]",
            expand=False,
            border_style="cyan"
        )
    )

# --- Translation Examples ------------------------------------

# Prompt 1: Simple English to Spanish translation
prompt_1 = f"""
Translate the following English text to Spanish: \ 
```Hi, I would like to order a blender```
"""
response_1 = get_completion(prompt_1)
display_output("Translation: English to Spanish", prompt_1, response_1)

# ---

# Prompt 2: Multiple language translation with a persona
prompt_2 = f"""
Translate the following text to French and Spanish
and English pirate: \
```I want to order a basketball```
"""
response_2 = get_completion(prompt_2)
display_output("Translation: Multiple Languages & Persona", prompt_2, response_2)

# ---

# Prompt 3: Formal and informal translation
prompt_3 = f"""
Translate the following text to Spanish in both the \
formal and informal forms: 
'Would you like to order a pillow?'
"""
response_3 = get_completion(prompt_3)
display_output("Translation: Formal vs. Informal Spanish", prompt_3, response_3)

# ---

# Prompt 4: Language identification
prompt_4 = f"""
Tell me which language this is: 
```Combien coûte le lampadaire?```
"""
response_4 = get_completion(prompt_4)
display_output("Language Identification", prompt_4, response_4)

# --- Tone Transformation ------------------------------------

prompt_5 = f"""
Translate the following from slang to a business letter: 
'Dude, This is Joe, check out this spec on this standing lamp.'
"""
response_5 = get_completion(prompt_5)
display_output("Tone Transformation", prompt_5, response_5)

# --- Format Conversion ------------------------------------

data_json = { "resturant employees" :[ 
    {"name":"Shyam", "email":"shyamjaiswal@gmail.com"},
    {"name":"Bob", "email":"bob32@gmail.com"},
    {"name":"Jai", "email":"jai87@gmail.com"}
]}

prompt_6 = f"""
Translate the following python dictionary from JSON to an HTML \
table with column headers and title: {data_json}
"""
response_6 = get_completion(prompt_6)
display_output("Format Conversion", prompt_6, response_6)


# --- Universal Translator ------------------------------------

console.rule("[bold magenta]Universal Translator[/bold magenta]")

user_messages = [
  "La performance du système est plus lente que d'habitude.",
  "Mi monitor tiene píxeles que no se iluminan.",
  "Il mio mouse non funziona",
  "Mój klawisz Ctrl jest zepsuty",
  "我的屏幕在闪烁"
] 

for issue in user_messages:
    # First, identify the language of the message
    prompt_lang = f"Tell me what language this is: ```{issue}```"
    lang = get_completion(prompt_lang)

    # Then, translate the message
    prompt_trans = f"""
    Translate the following text to English \
    and Korean: ```{issue}```
    """
    response_trans = get_completion(prompt_trans)

    # Display the original message and the translation
    console.print(
        Panel(
            f"[bold red]Original Message ({lang}):[/bold red] {issue}\n\n"
            f"[bold blue]Translation:[/bold blue]\n{response_trans}",
            title=f"[bold yellow]Message Analysis[/bold yellow]",
            expand=False,
            border_style="green"
        )
    )
