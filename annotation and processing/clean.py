import os
import re

folder_path = '/Users/lauravargas/Desktop/Digital Humanities/ProjectDH/Selected/spa'  

for root, _, files in os.walk(folder_path):
    for file_name in files:
        if file_name.endswith('annotated.xml'):
            file_path = os.path.join(root, file_name)
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # Eliminate tags <w> with pos="PUNCT" or pos="SPACE"
            modified_content = re.sub(r'<w\s+[^>]*pos="(?:PUNCT|SPACE)"[^>]*>.*?</w>', '', content, flags=re.DOTALL)

        
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(modified_content)
