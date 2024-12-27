import os
import json
from typing import List, Dict
import openai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = openai.OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def read_email_thread(file_path: str) -> str:
    """
    Read the content of an email thread file.
    
    Args:
        file_path (str): Path to the email thread file
        
    Returns:
        str: Content of the file
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except Exception as e:
        print(f"Error reading file {file_path}: {str(e)}")
        return ""

def analyze_aging_causes(content: str) -> List[Dict]:
    """
    Analyze email content using GPT-4o-mini to extract aging causes.
    
    Args:
        content (str): Email thread content
        
    Returns:
        List[Dict]: List of dictionaries containing extracted information
    """
    prompt = """
    Analyze the following email thread and extract information about causes of aging.
    For each mention of a cause of aging, provide:
    1. Email Subject Label
    2. Author (email address)
    3. Email Date/Time
    4. Cause of Aging number (for each author)
    5. Brief description of the cause (1-2 sentences)
    
    Format the response STRICTLY as a JSON array of objects with these exact fields:
    [
        {
            "subject": "Email Subject",
            "author": "author@email.com",
            "datetime": "YYYY-MM-DD HH:MM AM/PM",
            "cause_number": "1",
            "description": "Description of the cause"
        }
    ]
    
    Email thread content:
    """
    
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",  # Note: Replace with gpt-4o-mini when available
            messages=[
                {"role": "system", "content": "You are a helpful assistant that analyzes email threads about aging research. Always respond with valid JSON arrays containing the required fields."},
                {"role": "user", "content": prompt + content}
            ],
            temperature=0.3,
            max_tokens=10000
        )
        
        response_content = response.choices[0].message.content.strip()
        print("Raw OpenAI Response:")
        print(response_content)
        
        # Try to find JSON content if it's wrapped in other text
        try:
            # Look for content between square brackets
            start_idx = response_content.find('[')
            end_idx = response_content.rfind(']') + 1
            if start_idx != -1 and end_idx != 0:
                json_content = response_content[start_idx:end_idx]
            else:
                json_content = response_content
                
            # Parse the response and convert to list of dictionaries
            results = json.loads(json_content)
            
            # Validate the structure of each result
            validated_results = []
            required_fields = {'subject', 'author', 'datetime', 'cause_number', 'description'}
            
            for result in results:
                if isinstance(result, dict) and all(field in result for field in required_fields):
                    validated_results.append(result)
                else:
                    print(f"Skipping invalid result: {result}")
            
            return validated_results
            
        except json.JSONDecodeError as je:
            print(f"Error decoding JSON: {str(je)}")
            print("Invalid JSON content:", json_content)
            return []
            
    except Exception as e:
        print(f"Error in API call or processing: {str(e)}")
        return []

def create_markdown_table(results: List[Dict], output_file: str):
    """
    Create a markdown table from the analysis results.
    
    Args:
        results (List[Dict]): Analysis results
        output_file (str): Path to output markdown file
    """
    # Create markdown table header
    markdown_table = "| Email Subject Label | Author | Email Date/Time | Cause of Aging # | Brief Causes of Aging Description |\n"
    markdown_table += "|-------------------|---------|-----------------|-----------------|-----------------------------------|\n"
    
    # Add each result as a row in the table
    for result in results:
        markdown_table += f"| {result.get('subject', '')} | {result.get('author', '')} | {result.get('datetime', '')} | {result.get('cause_number', '')} | {result.get('description', '')} |\n"
    
    # Write to file
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(markdown_table)
    except Exception as e:
        print(f"Error writing markdown file: {str(e)}")

def main():
    """
    Main function to process email threads and generate aging causes analysis.
    """
    # File paths
    email_files = [
        "Data/Email Thread #1.txt",
        "Data/Email Thread #2.txt"
    ]
    output_file = "causesofaging.md"
    
    all_results = []
    
    # Process each email thread
    for file_path in email_files:
        content = read_email_thread(file_path)
        if content:
            results = analyze_aging_causes(content)
            all_results.extend(results)

    print(all_results)
    # Create markdown table
    if all_results:
        create_markdown_table(all_results, output_file)
        print(f"Analysis complete. Results written to {output_file}")
    else:
        print("No results were generated from the analysis.")

if __name__ == "__main__":
    main()
