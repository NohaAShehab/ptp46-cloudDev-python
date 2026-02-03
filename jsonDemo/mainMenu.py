
from filehandler import get_all_books, save_new_book
def create_book():
    id = input('Enter book id: ')
    name = input('Enter book name: ')
    price = input('Enter book price: ')

    book = {
        'id': id,
        'name': name,
        'price': price
    }
    saved = save_new_book(book)
    if saved:
        print("--- book saved ---")
    else:
        print("--- book not saved ---")
    # save the data in the json file then load it..


def display_books():
    books = get_all_books()
    print(books)


def main_menu():
    while True:
        choice = input('Enter your choice: , n for new, a for all, e for exit :')
        if choice == 'n':
            create_book()
        elif choice == 'a':
            display_books()
        elif choice == 'e':
            exit()
        else:
            print('Please enter a valid choice')




if __name__ == '__main__':
    main_menu()











