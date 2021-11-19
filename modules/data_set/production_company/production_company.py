import matplotlib.pyplot as plt
import seaborn as sns


def companies_bar(movies):
    company_dict_first_20 = dict(movies.production_company.value_counts().sort_values(ascending=False).head(20))

    plt.figure(figsize=(10, 10))  #
    sns.barplot(y=list(company_dict_first_20.keys()), x=list(company_dict_first_20.values()), color="purple")
    plt.xlabel('\nNumber of Movies')
    plt.title('Distributions of Production Companies')
    plt.ylabel('Companies\n')
    plt.show()
