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
        
    dict_chars = {}

    for c in chars:
        if c not in dict_chars:
            dict_chars["character"] = c
            dict_chars["count"] = 1
        else:
            dict_chars[c] += 1
    
    return dict_chars
    
main()

