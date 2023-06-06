from abc import ABC, abstractmethod


class IStorage(ABC):
    """
        abstract class with abstract methods used as template for implementing storage format
    """
    @abstractmethod
    def list_movies(self):
        """
            list the movies in database, method to be implemented by inherited classes
        :return:
        """
        pass

    @abstractmethod
    def add_movie(self, title, year, rating,  poster_img_url, country):
        """
            adds a movie to the database, method to be implemented by inherited classes
        :param title:
        :param year:
        :param rating:
        :param poster_img_url:
        :param country:
        :return:
        """
        pass

    @abstractmethod
    def delete_movie(self, title):
        """
            deletes a movie and updates the database, method to be implemented by inherited classes
        :param title:
        :return:
        """
        pass

    @abstractmethod
    def update_movie(self, title, notes):
        """
            updates a movie and updates the database, method to be implemented by inherited classes
        :param title:
        :param notes:
        :return:
        """
        pass
