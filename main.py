# TODO finish final report, need to output it so that the letter appearing most is at the top etc etc

alphabet = "abcdefghijklmnopqrstuvwxyz"


def main():
    file_content = read_bookfile()
    word_count = (count_words(file_content))
    response_dictionary = count_letters(file_content)
    sorted_list = sort_the_dictionary(response_dictionary)
    final_report(word_count, sorted_list)

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


def sort_the_dictionary(unsorted_dict):
    tmp = []
    for key, value in unsorted_dict.items():
        tmptuple = (value, key)
        tmp.append(tmptuple)
    # Sort the list in ascending order
    tmp = sorted(tmp, reverse=True)
    # print("This is the sorted list")
    # print(tmp)
    return tmp


def final_report(words_counted, stats_list):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{words_counted} words found in the document\n")
    for entry in stats_list:
        print(f"The {entry[1]} character was found {entry[0]} times")
    print("--- End report ---")

main()
