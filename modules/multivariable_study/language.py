import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def show_box_plot(movies):
    language_dict_first_10 = pd.Series(movies.language_first.value_counts().sort_values(ascending=False).head(10))
    print("English" in language_dict_first_10.keys())

    movies["language_check"] = movies['language_first'].apply(lambda val: str(val) if str(val) in language_dict_first_10.keys() else "false")

    movies = movies[movies.language_check != "false"]
    sns.boxplot(
        x="language_first",
        y="avg_vote",
        data=movies,
    )
    plt.title('Language / Average Vote Box Plot')
    plt.xlabel('Languages')
    plt.ylabel('Average Vote')
    plt.show()
