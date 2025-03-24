def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    print(text)

main()

def numwords(path):
    words = len(path.split())
    return words

def main():
    text = get_book_text(path)
    word_count = numwords(text)
    print(f"{word_count} words found in this document")
