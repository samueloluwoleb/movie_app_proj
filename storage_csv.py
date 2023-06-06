from istorage import IStorage
import csv
import requests
API_KEY_MOVIES = '1081add1'
API_KEY_COUNTRY = '956/jP02ZyHN3MoeMmFIGA==yefiVIYSS2Je5JNC'


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

    def add_movie(self):
        movies_data = self.load_data(self.File_path)
        search_title = input("Enter new movie name: ")
        try:
            url = f"https://www.omdbapi.com/?apikey={API_KEY_MOVIES}&t={search_title}"
            response = requests.get(url)
            response = response.json()
            title = response.get('Title')
            movies = []
            for data in movies_data:
                movies.append(data[0])
            if title in movies:
                print(f"Movie - {title}, already exists!")
                input("Press enter to continue ")
            elif response['Response'] == 'True':
                year = response['Year']
                rating = response['imdbRating']
                poster_img_url = response['Poster']
                country = response['Country']
                new_movie = [title, rating, year, poster_img_url, country, '']
                movies_data.append(new_movie)
                print(f"Movie - {title}, successfully added")
            else:
                print(f'Movie - {title}, can\'t be found')
            input("Press enter to continue ")
        except Exception:
            print('Please check your internet connectivity')

        with open(self.File_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['name', 'rating', 'year', 'poster', 'country', 'notes'])
            writer.writerows(movies_data)
        input("\nPress enter to continue ")

    def delete_movie(self):
        """
            Deletes a movie from the movies' database.
            Loads the information from the JSON file, deletes the movie,
            and saves it. The function doesn't need to validate the input.
        :param:
        :return:
        """
        movies_data = self.load_data(self.File_path)
        title_list= []
        temp_list = []
        title = input("Enter movie name to delete: ")

        for data in movies_data:
            title_list.append(data[0])
        if title in title_list:
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
        title_list = []
        for data in movies_data:
            title_list.append(data[0])
        if title in title_list:
            notes = input('Enter a note about the movie: ')
            for count, data in enumerate(movies_data):
                if data[0] == title:
                    movies_data[count][5] = notes
            with open(self.File_path, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['name', 'rating', 'year', 'poster', 'country', 'notes'])
                writer.writerows(movies_data)
                print(f'Movie - {title}, successfully updated')
        else:
            print(f"Movie - {title}, doesn't exist: ")
        input("\nPress enter to continue ")
