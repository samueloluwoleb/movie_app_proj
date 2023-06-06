from statistics import median
import random
from fuzzywuzzy import fuzz
import requests
API_KEY_MOVIES = '1081add1'
API_KEY_COUNTRY = '956/jP02ZyHN3MoeMmFIGA==yefiVIYSS2Je5JNC'


class MovieApp:
    """
        a class that defines all the functionality of the movie app
    """
    def __init__(self, storage):
        self._storage = storage

    @staticmethod
    def display_menu():
        """
            Defines a function that displays the menu for user to take action
        :param:
        :return:
        """
        menu = """
                ********** My Movies Database **********

        Menu:
        0. Exit
        1. List movies
        2. Add movie
        3. Delete movie 
        4. Update movie
        5. Stats
        6. Random movie
        7. Search movie
        8. Movies sorted by rating
        9. Generate website
            """
        print(f"{menu}")
        print("\t Enter choice (0-9): ", end='')

    @staticmethod
    def exit_command():
        """
             Exits the program without raising any error
            :param:
            :return:
        """
        print('Bye!')
        quit()

    def list_movies(self):
        """
            Defines a function list_movies to display the movies in the database
        :param:
        :return:
        """
        movies = self._storage.list_movies()
        for keys, values in movies.items():
            if values.get('Movie notes') is None:
                print(
                    f"Movie Title - {keys}\nRating - {values['Rating']}\nYear of Release - {values['Year of Release']}"
                    f"\nPoster Image Url - {values['Poster Image Url']}\n")
            else:
                print(
                    f"Movie Title - {keys}\nRating - {values['Rating']}\nYear of Release - {values['Year of Release']}"
                    f"\nPoster Image Url - {values['Poster Image Url']}\nMovie Notes - {values['Movie notes']}\n")
        input("Press enter to continue ")

    def add_movie(self):
        """
            Adds a new movie to the database of movies
        :param:
        :return:
        """
        movies_data = self._storage.load_data(self._storage.File_path)
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
                self._storage.add_movie(title, rating, year, poster_img_url, country)
                print(f"Movie - {title}, successfully added")
            else:
                print(f'Movie - {title}, can\'t be found')
                input("Press enter to continue ")
        except Exception:
            print('Please check your internet connectivity')
        input("\nPress enter to continue ")

    def del_movie(self):
        """
        Define a del_movie function to delete and update the movie database
        :param:
        :return:
        """
        movies_data = self._storage.load_data(self._storage.File_path)
        title = input("Enter movie to be deleted: ")
        title_list = []
        for data in movies_data:
            title_list.append(data[0])
        if title in title_list:
            self._storage.delete_movie(title)
            print(f'Movie - {title}, successfully deleted')
        else:
            print(f"Movie {title}, doesn't exist: ")
        input("\nPress enter to continue ")



    def update_movie(self):
        """
            Defines an update_movie function that changes the rating of a movie which exists in the movie database
        :param:
        :return:
        """
        movies_data = self._storage.load_data(self._storage.File_path)
        title = input("Enter new movie name: ")
        title_list = []
        for data in movies_data:
            title_list.append(data[0])
        if title in title_list:
            notes = input('Enter a note about the movie: ')
            self._storage.update_movie(title, notes)
	    print(f'Movie - {title}, successfully updated')	
        else:
            print(f"Movie - {title}, doesn't exist: ")
        input("\nPress enter to continue ")


    @staticmethod
    def average_rating(movies):
        """
            calculates and prints the average movie rating of all movie ratings
        :param movies:
        :return:
        """
        ratings_list = []
        for title in movies:
            if movies[title]['Rating'] == 'N/A':
                continue
            ratings_list.append(float(movies[title]['Rating']))
        ave_rating = sum(ratings_list) / len(ratings_list)
        print(f"Average rating: {ave_rating:.1f}")

    @staticmethod
    def median_rating(movies):
        """
            calculates and prints the median movie rating
        :param movies:
        :return:
        """
        ratings_list = []
        for title in movies:
            if movies[title]['Rating'] == 'N/A':
                continue
            ratings_list.append(float(movies[title]['Rating']))
        med_rating = median(ratings_list)
        print(f"Median rating: {med_rating:.1f}")

    @staticmethod
    def best_movies(movies):
        """
            prints the lists of Best movies if more than one movie has the same rating
        :param movies:
        :return:
        """
        ratings_list = []
        for title in movies:
            if movies[title]['Rating'] == 'N/A':
                continue
            ratings_list.append(float(movies[title]['Rating']))
        movies_list = list(movies.keys())
        max_list = []
        max_num = max(ratings_list)
        count_max = 0
        for x in ratings_list:
            if x == max_num:
                max_list.append(count_max)
            count_max += 1
        for x in max_list:
            print(f"Best movie(s): {movies_list[x]}, {ratings_list[x]}")

    @staticmethod
    def worst_movies(movies):
        """
            prints the lists of Worst movies if more than one movie has the same rating
        :param movies:
        :return:
        """
        ratings_list = []
        for title in movies:
            if movies[title]['Rating'] == 'N/A':
                continue
            ratings_list.append(float(movies[title]['Rating']))
        movies_list = list(movies.keys())
        min_list = []
        min_num = min(ratings_list)
        count_min = 0
        for x in ratings_list:
            if x == min_num:
                min_list.append(count_min)
            count_min += 1
        for x in min_list:
            print(f"Worst movie(s): {movies_list[x]}, {ratings_list[x]}")

    def movie_statistics(self):
        """
            This function calls the:
                average_rating,
                median_rating,
                best_movies,
                worst_movies functions
        :param:
        :return:
        """
        movies = self._storage.list_movies()
        print('')
        self.average_rating(movies)
        self.median_rating(movies)
        self.best_movies(movies)
        self.worst_movies(movies)
        input("\nPress enter to continue ")

    def random_movies(self):
        """
            Defines a random_movies function that displays a movie plus its rating at random
        :param:
        :return:
        """
        movies = self._storage.list_movies()
        ratings_list = []
        for title in movies:
            if movies[title]['Rating'] == 'N/A':
                ratings_list.append(float(0))
            else:
                ratings_list.append(float(movies[title]['Rating']))
        movies_list = list(movies.keys())
        random_num = random.randint(0, len(movies))
        print(f"Your movie for tonight: {movies_list[random_num]}, it's rated {ratings_list[random_num]} ")
        input("\nPress enter to continue ")

    def search_movie(self):
        """
            Defines a function search_movie that return list of movies that matches the search query
        :param:
        :return:
        """
        movies = self._storage.list_movies()
        ratio_list = []
        movies_list = list(movies.keys())
        searched_word = input("Enter a search: ")
        for title in movies_list:
            ratio_num = fuzz.ratio(searched_word.lower(), title.lower())
            ratio_list.append(ratio_num)
        sorted_ratio = sorted(ratio_list, reverse=True)
        print(movies_list[ratio_list.index(sorted_ratio[0])])
        print(movies_list[ratio_list.index(sorted_ratio[1])])
        print(movies_list[ratio_list.index(sorted_ratio[2])])
        input("\nPress enter to continue ")

    def sort_movies(self):
        """
            Defines a sort_movies that sorts through the movie lists by value and prints the sorted movie
        :param:
        :return:
        """
        movies = self._storage.list_movies()
        for title in movies:
            if movies[title]['Rating'] == 'N/A':
                movies[title]['Rating'] = 0
        sorted_list = sorted(movies.keys(), key=lambda x: float(movies[x]['Rating']), reverse=True)
        for keys in sorted_list:
            if movies[keys]['Rating'] == 0:
                print(f"{keys} : N/A")
            else:
                print(f"{keys} : {movies[keys]['Rating']}")
        input("\nPress enter to continue ")

    @staticmethod
    def movie_data_generator(movie_data, movies_data):
        """
            connects to multiple APIs to get the movie data needed for object
            serialization
        :param movie_data:
        :param movies_data:
        :return:
        """
        country_plus_code = {
            "United States": "US",
            "Canada": "CA",
            "Japan": "JP",
            "United Kingdom": "GB",
            "Poland": "PL",
            "Yemen": "YE",
            "Italy": "IT",
            "Nigeria": "NG",
            "France": "FR",
            "Australia": "AU",
            "South Africa": "ZA",
            "China": "CN",
            "Spain": "ES",
            "India": "IN"
        }

        title = movie_data
        year = movies_data[movie_data]["Year of Release"]
        image_url = movies_data[movie_data]["Poster Image Url"]
        rating = movies_data[movie_data]["Rating"]
        country = movies_data.get(movie_data).get("Country")
        country = country.split(',')
        country = country[0]
        countries_list = list(country_plus_code.keys())
        if country in countries_list:
            country_code = country_plus_code[country]
        else:
            api_url_country = f'https://api.api-ninjas.com/v1/country?name={country}'
            response = requests.get(api_url_country, headers={'X-Api-Key': API_KEY_COUNTRY})
            country_code = response.json()[0]["iso2"]
        imdb_title = title.replace(' ', '%20')
        imdb_url = f"https://www.imdb.com/find/?q={imdb_title}&ref_=nv_sr_sm"
        notes = movies_data.get(movie_data).get("Movie notes")

        return title, year, image_url, rating, country_code, imdb_url, notes

    def serialize(self):
        """
            Serializes a movie object representing a specific movie by calling the
            movie_data_generator function and unpacking the tuple data to return a serialized object as string.
        :param:
        :return str:
        """
        movies = self._storage.list_movies()
        output = ''
        for movie in movies:
            title, year, image_url, rating, country_code, imdb_url, notes = self.movie_data_generator(movie, movies)
            output += '<li><div class="movie tooltip">\n'
            output += f'<a href={imdb_url} target="_blank"><img class="movie-poster" src={image_url}" title=""/></a>\n'
            if movies.get(movie).get("Movie notes") is not None:
                output += f'<span class="tooltip-text"> {notes} </span>'
            output += '<div class="movie-title">\n'
            output += f"{title}"
            output += '</div>'
            output += '<div class="movie-year">\n'
            output += f"{year}"
            output += '</div>'
            output += '<div class="movie-rating">\n'
            output += f"{rating}"
            output += '</div>'
            output += '<div class="country-flag">\n'
            output += f'<img src="https://flagsapi.com/{country_code}/flat/32.png"/>\n'
            output += '</div>'
            output += '</div></li>\n'

        return output

    def generate_website(self):
        """
            Defines a generate_website function that generates a html document of a list of movies in database using the
            index_html template

        :param:
        :return:
        """
        template_title = "Samuel's Movie App"
        output = self.serialize()
        with open("index_template.html", "r") as fileobj:
            data = fileobj.read()
            replaced_data = data.replace("__TEMPLATE_TITLE__", template_title)
            replaced_data = replaced_data.replace("__TEMPLATE_MOVIE_GRID__", output)

        with open(f"movie.html", "w") as fileobj:
            fileobj.write(replaced_data)
            print(f'Website was successfully generated to the file movie.html')
        input("\nPress enter to continue ")

    def run(self):
        while True:
            self.display_menu()
            user_input = int(input())
            if user_input == 0:
                self.exit_command()
            elif user_input == 1:
                self.list_movies()
            elif user_input == 2:
                self.add_movie()
            elif user_input == 3:
                self.del_movie()
            elif user_input == 4:
                self.update_movie()
            elif user_input == 5:
                self.movie_statistics()
            elif user_input == 6:
                self.random_movies()
            elif user_input == 7:
                self.search_movie()
            elif user_input == 8:
                self.sort_movies()
            elif user_input == 9:
                self.generate_website()
            else:
                input("\nPress enter to continue ")