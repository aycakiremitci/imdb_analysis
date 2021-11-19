import seaborn as sns
import matplotlib.pyplot as plt


def country_pie(movies):
    country_dict_first_10 = dict(movies.country.value_counts().sort_values(ascending=False).head(10))
    labels = country_dict_first_10.keys()
    sizes = country_dict_first_10.values()
    colors = [
        '#fff100',
        '#ff8c00',
        '#e81123',
        '#ec008c',
        '#68217a',
        '#00188f',
        '#00bcf2',
        '#00b294',
        '#009e49',
        '#bad80a',
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

    plt.title("Countries")
    plt.axis('equal')
    plt.show()
