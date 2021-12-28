import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn import linear_model


def show_scatter_plot(movies):
    movies = movies[movies.metascore > 0.0]

    sns.scatterplot(
        x="metascore",
        y="avg_vote",
        data=movies,
    )

    plt.title('Metascore / Average Votes Scatter Plot')
    plt.xlabel('Metascore')
    plt.ylabel('Average Vote')
    plt.show()


def show_regression(movies):
    movies = movies[movies.metascore > 0.0]

    x_var = pd.DataFrame(movies["metascore"])
    y_var = pd.DataFrame(movies["avg_vote"])

    model = linear_model.LinearRegression()
    model.fit(x_var, y_var)
    model.predict(x_var)

    g = sns.regplot(x=x_var, y=y_var, color="b")
    plt.title('Metascore/ Average Votes')
    plt.xlabel('Metascore')
    plt.ylabel('Average Vote')
    plt.show()