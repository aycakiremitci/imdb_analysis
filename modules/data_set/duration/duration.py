import seaborn as sns
from matplotlib import pyplot as plt
import pandas as pd


def duration_hist(movies):
    durations = pd.Series(movies.duration)

    sns.histplot(
        durations,
        kde=True,
        color='purple',
        bins=100,
        fill=True,
    )

    plt.title('Histogram of Duration')
    plt.xlabel('Duration\n\n\nMean : {:.2f} Median : {:.2f} Mode : {:.2f}'
               .format(durations.mean(), durations.median().mean(), durations.mode().mean()))
    plt.ylabel('Movie Count')
    plt.show()



