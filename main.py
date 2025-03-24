from stats import numwords
from stats import numcharacters

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    word_count = numwords(text)
    letter_count = numletters(text)
    print(f"{word_count} words found in the document")
    return letter_count
main()


