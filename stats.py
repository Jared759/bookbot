def numwords(path):
    words = len(path.split())
    return words

def numcharacters(path):
    dict = {}
    for i in path:
        letter = i.lower()
        if letter in dict:  # Check if the lowercase letter is in dict, not i
            dict[letter] += 1
        else:
            dict[letter] = 1
    return dict
