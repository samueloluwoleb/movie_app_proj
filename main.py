from movie_app import MovieApp
from storage_json import StorageJson
from storage_csv import StorageCsv


def main():
    """
        Performs menu operations based on user input and selections
    :return:
    """
    storage = StorageJson('movies_data.json')
    movie_app = MovieApp(storage)
    movie_app.run()


if __name__ == "__main__":
    main()
