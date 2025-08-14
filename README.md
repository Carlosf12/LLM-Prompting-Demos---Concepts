LLM Prompting Demos & Concepts
This repository offers Python scripts to demonstrate effective prompt engineering with Large Language Models (LLMs), utilizing Ollama and the local llama3 model for a self-contained learning environment.

Features
The project includes three main demo scripts:

guidelines_demo.py: Showcases various prompting techniques like using delimiters, structured output (JSON), conditional logic, few-shot prompting, and specifying steps. It also features a marketing copy generation demo with rich terminal output and HTML reports.

iterative_prompts.py: Focuses on refining prompts through an iterative development process.

transforming.py: Demonstrates text transformations including multi-language translation (simple, persona-based, formal/informal), language identification, tone transformation (slang to business), and JSON to HTML table conversion. It also includes a "Universal Translator" loop.

Setup
Prerequisites
You'll need:

Python 3 and pip.

Ollama installed locally.

The llama3 model pulled via Ollama: ollama pull llama3

Installation
Clone the repository.

Install Python dependencies: pip install -r requirements.txt (ensure requirements.txt includes openai, python-dotenv, and rich).

Create a .env file for API keys (optional, as Ollama runs locally).

Usage
Ensure Ollama server is running and llama3 is available.

Run desired script from your terminal:

python3 guidelines_demo.py

python3 iterative_prompts.py

python3 transforming.py

Output will appear in the terminal, and output.html will be generated for the marketing copy demo.