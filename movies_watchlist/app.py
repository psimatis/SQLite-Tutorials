import database
import datetime

menu = """Please select one of the following options:
1) Add new movie.
2) View upcoming movies.
3) View all movies
4) Watch a movie
5) View watched movies.
6) Add user.
7) Search for a movie.
8) Exit.

Your selection: """
print("Welcome to the watchlist app!")

database.create_tables()


def prompt_add_movie():
    title = input("Movie title: ")
    release_date = input("Release date (dd-mm-yyyy): ")
    parsed_date = datetime.datetime.strptime(release_date, "%d-%m-%Y")
    timestamp = parsed_date.timestamp()
    database.add_movies(title, timestamp)


def print_movie_list(heading, movies):
    print(f'{heading} movies')
    for _id, title, release_date in movies:
        movie_date = datetime.datetime.fromtimestamp(release_date)
        human_date = movie_date.strftime("%d %b %Y")
        print(f"{_id}: {title} on {human_date}")
    print('---\n')


def prompt_watch_movie():
    username = input('Username:')
    movie_id = input("Movie id:")
    database.watch_movie(username, movie_id)


def prompt_add_user():
    username = input('Username:')
    database.add_user(username)


def prompt_show_watched_movies():
    username = input('Username: ')
    movies = database.get_watched_movies(username)
    if movies:
        print_movie_list(f"{username}'s watched", movies)
    else:
        print('No movies')


def prompt_search_movies():
    search_term = input("Enter partial movie title:")
    movies = database.search_movies(search_term)
    if movies:
        print_movie_list("Movies found", movies)
    else:
        print("No movies found")


while (user_input := input(menu)) != "8":
    if user_input == "1":
        prompt_add_movie()
    elif user_input == "2":
        movies = database.get_movies(True)
        print_movie_list("Upcoming", movies)
    elif user_input == "3":
        movies = database.get_movies()
        print_movie_list("All", movies)
    elif user_input == "4":
        prompt_watch_movie()
    elif user_input == "5":
        prompt_show_watched_movies()
    elif user_input == "6":
        prompt_add_user()
    elif user_input == "7":
        prompt_search_movies()
    else:
        print("Invalid input, please try again!")
