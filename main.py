def main():

    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    print(file_contents)
    print(f"Word Count: {count_words(file_contents)}")
    print(count_uchars(file_contents))

def count_words(text):
    words = len(text.split())
    
    return words

def count_uchars(text):
    chars = list(text)
        
    return chars
    
    #print(chars)
    #uncounted_chars = words.split()


    #chars = {}




main()

