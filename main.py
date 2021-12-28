from modules.csv import init_csv
from modules.data_set.average_vote import average_vote
from modules.data_set.countries import countries
from modules.data_set.duration import duration
from modules.data_set.genres import genres
from modules.data_set.languages import languages
from modules.data_set.production_company import production_company
from modules.multivariable_study import genre
from modules.multivariable_study import votes_number
from modules.multivariable_study import heatmap
from modules.multivariable_study import duration
from modules.multivariable_study import metascore
from modules.multivariable_study import reviews_from_users
from modules.multivariable_study import reviews_from_critics
from modules.multivariable_study import year
from modules.multivariable_study import description
from modules.multivariable_study import countries
from modules.multivariable_study import language

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


def scatter_plots():
    #votesNumber_score.show_scatter_plot(movies)
    #votesNumber_score.show_regression(movies)
    #duration_score.show_scatter_plot(movies)
    #duration_score.show_regression(movies)
    #metascore_score.show_scatter_plot(movies)
    #metascore_score.show_regression(movies)
    #reviews_from_users.show_scatter_plot(movies)
    #reviews_from_users.show_regression(movies)
    #reviews_from_critics.show_scatter_plot(movies)
    #reviews_from_critics.show_regression(movies)
    year.show_scatter_plot(movies)
    year.show_regression(movies)


def box_plots():
    description.show_box_plot(movies)
    genre_score.show_box_plot(movies)
    language.show_box_plot(movies)
    countries.show_box_plot(movies)


def line_plots():
    year.show_line_plot(movies)


movies = initialize_analysis()
#duration_graph()
#genre_graph()
#country_graph()
#anguage_graph()
#avg_vote_graph()
#production_company_graph()
heatmap.show_correlation_map(movies)
heatmap.show_correlation_heatmap(movies)
#scatter_plots()
box_plots()
#line_plots()
