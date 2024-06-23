import os
import re

# Define the directory containing the files
directory = os.path.join(os.getcwd(), "html")

# Function to wrap text in <p> tags
def wrap_in_p_tags(text):
    # Split the text into paragraphs based on double newlines or newlines
    paragraphs = re.split(r'\n\s*\n', text)
    wrapped_paragraphs = [f"<p>{paragraph.strip()}</p>" for paragraph in paragraphs if paragraph.strip()]
    return "\n\n".join(wrapped_paragraphs)

# Iterate over all files in the directory
for filename in os.listdir(directory):
    if filename.endswith(".html"):
        filepath = os.path.join(directory, filename)
        
        # Read the content of the file
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Wrap the content in <p> tags
        wrapped_content = wrap_in_p_tags(content)
        
        # Write the modified content back to the file
        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(wrapped_content)

print("All files have been processed and text wrapped in <p> tags.")
