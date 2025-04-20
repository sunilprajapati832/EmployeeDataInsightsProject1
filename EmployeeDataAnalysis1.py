import pandas as pd
import matplotlib.pyplot as plt

def read_csv_file():
    file_path = 'employees.csv' # Filepath to your CSV file
    df = pd.read_csv(file_path) # Read the CSV file using pandas
    print("Original Dataframe:")
    pd.set_option('display.max_rows', None)    # Show all rows
    pd.set_option('display.max_columns', None) # Show all columns
    print(df)  # print the DataFrame

# read_csv_file()

def data_cleaning_remove_method():
        df = pd.read_csv('employees.csv')
        df.dropna(inplace=True)
        print("\n Dataframe after dropping row with missing values:")
        pd.set_option('display.max_rows', None)  # Show all rows
        pd.set_option('display.max_columns', None)  # Show all columns
        print(df)

# data_cleaning_remove_method()

def data_cleaning_fill_method():
    df = pd.read_csv('employees.csv')
    df.fillna(df.mean(),inplace=True)
    print("\n Dataframe after filling missing numerical values with mean:")
    pd.set_option('display.max_rows', None)  # Show all rows
    pd.set_option('display.max_columns', None)  # Show all columns
    print(df)

# data_cleaning_remove_method()

def data_cleaning_forward_fill_method():
    df = pd.read_csv('employees.csv')
    df.fillna(method='ffill', inplace=True)
    print("\n Dataframe after filling missing numerical values with forward filling approach (ffill):")
    pd.set_option('display.max_rows', None)  # Show all rows
    pd.set_option('display.max_columns', None)  # Show all columns
    print(df)

# data_cleaning_forward_fill_method()

def data_duplicates_count():
    df = pd.read_csv('employees.csv')
    duplicates = df.duplicated()  # Check for duplicate rows (returns a boolean Series)
    duplicate_rows = duplicates.sum() # Show only duplicated rows
    # duplicate_rows = df[df.duplicated(subset=['First Name', 'Team'])] # Check for duplicates based on 'First Name' and 'Team'
    print("Duplicate Rows : " , duplicate_rows)

#data_duplicates_count()

'''    
def data_duplicates_specific_column():
    df = pd.read_csv('employees.csv')
    duplicate_rows = df[df.duplicated(subset=['First Name'])] # Check for duplicates based on 'First Name' and 'Team'
    sum_of_duplicated_rows = duplicate_rows().sum()
    print("Total duplicates rows: " , sum_of_duplicated_rows)
    print("Duplicate Rows : ", duplicate_rows)

data_duplicates_specific_column()
'''

def data_duplicates_remove_fc():
    df = pd.read_csv('employees.csv')
    df_no_duplicates = df.drop_duplicates() # Remove duplicate rows (keep the first occurrence)
    print("\n Dataframe after removing duplicates values with first occurrence:")
    print(df_no_duplicates)

#data_duplicates_remove_fc()

def data_duplicates_remove_lc():
    df = pd.read_csv('employees.csv')
    df_no_duplicates = df.drop_duplicates(keep='last') # OR keep the last occurrence
    print("\n Dataframe after removing duplicates values with last occurrence:")
    print(df_no_duplicates)

#data_duplicates_remove_lc()

def standardizing_data_formate():
    df = pd.read_csv('employees.csv')
    # Remove leading/trailing spaces, convert to lowercase, remove double spaces
    df['First_Name_cleaned'] = (
        df['First Name']
        .str.strip()  # remove extra spaces
        .str.lower()  # make all lowercase
        .str.replace(r'\s+', ' ', regex=True)  # replace multiple spaces with one
    )
    print(df)

standardizing_data_formate()