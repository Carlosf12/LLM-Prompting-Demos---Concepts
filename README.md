# LLM Prompting Demos & Concepts

This repository contains a collection of Python scripts to demonstrate key principles and tactics for effective prompt engineering with Large Language Models (LLMs). The project is set up to use the Ollama framework to run a local `llama3` model, providing a self-contained and easy-to-use environment for learning.

***

## Project Features

* **Prompting Guidelines Demos (`guidelines_demo.py`)**: A single script that showcases a variety of prompting techniques, which can be run by changing a `demo_tactic` variable. These tactics include:
    1.  **Using Delimiters**: Structuring prompts to clearly separate instructions from content.
    2.  **Structured Output**: Asking for responses in formats like JSON.
    3.  **Conditional Logic**: Guiding the model to perform actions based on conditions.
    4.  **Few-shot Prompting**: Providing examples to teach the model a desired style.
    5.  **Specifying Steps**: Breaking down complex tasks for the model.
    6.  **Working Out Solutions First**: Improving accuracy by having the model solve a problem before evaluating an answer.
    7.  **Generating Marketing Copy**: Creating a product description from a technical fact sheet and then refining the output with a word count constraint. This demo now includes enhanced terminal output using the **`rich`** library and saves a formatted HTML report.

* **Iterative Prompt Development (`iterative_prompts.py`)**: A dedicated script that demonstrates the process of iteratively refining a prompt to achieve a progressively better and more targeted output.

***

## Prerequisites

Before running this demo, you need to have the following installed:

* **Python 3:** The script is written in Python.
* **pip:** Python's package installer.
* **Ollama:** A framework to run LLMs locally. You can download it from [ollama.ai](https://ollama.ai/).
* **llama3 model:** Once Ollama is installed, open your terminal and pull the `llama3` model:
    ```bash
    ollama pull llama3
    ```

***

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
    (Note: You may need to create a `requirements.txt` file containing `openai`, `python-dotenv`, and **`rich`**).

3.  Create a `.env` file in the project directory with your OpenAI API key (or leave it blank, as the script is configured to use Ollama's local API).

***

## Usage

1.  Ensure the Ollama server is running and the `llama3` model is available.

2.  Open either **`guidelines_demo.py`** or `iterative_prompts.py` and modify the `demo_tactic` variable as needed to select the desired demo.

3.  Run the script from your terminal:
    ```bash
    python3 guidelines_demo.py
    ```
    or
    ```bash
    python3 iterative_prompts.py
    ```

The output in your terminal will show the results of the chosen prompting tactic. When running the `Generating Marketing Copy` demo, a file named `output.html` will also be created, which you can open in your browser to see a detailed, formatted report.