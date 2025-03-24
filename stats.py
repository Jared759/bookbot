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

def sort(char_dict):
    char_list = []
    
    for char, count in char_dict.items():
        char_list.append({"letter": char, "count": count})  # Convert to list of dictionaries

    # Sort in descending order by "count"
    char_list.sort(key=lambda x: x["count"], reverse=True)
    return char_list

def numcharacters(text):
    char_counts = {}
    
    for char in text.lower():  # Convert text to lowercase for case-insensitivity
        if char.isalpha():  # Only count alphabetical characters
            char_counts[char] = char_counts.get(char, 0) + 1  # Increment count

    return char_counts

