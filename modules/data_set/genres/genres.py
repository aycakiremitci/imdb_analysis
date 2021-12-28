import matplotlib.pyplot as plt
import seaborn as sns


def genre_bar(movies):
    movie_genres = movies['genre']
    genres = []  # creating an empty list for genre and genre count.
    genre_counts = []

    for genre_list in movies['genre']:
        for genre in genre_list.split(', '):  # delimiting genre on the bases of comma.
            if genre not in genres:
                genres.append(genre)  # appending the genres in empty list
                genre_counts.append(1)
            else:
                genre_counts[genres.index(genre)] += 1
    # sorting and ordering genres on the basis of count and percentage
    ordered_genres = [x for y, x in sorted(zip(genre_counts, genres))]
    sorted_counts = [x / len(movie_genres) * 100 for x in sorted(genre_counts)]

    # visualizing the graph
    plt.figure(figsize=(10, 10))  #
    #sns.barplot(y=ordered_genres, x=sorted_counts, palette="deep")
    plt.barh(ordered_genres, sorted_counts, color='green')
    plt.xlabel('Percentage of Films (%)')
    plt.title('Distributions of Genres')
    plt.ylabel('Genres')
    plt.show()
