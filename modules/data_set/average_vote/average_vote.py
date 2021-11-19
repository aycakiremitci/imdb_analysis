import seaborn as sns
import matplotlib.pyplot as plt


def avg_vote_hist(movies):
    average = movies['avg_vote'].mean()
    fig_dim = (10, 7)
    fig, ax = plt.subplots(figsize=fig_dim)
    sns.histplot(
        movies['avg_vote'],
        ax=ax,
        kde=True,
        color='pink',
        bins=10,
        fill=True,
    )
    plt.axvline(average, color='green', label='Average rating: {:.2f}'.format(average))
    plt.legend()
    plt.title('Distribution of the ratings')
    plt.xlabel('Average Vote')
    plt.show()
