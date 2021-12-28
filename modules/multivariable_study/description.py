import seaborn as sns
from matplotlib import pyplot as plt


def show_box_plot(movies):
    sns.boxplot(
        x="has_description",
        y="avg_vote",
        data=movies,
    )
    plt.title('Has Description / Average Vote Box Plot')
    plt.xlabel('Has Description')
    plt.ylabel('Average Vote')
    plt.show()
