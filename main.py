from movie_app import MovieApp
from storage_json import StorageJson
from storage_csv import StorageCsv
import random
import sys


def main():
    """
        Performs menu operations based on user input and selections
    :return:
    """
    def load_csv():
        """
            This is called when a csv file is the preferred storage
        :return:
        """
        storage = StorageCsv('movies_data.csv')
        movie_app = MovieApp(storage)
        movie_app.run()

    def load_json():
        """
            This is called when a json file is the preferred storage
        :return:
        """
        storage = StorageJson('movies_data.json')
        movie_app = MovieApp(storage)
        movie_app.run()

    # block of code be executed if a command line argument is provided
    if len(sys.argv) > 1:
        cmd_line_arg = sys.argv[1]
        print(cmd_line_arg)
        cmd_line_arg_list = cmd_line_arg.split('.')
        if cmd_line_arg_list[1] == 'json':
            load_json()
        elif cmd_line_arg_list[1] == 'csv':
            load_csv()
    # block of code be executed if a command line argument is not provided
    else:
        print(f"What kind of storage file should be implemented?\n"
              f"Enter '1' for csv, '2' for json, 'r' for random pick, 'q' to exit: ")
        while True:
            user_input = input()
            if user_input not in ['1', '2', 'r', 'q']:
                print('Please enter the correct input')
            else:
                break
        if user_input == 'q':
            print('Bye')
            quit()
        elif user_input == '1':
            load_csv()
        elif user_input == '2':
            load_json()
        elif user_input == 'r':
            random_choice = random.randint(1, 2)
            if random_choice == 1:
                load_csv()
            if random_choice == 2:
                load_json()


if __name__ == "__main__":
    main()
