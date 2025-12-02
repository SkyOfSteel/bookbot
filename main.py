import sys
from stats import count_words, character_count, formatting_function

# opens a book for analysis

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

# filepath is a parameter for main() to make sure that main() 
# does not depend on a global variable or a hardcoded path

def main(filepath):
    text = get_book_text(filepath)
    num_words = count_words(text) 
    
    # function from stats.py to split the text using blank spaces as separators
    
    word_dictionary = character_count(text) 
    
    # function from stats.py to generate a dictionary of lower-case characters
    
    formatted_text = formatting_function(word_dictionary) 
    
    # function from stats.py to split the dictionary from character_count 
    # into a list of dictionaries in the "character: count" format

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for entry in formatted_text:
        if entry["char"].isalpha():
            print(f'{entry["char"]}: {entry["num"]}')
    print("============= END ===============")

    # isalpha() method returns True for alpha-numeric characters,
    # allowing to ignore blank spaces in the final list,
    # then keys ("char") and values ("num") 
    # from formatting_function are printed on separate lines

if len(sys.argv) == 2:

# checking that sys.argv has exactly two arguments,
# so that the second input can be used as a file path

    filepath = sys.argv[1]
    main(filepath)
else:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)