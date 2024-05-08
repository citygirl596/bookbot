# TODO finish final report, need to output it so that the letter appearing most is at the top etc etc

alphabet = "abcdefghijklmnopqrstuvwxyz"


def main():
    file_content = read_bookfile()
    word_count = (count_words(file_content))
    response_dictionary = count_letters(file_content)
    final_report(word_count, response_dictionary)

def read_bookfile():
    with open("books/frankenstein.txt") as bookfile:
        bookfile = bookfile.read()
    return bookfile


def count_words(string_of_text):
    word_list = string_of_text.split()
    # print(word_list)
    return len(word_list)


def count_letters(string_of_text):
    final_dict = {}
    lower_case = string_of_text.lower()
    for letter in alphabet:
        dict_key = letter
        dict_value = lower_case.count(letter)
        # print(f"Dictionary key is {dict_key} and the value is {dict_value}")
        final_dict[dict_key] = dict_value
    # print(final_dict)
    return final_dict



def final_report(words_counted, stats_dictionary):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{words_counted} words found in the document\n")
    print("Unsorted dictionary")
    print(stats_dictionary)

    print("--- End report ---")

main()
