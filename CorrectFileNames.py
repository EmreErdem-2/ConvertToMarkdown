import os
import re
import sys
# Dictionary to map Turkish characters to Latin characters
turkish_to_latin = {
    'ş': 's',
    'Ş': 'S',
    'ç': 'c',
    'Ç': 'C',
    'ı': 'i',
    'İ': 'I',
    'ğ': 'g',
    'Ğ': 'G',
    'ö': 'o',
    'Ö': 'O',
    'ü': 'u',
    'Ü': 'U'
}

# Function to replace Turkish characters with Latin characters
def replace_turkish_characters(text):
    for turkish_char, latin_char in turkish_to_latin.items():
        text = text.replace(turkish_char, latin_char)
    return text

# Function to convert to PascalCase
def to_pascal_case(text):
    return ''.join(capitalize_first(word) for word in text.split())

# Only capitalizes first letter but don't change the rest
def capitalize_first(word):
    return word[:1].upper() + word[1:]

# Function to clean file names
def cleanFileNames(directory):
    for filename in os.listdir(directory):
        # Split the filename into name and extension
        name, ext = os.path.splitext(filename)
        # Replace Turkish characters
        cleaned_name = replace_turkish_characters(name)
        # Convert to PascalCase
        cleaned_name = to_pascal_case(cleaned_name)
        # Replace non-letter characters with spaces
        cleaned_name = re.sub(r'[^a-zA-Z]', ' ', cleaned_name)
        # Convert to PascalCase. Bc there remains spaces after cleaning notations
        cleaned_name = to_pascal_case(cleaned_name)
        # Combine cleaned name with extension
        cleaned_filename = cleaned_name + ext
        # Rename the file
        original_path = os.path.join(directory, filename)
        cleaned_path = os.path.join(directory, cleaned_filename)
        os.rename(original_path, cleaned_path)
        print(f'Renamed: {filename} -> {cleaned_filename}')

# Specify the directory containing the files
directory = r'C:\Users\eerde\Desktop\TargetNotebookFolder'

if len(sys.argv) >= 2 : directory = sys.argv[1]

if __name__ == "__main__":
    # Clean the file names
    cleanFileNames(directory) 
