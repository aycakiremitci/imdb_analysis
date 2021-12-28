import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def show_box_plot(movies):
    country_first_10 = pd.Series(movies.country_first.value_counts().sort_values(ascending=False).head(10))
    print("USA" in country_first_10.keys())

    movies["country_check"] = movies['country_first'].apply(lambda val: str(val) if str(val) in country_first_10.keys() else "false")

    movies = movies[movies.country_check != "false"]
    sns.boxplot(
        x="country_first",
        y="avg_vote",
        data=movies,
    )
    plt.title('Country / Average Vote Box Plot')
    plt.xlabel('Countries')
    plt.ylabel('Average Vote')
    plt.show()
