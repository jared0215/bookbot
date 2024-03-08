import string

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_letters = count_letters(text)
    report = convert_to_list(num_letters)
    report.sort(reverse=True, key=sort_on)

    print("--- Begin report of {} ---".format(book_path))
    print("{} words found in the document\n".format(num_words))
    for item in report:
        print("The '{}' character was found {} times".format(item['name'], item['num']))
    print("--- End report ---")


def sort_on(report):
    return report["num"]

def convert_to_list(num_letters):
    report_list = []
    for key, value in num_letters.items():
        new_dict = {}
        new_dict['name'] = key
        new_dict['num'] = value
        report_list.append(new_dict)
    return report_list

    
def count_letters(text):
    d = dict.fromkeys(string.ascii_lowercase, 0)
    lowered_text = text.lower()
    for letter in lowered_text:
        if letter.isalpha():
            d[letter] = d[letter] + 1
    return d

def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()