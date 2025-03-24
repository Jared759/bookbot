from stats import numwords
from stats import numcharacters
from stats import sort

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    word_count = numwords(text)
    letter_count = numcharacters(text)  # This should return the letter frequency dictionary
    sorted_letters = sort(letter_count)
    print(f"Found {word_count} total words.")
    print(sorted_letters)
main()


