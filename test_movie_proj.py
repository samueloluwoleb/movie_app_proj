import pytest
from storage_json import StorageJson
from storage_csv import StorageCsv
from movie_app import MovieApp

storage_csv = StorageCsv("movies_data.csv")
storage_json = StorageJson("movies_data.json")
app_movie_csv = MovieApp(storage_csv)
app_movie_json = MovieApp(storage_json)


def test_creating_obj_json():
    assert storage_json.File_path == "movies_data.json"


def test_creating_obj_csv():
    assert storage_csv.File_path == "movies_data.csv"


def test_list_movie_csv():
    assert type(storage_csv.list_movies()) is dict


def test_list_movie_json():
    assert type(storage_json.list_movies()) is dict


pytest.main()
