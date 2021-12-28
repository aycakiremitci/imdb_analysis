import seaborn as sns
from matplotlib import pyplot as plt
import pandas as pd
from sklearn import linear_model


def show_line_plot(movies):
    sns.lineplot(
        data=movies,
        x="year",
        y="avg_vote",
    )

    plt.title('Year / Average Vote Line Plot')
    plt.xlabel('Year')
    plt.ylabel('Average Vote')
    plt.show()


def show_scatter_plot(movies):
    sns.scatterplot(
        x="year",
        y="avg_vote",
        data=movies,
    )

    plt.title('Year / Average Votes Scatter Plot')
    plt.xlabel('Year')
    plt.ylabel('Average Vote')
    plt.show()


def show_regression(movies):
    x_var = pd.DataFrame(movies["year"])
    y_var = pd.DataFrame(movies["avg_vote"])

    model = linear_model.LinearRegression()
    model.fit(x_var, y_var)
    model.predict(x_var)

    sns.regplot(x=x_var, y=y_var, color="b")
    plt.title('Year / Average Vote')
    plt.xlabel('Year')
    plt.ylabel('Average Vote')
    plt.show()
