import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn import linear_model


def show_scatter_plot(data_set):
    sns.scatterplot(
        x="duration",
        y="avg_vote",
        data=data_set,
    )

    plt.title('Duration / Average Votes Scatter Plot')
    plt.xlabel('Duration')
    plt.ylabel('Average Vote')
    plt.show()


def show_regression(movies):
    x_var = pd.DataFrame(movies["duration"])
    y_var = pd.DataFrame(movies["avg_vote"])

    model = linear_model.LinearRegression()
    model.fit(x_var, y_var)
    model.predict(x_var)

    g = sns.regplot(x=x_var, y=y_var, color="g")
    plt.title('Duration/ Average Votes')
    plt.xlabel('Duration')
    plt.ylabel('Average Vote')
    plt.show()