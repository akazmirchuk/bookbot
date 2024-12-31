def main():

    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    file_text = file_contents
    word_count = count_words(file_contents)
    char_count = count_uchars(file_contents)
    report(word_count,char_count)
    #print(f"Word Count: {count_words(file_contents)}")
    #print(count_uchars(file_contents))

def count_words(text):
    words = len(text.split())
    
    return words

def count_uchars(text):
    
    formatted_text = text.lower()
    #chars = list(text)
        
    dict_chars = {}

    for c in formatted_text:
        if c not in dict_chars:
            dict_chars[c] = 1
        else:
            dict_chars[c] += 1
    
    return dict_chars

def report(word, char):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word} words found in the document\n\n")
    
    for ch,cnt in char.items():
        print(f"The {ch} character was found {cnt} times")
    
    print("--- End report ---")
    
main()

