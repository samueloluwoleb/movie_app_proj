from istorage import IStorage
import json


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

    def add_movie(self, title, year, rating, poster_img_url, country):
        """
            Adds a movie to the movies' database.
            Loads the information from the JSON file, add the movie,
            and saves it. The function doesn't need to validate the input.
        :param title:
        :param year:
        :param rating:
        :param poster_img_url:
        :param country:
        :return:
        """
        movies_data = self.load_data(self.File_path)
        new_movie = {
            'Rating': rating,
            'Year of Release': year,
            'Poster Image URL': poster_img_url,
            'Country': country
        }
        movies_data[title] = new_movie
        with open(self.File_path, "w") as fileobj:
            fileobj.write(json.dumps(movies_data))

    def delete_movie(self, title):
        """
            Deletes a movie from the movies' database.
            Loads the information from the JSON file, deletes the movie,
            and saves it. The function doesn't need to validate the input.
        :param title:
        :return:
        """
        movies_data = self.load_data(self.File_path)
        del movies_data[title]
        with open(self.File_path, "w") as fileobj:
            fileobj.write(json.dumps(movies_data))

    def update_movie(self, title, notes):
        """
            Updates a movie from the movies' database.
            Loads the information from the JSON file, updates the movie,
            and saves it. The function doesn't need to validate the input.
        :param title:
        :param notes:
        :return:
        """
        movies_data = self.load_data(self.File_path)
        movies_data[title]['Movie notes'] = notes
        with open(self.File_path, "w") as fileobj:
            fileobj.write(json.dumps(movies_data))


