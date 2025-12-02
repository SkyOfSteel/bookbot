# BookBot

BookBot is a small Python script to analyze the contents of a text file and report its total word count and individual character count. Characters are normalized into lower case for accuracy of the total count.

The word count is displayed as a single line in the format: `Found <X> total words`, printed to the console.

The character count is a sorted list of dictionaries in the format of `<character>: <count>`, with a separate line for each character.

# Usage

**`python3 main.py <file path>`**

The script uses sys.argv[1] as the input for a file path. An error message `Usage: python3 main.py <path_to_book>` is printed to the console on failure.

# Example

An input file with the text "Sphinx of black quartz, judge my vow" will produce the following result:

```
============ BOOKBOT ============
Analyzing book found at ./books/test.txt...  
----------- Word Count ----------  
Found 7 total words  
--------- Character Count -------  
o: 2  
a: 2  
u: 2  
s: 1  
p: 1  
h: 1  
i: 1  
n: 1  
x: 1  
f: 1  
b: 1  
l: 1  
c: 1  
k: 1  
q: 1  
r: 1  
t: 1  
z: 1  
j: 1  
d: 1  
g: 1  
e: 1  
m: 1  
y: 1  
v: 1  
w: 1  
============= END ===============
```

# Function Flow

1. *get_book_text* - read the text.
2. *count_words* - count the words.
3. *character_count* - count the characters and put them into a dictionary.
4. *formatting_function* and *sort_key* - format the dictionary into a list of mini-dictionaries for each character and sort.
5. *main* - format the final output.
