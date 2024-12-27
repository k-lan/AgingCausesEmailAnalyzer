# Aging Causes Analysis

## Overview

This program is an automated email analysis tool that processes email threads to identify and extract information about various causes of aging. It leverages OpenAI's GPT model to intelligently analyze email content, identifying key discussions about aging factors, and compiles this information into a structured format. The program helps researchers and professionals easily track and categorize different aging mechanisms discussed in email communications.

## Requirements

- Python 3.8+
- OpenAI API key

## Installation and Setup

1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd <repository-name>
   ```

2. Set up a virtual environment:
   ```bash
   # Create a virtual environment
   python -m venv venv

   # Activate the virtual environment
   # On macOS/Linux:
   source venv/bin/activate
   # On Windows:
   .\venv\Scripts\activate
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root with your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

## Usage

1. Place your email thread files in the `Data` directory:
   - `Data/Email Thread #1.txt`
   - `Data/Email Thread #2.txt`

2. Ensure your virtual environment is activated, then run the analysis script:
   ```bash
   python aging.py
   ```

3. The results will be saved in `causesofaging.md` in a table format with the following columns:
   - Email Subject Label
   - Author
   - Email Date/Time
   - Cause of Aging #
   - Brief Causes of Aging Description

## Output Format

The output markdown table will look like this:

| Email Subject Label | Author | Email Date/Time | Cause of Aging # | Brief Causes of Aging Description |
|-------------------|---------|-----------------|-----------------|-----------------------------------|
| Subject | author@email.com | 2023-12-01 10:00 AM | 1 | Description of the cause |

## Note

This project uses the OpenAI GPT model to analyze the content. Make sure you have sufficient API credits and a valid API key.

## Deactivating the Virtual Environment

When you're done working on the project, you can deactivate the virtual environment:
```bash
deactivate
``` 