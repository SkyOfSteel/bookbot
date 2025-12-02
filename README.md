# BookBot

BookBot is a small Python script to analyze the contents of a text file and report its total word count and individual character count. Characters are normalized into lower case for accuracy of the total count.

The word count is displayed as a single line in the format: "Found <X> total words", printed to the console.

The character count is a sorted list of dictionaries in the format of "<character>: <count>", with a separate line for each character.

# Usage

**python3 main.py <file path>**

The script uses sys.argv[1] as the input for a file path. An error message "Usage: python3 main.py <path_to_book>" is printed to the console on failure.

# Function Flow

1. Read the text - *get_book_text*.
2. Count the words - *count_words*.
3. Count the characters and put them into a dictionary - *character_count*.
4. Format the dictionary into a list of mini-dictionaries for each character and sort - *formatting_function* and *sort_key*.
5. Format the final output - *main*.