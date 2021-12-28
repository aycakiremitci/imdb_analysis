import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn import linear_model


def show_scatter_plot(data_set):
    sns.scatterplot(
        x="votes",
        y="avg_vote",
        data=data_set,
    )

    plt.title('Vote Numbers / Average Votes Scatter Plot')
    plt.xlabel('Vote Numbers')
    plt.ylabel('Average Vote')
    plt.show()


def show_regression(movies):
    x_var = pd.DataFrame(movies["votes"])
    y_var = pd.DataFrame(movies["avg_vote"])

    model = linear_model.LinearRegression()
    model.fit(x_var, y_var)
    model.predict(x_var)

    g = sns.regplot(x=x_var, y=y_var, color="b")
    plt.title('Vote Numbers/ Average Votes')
    plt.xlabel('Vote Number')
    plt.ylabel('Average Vote')
    plt.show()