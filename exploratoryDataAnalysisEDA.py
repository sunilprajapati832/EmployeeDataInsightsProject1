import pandas as pd

def exploratory_data_analysis():
    # EDA
    df = pd.read_csv('employees.csv')
    df['first name'] = (
         df['First Name']
         .str.strip()
         .str.upper()
         .str.replace(r'\s+', ' ', regex=True)
    )
    pd.set_option('display.max_rows', None)
    df_unique = df.drop_duplicates(subset='first name')
    print(df_unique)

    # measure of Central Tendency
    print("\nMean of 'Salary' is: "  , round(df['Salary'].mean()))
    print("Median of 'Salary' is: ", round(df['Salary'].median()))
    print("Mode of 'Team' is: ", df['Team'].mode())

    # measure of Spread
    print("\nStandard Deviation of 'Salary' : ", df['Salary'].std()) # measure standard deviation
    print("Variance in 'Salary' is: ", df['Salary'].var()) # measure variance

    # Interquartile Range (IQR)
    q1 = df['Salary'].quantile(0.25)
    q2 = df['Salary'].quantile(0.75)
    iqr = q2 - q1
    print("\nFirst quartile (0.25) : ", q1)
    print("Second quartile (0.75) : ",q2)
    print("Inter quartile range 'IQR' :", iqr)

exploratory_data_analysis()