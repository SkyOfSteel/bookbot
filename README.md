# BookBot

BookBot is a small Python script to analyze the contents of a text file and report its total word count and individual character count. Characters are normalized into lower case for accuracy of the total count.

The word count is displayed as a single line in the format: `Found <X> total words`, printed to the console.

The character count is a sorted list of dictionaries in the format of `<character>: <count>`, with a separate line for each character.

# Usage

**`python3 main.py <file path>`**

The script uses sys.argv[1] as the input for a file path. An error message `Usage: python3 main.py <path_to_book>` is printed to the console on failure.

# Function Flow

1. *get_book_text* - read the text.
2. *count_words* - count the words.
3. *character_count* - count the characters and put them into a dictionary.
4. *formatting_function* and *sort_key* - format the dictionary into a list of mini-dictionaries for each character and sort.
5. *main* - format the final output.