import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn import linear_model


def show_scatter_plot(data_set):
    sns.scatterplot(
        x="reviews_from_critics",
        y="avg_vote",
        data=data_set,
    )

    plt.title('Reviews From Critics / Average Votes Scatter Plot')
    plt.xlabel('Reviews From Critics')
    plt.ylabel('Average Vote')
    plt.show()


def show_regression(movies):
    movies = movies[movies.reviews_from_critics > 0.0]

    x_var = pd.DataFrame(movies["reviews_from_critics"])
    y_var = pd.DataFrame(movies["avg_vote"])

    model = linear_model.LinearRegression()
    model.fit(x_var, y_var)
    model.predict(x_var)

    g = sns.regplot(x=x_var, y=y_var, color="b")
    plt.title('Reviews From Critics/ Average Votes')
    plt.xlabel('Reviews From Critics')
    plt.ylabel('Average Vote')
    plt.show()