import pandas as pd

def exploratory_data_analysis2():
    # EDA according to Bonus %
    df = pd.read_csv('employees.csv')

    # measure of Central Tendency
    print("\nMean of 'Bonus %' is: ", round(df['Bonus %'].mean()))
    print("Median of 'Bonus %' is: ", round(df['Bonus %'].median()))
    print("Mode of 'Gender' is: ", df['Gender'].mode())

    # measure of Spread
    print("\nStandard Deviation of 'Bonus %' : ", df['Bonus %'].std())  # measure standard deviation
    print("Variance in 'Bonus %' is: ", df['Bonus %'].var())  # measure variance

    # Interquartile Range (IQR)
    q1 = df['Bonus %'].quantile(0.25)
    q2 = df['Bonus %'].quantile(0.75)
    iqr = q2 - q1
    print("\nFirst quartile (0.25) : ", q1)
    print("Second quartile (0.75) : ", q2)
    print("Inter quartile range 'IQR' :", iqr)

exploratory_data_analysis2()