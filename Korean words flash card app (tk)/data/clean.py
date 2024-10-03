""""for that I couldn't find a very wide list of korean to english words, so I tried the Google sheets method to translate a
wide variety of korean words that is widely used in everyday life (frequency wise) and then sadly couldn't download it as a csv format as
 the korean letters wasn't correctly displayed, so I copied everything as the nn.csv that is the only way it worked for me then
 so this code is for cleaning and formatting the csv into a usable form for the flash card project"""
import re

input_file = 'nn.csv'
output_file = 'output.csv'


# Function to remove numbers from a string
def remove_numbers(text):
    return re.sub(r'\d+', '', text).strip()


# Opening the input file and process it
with open(input_file, mode='r', encoding='utf-8') as infile, open(output_file, mode='w', encoding='utf-8',
                                                                  newline='') as outfile:
    for line in infile:
        # Split the line at the first comma
        parts = line.split(',', 1)
        if len(parts) == 2:
            korean = remove_numbers(parts[0])
            english = remove_numbers(parts[1])
            print(f"Processed Korean: '{korean}', English: '{english}'")
            outfile.write(f"{korean},{english}\n")
        else:
            print(f"Skipping line (unexpected format): {line.strip()}")
