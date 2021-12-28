from matplotlib import rcParams
import pandas as pd


def initialize_data_set():
    movies = pd.read_csv('C:/Users/ayca/PycharmProjects/imdb_analysis/assets/IMDb movies.csv')
    print(f'Number of movies in dataset: {len(movies)}')

    movies.head()

    movies = movies.assign(**{'has_description': movies.description > ""})
    movies["year"] = movies["year"].apply(lambda val: float(str(val)))
    movies["genre_first"] = movies['genre'].apply(lambda val: val.split(',')[0])
    movies["language_first"] = movies['language'].apply(lambda val: str(val).split(',')[0])
    movies["country_first"] = movies['country'].apply(lambda val: str(val).split(',')[0])

    print(movies.info())

    return movies


def configure_rc_params():
    rcParams['figure.figsize'] = 8, 6
    rcParams['font.family'] = 'Courier New',
    rcParams['font.size'] = 12.0
    rcParams['axes.titlesize'] = 18
    rcParams['axes.labelsize'] = 14
    rcParams['xtick.labelsize'] = 14
    rcParams['ytick.labelsize'] = 14
    rcParams['legend.fontsize'] = 11
    return rcParams
