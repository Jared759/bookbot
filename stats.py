def numwords(path):
    words = len(path.split())
    return words

#def numcharacters(path):
    #dict = {}
    #for i in path:
        #letter = i.lower()
        #if letter in dict:  # Check if the lowercase letter is in dict, not i
            #dict[letter] += 1
        #else:
            #dict[letter] = 1
    #return dict

def letter_count(dict):
    char_list = []

    for l, count in dict.items():

        char_dict = {"letter": l, "count": count}

        char_list.append(char_dict)

        char_list.sort(key=lambda x: x["count"], reverse=True)

    return char_list

def numcharacters(text):
    char_counts = {}
    
    for char in text.lower():  # Convert text to lowercase for case-insensitivity
        if char.isalpha():  # Only count alphabetical characters
            char_counts[char] = char_counts.get(char, 0) + 1  # Increment count

    return char_counts
