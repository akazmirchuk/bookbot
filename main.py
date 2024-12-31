def main():

    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    word_count = count_words(file_contents)
    char_count = count_uchars(file_contents)
    report(word_count,char_count)

def count_words(text):
    words = len(text.split())  
    return words

def count_uchars(text):
    
    formatted_text = text.lower()  
    dict_chars = {}

    for c in formatted_text:
        if c not in dict_chars:
            dict_chars[c] = 1
        else:
            dict_chars[c] += 1


    list_chars = list(dict_chars.items())
        
    list_chars.sort(reverse=True, key=lambda item: item[1])

    sorted_dict = dict(list_chars)

    return sorted_dict

def report(word, char):

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word} words found in the document\n\n")
    
    for ch,cnt in char.items():
        if ch.isalpha():
            print(f"The {ch} character was found {cnt} times")
    
    print("--- End report ---")
    
main()

