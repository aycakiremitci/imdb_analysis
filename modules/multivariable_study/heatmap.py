import matplotlib.pyplot as plt
import seaborn as sb


def show_correlation_map(movies):
    ax = plt.subplots()
    hm = sb.heatmap(movies.corr(), annot=True, linewidths=.5, fmt=".2f", cmap="Wistia_r")
    hm.set_yticklabels(labels=movies.corr().columns.values, va="top", rotation=22)
    hm.set_xticklabels(labels=movies.corr().columns.values, ha="right", rotation=22)
    plt.title("Correlation Heatmap")
    plt.show()


def show_correlation_heatmap(movies):
    plt.subplots()
    hm = sb.heatmap(movies.corr(), vmax=1, square=True)
    hm.set_yticklabels(labels=movies.corr().columns.values, va="top", rotation=22)
    hm.set_xticklabels(labels=movies.corr().columns.values, ha="right", rotation=22)
    plt.title("Correlation Heatmap")
    plt.show()
