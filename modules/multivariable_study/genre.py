import matplotlib.pyplot as plt
import seaborn as sns


def show_box_plot(movies):
    sns.boxplot(
        x="genre_first",
        y="avg_vote",
        data=movies,
    )
    plt.title('Genre / Average Vote Box Plot')
    plt.xlabel('Genres')
    plt.ylabel('Average Vote')
    plt.show()
