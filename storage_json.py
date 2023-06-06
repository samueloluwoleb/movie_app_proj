from istorage import IStorage
import requests
import json
API_KEY_MOVIES = '1081add1'
API_KEY_COUNTRY = '956/jP02ZyHN3MoeMmFIGA==yefiVIYSS2Je5JNC'


class StorageJson(IStorage):
    """
        a derived class from abstract class for Json storage type
    """

    @staticmethod
    def load_data(file_path):
        """ Loads a JSON file """
        with open(file_path, "r") as handle:
            return json.load(handle)

    def __init__(self, file_path):
        """
            The constructor to initialize the objects
        :param file_path:
        """
        self.File_path = file_path

    def list_movies(self):
        """
            Returns a dictionary of dictionaries that
            contains the movies information in the database.

            The function loads the information from the JSON
            file and returns the data.
        :param:
        :return dict:
        """
        movies_data = self.load_data(self.File_path)
        return movies_data

    def add_movie(self):
        """
            Adds a movie to the movies' database.
            Loads the information from the JSON file, add the movie,
            and saves it. The function doesn't need to validate the input.
        :param:
        :return:
        """
        movies_data = self.load_data(self.File_path)
        search_title = input("Enter new movie name: ")
        try:
            url = f"https://www.omdbapi.com/?apikey={API_KEY_MOVIES}&t={search_title}"
            response = requests.get(url)
            response = response.json()
            title = response.get('Title')
            if title in movies_data:
                print(f"Movie - {title}, already exists!")
                input("Press enter to continue ")
            elif response['Response'] == 'True':
                year = response['Year']
                rating = response['imdbRating']
                poster_img_url = response['Poster']
                country = response['Country']
                new_movie = {
                    'Rating': rating,
                    'Year of Release': year,
                    'Poster Image Url': poster_img_url,
                    'Country': country
                            }
                movies_data[title] = new_movie

                with open(self.File_path, "w") as fileobj:
                    fileobj.write(json.dumps(movies_data))
                    print(f"Movie - {title}, successfully added")
            else:
                print(f'Movie - {title}, can\'t be found')
        except Exception:
            print('Please check your internet connectivity')
        input("Press enter to continue ")

    def delete_movie(self):
        """
            Deletes a movie from the movies' database.
            Loads the information from the JSON file, deletes the movie,
            and saves it. The function doesn't need to validate the input.
        :param:
        :return:
        """
        movies_data = self.load_data(self.File_path)
        title = input("Enter movie name to delete: ")
        if title in movies_data:
            del movies_data[title]
            with open(self.File_path, "w") as fileobj:
                fileobj.write(json.dumps(movies_data))
                print(f'Movie - {title}, successfully deleted')
        else:
            print(f"Movie - {title}, doesn't exist: ")
        input("\nPress enter to continue ")

    def update_movie(self):
        """
            Updates a movie from the movies' database.
            Loads the information from the JSON file, updates the movie,
            and saves it. The function doesn't need to validate the input.
        :param:
        :return:
        """
        movies_data = self.load_data(self.File_path)
        title = input("Enter movie name to update: ")
        if title in movies_data:
            notes = input('Enter a note about the movie: ')
            movies_data[title]['Movie notes'] = notes
            with open(self.File_path, "w") as fileobj:
                fileobj.write(json.dumps(movies_data))
                print(f'Movie - {title}, successfully updated')
        else:
            print(f"Movie - {title}, doesn't exist: ")
        input("\nPress enter to continue ")
