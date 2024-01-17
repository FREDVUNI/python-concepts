
# Paths to the two files you want to compare and fix
file1_path = 'output.txt'
file2_path = 'products.txt'
output_file_path = 'unique_paths_in_output.json'

import json

# Read the content of both files
with open(file1_path, 'r', encoding='utf-8') as file1:
    output_content = file1.readlines()

with open(file2_path, 'r', encoding='utf-8') as file2:
    products_content = file2.readlines()

# Function to extract paths from a file
def extract_paths(lines):
    return {line.strip() for line in lines}

# Extract paths from output and products
output_paths = extract_paths(output_content)
products_paths = extract_paths(products_content)

# Find paths that are unique to the output
unique_paths_in_output = output_paths - products_paths

# Convert the set to a list and write it to a file
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    json.dump(list(unique_paths_in_output), output_file, indent=2)

# Print a message indicating the process is complete
print(f'Unique paths in output have been written to {output_file_path}')
