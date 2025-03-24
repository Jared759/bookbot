def numwords(path):
    words = len(path.split())
    return words

def numcharacters(path):
    dict = {}
    count = 0
    for i in path:
        letter = i.lower()
        if i in dict:
            dict[letter] += 1
        else:
            dict[letter] = 1
    return dict
