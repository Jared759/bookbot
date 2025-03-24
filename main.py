from stats import numwords
from stats import numcharacters
from stats import sort
import sys

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
book_path = sys.argv[1]

with open(book_path, "r") as f:

text = get_book_text(book_path)
word_count = numwords(text)
letter_count = numcharacters(text)  # This should return the letter frequency dictionary
sorted_letters = sort(letter_count)
print("============ BOOKBOT ============")
print("Analyzing book found at books/frankenstein.txt...")
print("----------- Word Count ----------")
print(f"Found {word_count} total words")
print("--------- Character Count -------")
for item in sorted_letters:  # Loop through the sorted list
    print(f"{item['letter']}: {item['count']}")

main()


