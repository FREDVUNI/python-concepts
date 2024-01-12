# Function to read file content and return a set of lines
def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return set(file.readlines())

# Function to write lines to a file
def write_file(file_path, lines):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(lines)

# Paths to the two files you want to compare
file1_path = 'dme-server.txt'
file2_path = 'dme-site.txt'

# Read the content of the two files
file1_content = read_file(file1_path)
file2_content = read_file(file2_path)

# Find lines that are present in one file but not in the other
unique_to_file1 = file1_content - file2_content
unique_to_file2 = file2_content - file1_content

# Write the unique lines to a new file
output_file_path = 'differences.txt'
write_file(output_file_path, list(unique_to_file1.union(unique_to_file2)))

print(f"Lines unique to {file1_path}:\n{unique_to_file1}")
print(f"\nLines unique to {file2_path}:\n{unique_to_file2}")
print(f"\nDifferences written to {output_file_path}")
