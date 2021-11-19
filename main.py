from modules.csv import init_csv
from modules.data_set.average_vote import average_vote
from modules.data_set.countries import countries
from modules.data_set.duration import duration
from modules.data_set.genres import genres
from modules.data_set.languages import languages
from modules.data_set.production_company import production_company


def initialize_analysis():
    movies_set = init_csv.initialize_data_set()
    init_csv.configure_rc_params()
    return movies_set


def duration_graph():
    duration.duration_hist(movies)


def genre_graph():
    genres.genre_bar(movies)


def country_graph():
    countries.country_pie(movies)


def language_graph():
    languages.language_pie(movies)


def avg_vote_graph():
    average_vote.avg_vote_hist(movies)


def production_company_graph():
    production_company.companies_bar(movies)


movies = initialize_analysis()
duration_graph()
genre_graph()
country_graph()
language_graph()
avg_vote_graph()
production_company_graph()
