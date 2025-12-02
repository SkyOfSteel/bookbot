def count_words(text):
    num_words = text.split()
    return len(num_words)

    # splits the text into individual words on blank spaces

def character_count(text):
    result = {}
    input_text_lower = text.lower()

    # lowers the letter register for convenience and accuracy

    for character in input_text_lower:
        if character not in result:
            result[character] = 1
        else:
            result[character] += 1
    return result

    # calculates the number of each character occurrence and
    # puts them in a dictionary: "{'a': 12414, 'b': 34324"}, etc.

def formatting_function(text):
    result = []
    
    for i in text:
        dictionary = {}
        dictionary["char"] = i
        dictionary["num"] = text[i]
        result.append(dictionary)

    result.sort(reverse=True, key=sort_key)

    # formats the dictionary with character counts into
    # a list of mini-dictionaries with individual characters
    # like "[{'char': 'a', 'num': 12414}, ...]" and so on, and then
    # sorts them from higher to lower count per sort_key

    return result

def sort_key(text):
    return text["num"]

    # sorting by the "num" key