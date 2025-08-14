LLM Prompting Demos & Concepts
This repository offers Python scripts to demonstrate effective prompt engineering with Large Language Models (LLMs). It leverages the Ollama framework to run a local llama3 model, providing a self-contained and easy-to-use environment for learning.

Project Features
The project includes three main demo scripts:

guidelines_demo.py:

Showcases various prompting techniques, including:

Using Delimiters for clear instruction separation.

Structured Output (e.g., JSON).

Conditional Logic.

Few-shot Prompting with examples.

Specifying Steps for complex tasks.

Working Out Solutions First for improved accuracy.

Generating Marketing Copy with word count constraints, enhanced by the rich library for terminal output and HTML reports.

iterative_prompts.py:

Demonstrates the iterative refinement process for achieving targeted LLM outputs.

transforming.py:

Highlights the LLM's text transformation capabilities, focusing on:

Multi-language Translation (simple, persona-based, formal/informal).

Language Identification.

Tone Transformation (e.g., slang to business).

Format Conversion (e.g., JSON to HTML table).

A "Universal Translator" loop for dynamic translation.

Setup
Prerequisites
You'll need:

Python 3 and pip.

Ollama installed locally.

The llama3 model pulled via Ollama:

ollama pull llama3

Installation
Clone the repository:

git clone <your-repo-url>
cd <your-repo-directory>

Install Python dependencies:

pip install -r requirements.txt

(Ensure requirements.txt includes openai, python-dotenv, and rich).

Create a .env file in the project directory for API keys (optional, as Ollama runs locally).

Usage
Ensure the Ollama server is running and the llama3 model is available.

Open either guidelines_demo.py, iterative_prompts.py, or transforming.py and modify variables or run directly.

Run the script from your terminal:

python3 guidelines_demo.py

or

python3 iterative_prompts.py

or

python3 transforming.py

Output will appear in your terminal. For the marketing copy demo, an output.html file will also be generated.