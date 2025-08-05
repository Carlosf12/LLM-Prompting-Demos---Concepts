# LLM Prompting Principles Demo

This repository contains a simple Python script to demonstrate key principles and tactics for effective prompt engineering with Large Language Models (LLMs). The script uses the Ollama framework to run a local `llama3` model.

## Prerequisites

Before running this demo, you need to have the following installed:

* **Python 3:** The script is written in Python.
* **pip:** Python's package installer.
* **Ollama:** A framework to run LLMs locally. You can download it from [ollama.ai](https://ollama.ai/).
* **llama3 model:** Once Ollama is installed, open your terminal and pull the `llama3` model:
    ```bash
    ollama pull llama3
    ```

## Installation

1.  Clone this repository:
    ```bash
    git clone <your-repo-url>
    cd <your-repo-directory>
    ```

2.  Install the required Python libraries:
    ```bash
    pip install -r requirements.txt
    ```
    (Note: You may need to create a `requirements.txt` file containing `openai` and `python-dotenv`).

3.  Create a `.env` file in the project directory with your OpenAI API key (or leave it blank, as the script is configured to use Ollama's local API).

## Usage

1.  Ensure the Ollama server is running and the `llama3` model is available.

2.  Open the `prompt_demo.py` file and find the `demo_tactic` variable at the top.

3.  Set the `demo_tactic` variable to the number of the tactic you want to run (e.g., `demo_tactic = 6`).

4.  Run the script from your terminal:
    ```bash
    python3 prompt_demo.py
    ```

The output in your terminal will show the results of the chosen prompting tactic.