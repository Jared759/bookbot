def numwords(path):
    words = len(path.split())
    return words

def numletters(path):
    dict = {}
    count = 0
    for i in path:
        count += 1
        dict =(f"{i}: {count}")
    return dict
