
from connect import connect_db
from find import find_db
from create_db_load_data import create_db_load_date
from find_quote import find_quote
from scrap import scraping_site


def menu():

    commands = [" 1  - Create DB and load date",
                " 2  - Check DB connection",
                " 3  - Scrap ",
                " 4  - Output в розробці ",
                " 5  - Create в розробці",
                " 6  - Find all date DB ",
                " 7  - Update в розробці",
                " 8  - Delete в розробці ",
                " 9  - Find Quote ",
                " 0  - Exit"
                ]

    while True:

        print("_"*31)
        print("| {:<1} {:^27}|".format("☰", "Welcome to main menu"))
        print('|'+'_'*30 + '|')
        for el in commands:
            print('|{:<30}|'.format(el))
        print('|'+'_'*30 + '|')
        print('|{:<30}|'.format('Type number to start:  '))
        user_input = input("|>>> ")
        print('|'+'_'*30 + '|')

        if user_input == '1':
            print("_"*31)
            print("|{:^28}|".format("✨ Create DB! ✨"))
            print("|"+"_"*30 + "|")
            name_db = input(("|>>> Input name DB "))
            print(create_db_load_date(name_db))

        elif user_input == '2':
            print("_"*30)
            print("|{:^27}|".format("✨ Connect DB! ✨"))
            print("|"+"_"*29 + "|")
            name_db = input(("|>>> Input name DB "))
            print(connect_db(name_db))
        elif user_input == '3':
            print("_"*30)
            print("|{:^30}|".format("✨ Scraping site! ✨"))
            print("|"+"_"*28 + "|")
            # print('В розробці')
            # result = load_to_db()
            print(scraping_site())
        elif user_input == '4':
            print("_"*30)
            print("|{:^30}|".format("✨ Output date from DB! ✨"))
            print("|"+"_"*28 + "|")
            print('В розробці')
            # output_from_db()
        elif user_input == '5':
            print("_"*30)
            print("|{:^30}|".format("✨ Create document! ✨"))
            print("|"+"_"*30 + "|")
            print('В розробці')
            # create_doc()
        elif user_input == '6':
            print("_"*30)
            print("|{:^30}|".format("✨ Find date! ✨"))
            print("|"+"_"*30 + "|")
            name_db = input(("|>>> Input name DB "))
            name_col = input(("|>>> Input name collection "))
            print(find_db(name_db, name_col))
        elif user_input == '7':
            print("_"*30)
            print("|{:^30}|".format("✨ Update date! ✨"))
            print("|"+"_"*30 + "|")
            print('В розробці')
            # update_doc()
        elif user_input == '8':
            print("_"*30)
            print("|{:^30}|".format("✨ Delete date! ✨"))
            print("|"+"_"*30 + "|")
            print('В розробці')
            # delete_doc()
        elif user_input == '9':
            print("_"*30)
            print("|{:^30}|".format("✨ Find Quotes! ✨"))
            print("|"+"_"*30 + "|")

            print(find_quote())
        elif user_input == '0' or user_input.lower() == "exit":
            print('\nGoodbye!\n')
            break
        else:
            print("_"*30)
            print("|{:^30}|".format("Wrong number... Try again..."))
            print("|"+"_"*30 + "|")


if __name__ == '__main__':
    menu()
