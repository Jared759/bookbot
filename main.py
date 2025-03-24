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
    
    book_path = sys.argv[1]  # Define book_path inside main() after checking args
    
    text = get_book_text(book_path)
    word_count = numwords(text)
    letter_count = numcharacters(text)
    sorted_letters = sort(letter_count)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")  # Use book_path here
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in sorted_letters:
        print(f"{item['letter']}: {item['count']}")

main()


