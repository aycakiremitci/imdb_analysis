import seaborn as sns
import matplotlib.pyplot as plt


def language_pie(movies):
    language_dict_first_20 = dict(movies.language.value_counts().sort_values(ascending=False).head(10))
    labels = language_dict_first_20.keys()
    sizes = language_dict_first_20.values()
    colors = [
        '#FBF8CC',
        '#FDE4CF',
        '#FFCFD2',
        '#F1C0E8',
        '#CFBAF0',
        '#A3C4F3',
        '#90DBF4',
        '#8EECF5',
        '#98F5E1',
        '#B9FBC0',
    ]

    with sns.color_palette("colorblind"):
        plt.pie(
            sizes,
            labels=labels,
            colors=colors,
            autopct='%1.1f%%',
            shadow=True,
            startangle=45,
        )

    plt.title("Languages")
    plt.axis('equal')
    plt.show()