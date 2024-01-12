import csv
import re

# Open the CSV file
with open('dme.csv', 'r') as file:
    # Create a CSV reader
    csv_reader = csv.reader(file)
    
    # Skip the header row if it exists
    next(csv_reader, None)

    # Initialize a list to store the extracted URLs
    zip_urls = []

    # Iterate through the rows in the CSV file
    for row in csv_reader:
        # Extract URLs from the 'file' column using a regular expression
        urls = re.findall(r'https?://\S+\.zip', row[2])

        # Add the extracted URLs to the list
        zip_urls.extend(urls)

# Format the URLs as ./year/month/filename.zip and remove 'woocommerce_uploads'
formatted_urls = [f"./{url.split('/')[-3]}/{url.split('/')[-2]}/{url.split('/')[-1]}" if 'woocommerce_uploads' in url else f"./{url.split('/')[-2]}/{url.split('/')[-1]}" for url in zip_urls]

# Write the formatted URLs to a new text file
with open('output.txt', 'w') as output_file:
    for formatted_url in formatted_urls:
        output_file.write(formatted_url + '\n')
