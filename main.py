def get_book_text(path):
    with open(path) as f:
        return f.read()


def count_words(text):
    return len(text.split())


def count_characters(text):
    text = text.lower()
    ch_dict = {}
    for ch in text:
        if ch in ch_dict:
            ch_dict[ch] += 1
        else:
            ch_dict[ch] = 1
    return ch_dict


def sort_on(dict):
    return dict["num"]


def format_ch_dict(ch_dict):
    ch_list = []
    for key in ch_dict:
        if key.isalpha():
            ch_list.append({"name": key, "num": ch_dict[key]})
    return ch_list


def main():
    book_path = './books/frankenstein.txt'
    text = get_book_text(book_path)

    #print(text)
    print(f"{count_words(text)}\n")
    #print(count_characters(text))

    ch_list = format_ch_dict(count_characters(text))
    ch_list.sort(reverse=True, key=sort_on)
    for ch in ch_list:
        print(f"The '{ch['name']}' character was found {ch['num']} times")


main()
