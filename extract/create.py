from difflib import get_close_matches

# Function to read file content and return a set of lines
def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return set(file.readlines())

# Function to find similar but different lines
def find_similar_but_different(lines, reference_lines, threshold=0.8):
    similar_lines = set()

    for line in lines:
        matches = get_close_matches(line, reference_lines, n=1, cutoff=threshold)
        if matches and line != matches[0]:
            similar_lines.add(line)

    return similar_lines

# Paths to the two files you want to compare
file1_path = 'output.txt'
file2_path = 'products.txt'

# Read the content of the two files
file1_content = [line.strip() for line in read_file(file1_path)]
file2_content = [line.strip() for line in read_file(file2_path)]

# Find lines that are similar but different
similar_but_different_lines = find_similar_but_different(file1_content, file2_content)

# Write the lines to the 'similar_but_different.txt' file
with open('similar_but_different.txt', 'w', encoding='utf-8') as file:
    file.write(f"{'='*10} Similar But Different {'='*10}\n")
    for line in similar_but_different_lines:
        file.write(f"{file1_path}: {line}\n")
        file.write(f"{file2_path}: {line}\n")
        file.write("-" * 30 + "\n")

# Print a message indicating the process is complete
print(f"Similar but different lines have been written to 'similar_but_different.txt'")
