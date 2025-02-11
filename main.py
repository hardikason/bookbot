def main():

    path_to_file = 'books/frankenstein.txt'
    file_contents = read_file(path_to_file)

    print("--- Begin report of books/frankenstein.txt ---")

    word_count = get_word_count(file_contents)
    print(f"{word_count} words found in the document")


    character_dict = count_characters(file_contents)

    sort_charater_dictionary(character_dict)

    print("--- End report ---")


def read_file(path_to_file):
    with open(path_to_file) as f:
        return f.read();


def get_word_count(file_contents):
    word_count = len(file_contents.split());
    return word_count;


def count_characters(file_contents):
    lower_string = file_contents.lower()
    character_dict = {}
    
    for character in lower_string:
        if character in character_dict :
            character_dict[character] = character_dict[character] + 1
        else:
            character_dict[character] = 1

    return character_dict;


def sort_charater_dictionary(character_dict):

    sorted_data = sorted(character_dict.items(), key=lambda item:item[1], reverse=True);
        
    sorted_dict = dict(sorted_data);

    for character in sorted_dict:
        if character.isalpha():
            print(f"The '{character}' character was found {sorted_dict[character]} times")

    

main()