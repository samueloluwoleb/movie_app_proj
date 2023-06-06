from istorage import IStorage
import csv


class StorageCsv(IStorage):
    """
        a derived class from abstract class for Json storage type
    """

    @staticmethod
    def load_data(file_path):
        """ Loads a csv file """
        with open(file_path, "r") as handle:
            reader = csv.reader(handle)
            next(reader)
            data = list(reader)
        return data

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

            The function loads the information from the CSV
            file and returns the data.
        :param:
        :return dict:
        """
        data = {}
        movies_data = self.load_data(self.File_path)
        for count, row in enumerate(movies_data):
            if row[5] == '':
                movies_data[count][5] = None
                name, rating, year, poster, country, notes = row
                data[name] = {'Rating': rating, 'Year of Release': year,
                              'Poster Image Url': poster, 'Country': country, 'Movie notes': notes}
            else:
                name, rating, year, poster, country, notes = row
                data[name] = {'Rating': rating, 'Year of Release': year,
                              'Poster Image Url': poster, 'Country': country, 'Movie notes': notes}
        return data

    def add_movie(self, title, rating, year, poster_img_url, country):
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
        new_movie = [title, rating, year, poster_img_url, country, '']
        movies_data.append(new_movie)

        with open(self.File_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['name', 'rating', 'year', 'poster', 'country', 'notes'])
            writer.writerows(movies_data)

    def delete_movie(self, title):
        """
            Deletes a movie from the movies' database.
            Loads the information from the JSON file, deletes the movie,
            and saves it. The function doesn't need to validate the input.
        :param title:
        :return:
        """
        movies_data = self.load_data(self.File_path)
        temp_list = []
        for data in movies_data:
            if data[0] == title:
                continue
            else:
                temp_list.append(data)
        movies_data = temp_list

        with open(self.File_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['name', 'rating', 'year', 'poster', 'country', 'notes'])
            writer.writerows(movies_data)

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
        for count, data in enumerate(movies_data):
            if data[0] == title:
                movies_data[count][5] = notes

        with open(self.File_path, 'w',newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['name', 'rating', 'year', 'poster', 'country', 'notes'])
            writer.writerows(movies_data)