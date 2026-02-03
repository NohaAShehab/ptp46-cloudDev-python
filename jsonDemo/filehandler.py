


"""

[{},{}]  or {}
"""
# 1- get all books from file books.json
import json
def get_all_books():
    books = []
    try:
        with open('books.json') as file_object:
            books=json.load(file_object) # read content from json to suitable python data

    except Exception as e:
        print(e)

    return books


### to save new book
def save_new_book(book_info):
    all_books = get_all_books()
    all_books.append(book_info)
    try:
        with open('books.json', 'w') as file_object:
            # convert the list of dicts  --> serialization to a string
            # books_string= json.dumps(all_books)
            # file_object.write(books_string)
            ###
            json.dump(all_books, file_object, indent=4)
        return True
    except Exception as e:
        print(e)
        return False
