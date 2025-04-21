import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def data_visualization():
    df = pd.read_csv('employees.csv')

    # Histogram-Understanding Data Distribution
    plt.figure(figsize=(8, 5))
    sns.histplot(df['Salary'], bins=30, kde=True)
    plt.title('Histogram of Salary')
    plt.show()

    # Boxplot-Identifying Outliers
    plt.figure(figsize=(6, 4))
    sns.boxplot(x=df['Salary'])
    plt.title('Boxplot of Salary')
    plt.show()

    # Scatterplot-Relationship Between Variables
    plt.figure(figsize=(6, 4))
    sns.scatterplot(x=df['Salary'], y=df['Bonus %'])
    plt.title('Scatterplot between Salary & Bonus %')
    plt.show()

    # Correlation Heatmap-Detecting Relationships
    df_numeric = df.select_dtypes(include=['number'])  # select only numerical columns
    plt.figure(figsize=(10, 6))
    sns.heatmap(df_numeric.corr(), annot=True, cmap='coolwarm', linewidths=0.5)
    plt.title('Correlation Heatmap')
    plt.show()


data_visualization()