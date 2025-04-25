import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import squarify

# Load your CSV file
df = pd.read_csv('employees.csv')
df = df.drop_duplicates()
df.dropna(inplace=True)
# pd.set_option('display.max_rows', None)
# print(df)
teams = df['Team'].unique()

print("-------------- Welcome to Employee Data --------------")
a = input("\tPress keys as you wish for "
          "\n1. You want to know total number of Teams in this data "
          "\n2. You want know all names of Teams in this data"
          "\n3. If you want to complete details of any Team "
          "\n4. Team-wise Gender Count (Pivot Table)"
          "\n5. Average salary per Team"
          "\n6. You want data visualization \n")

b = int(a)

match b:
    case 1:
        total_teams = len(df['Team'].unique())
        print("Total number of Teams:", total_teams)

    case 2:
        print(df['Team'].unique())

    case 3:
        c = input(" Please select Team : \n "
                  "1.Marketing  2.Finance  3.Client Services  4.Legal  5.Product  6.Engineering  7.Business Development  "
                  "8.Human Resource  9.Sales  10.Distribution \n")
        index = int(c) - 1
        team_count = len(df[df['Team'] == teams[index]])
        print(f"Number of employees in {teams[index]} Team : {team_count}")
        df_team = df[df['Team'] == teams[index]]
        gender_counts = df_team.groupby(['Team', 'Gender']).size().unstack(fill_value=0)
        print(gender_counts)
        print("-----------------Details as below-------------------")
        pd.set_option('display.max_rows', None)
        print(df_team)
        print("\n")

    case 4:
        print("Team-wise Gender Count (Pivot Table)")
        gender_counts = df.groupby(['Team', 'Gender']).size().unstack(fill_value=0)
        print(gender_counts)

    case 5:
        print("Average salary per team")
        team_stats = df.groupby('Team').agg({
            'Salary': ['mean', 'min', 'max'],
            'Bonus %': ['mean', 'std']})
        print(team_stats)
    case 6:
        d = input(" Enter type of chart you want :"
                  "1. Bar Chart  2.Line Chart  3.Histogram  4.BoxPlot  5.ScatterPlot  6.Heatmap  7.PieChart  8.Treemap\n")
        e = int(d)
        match e:
            case 1:
                column1 = input(
                    "You choose 'Bar Chart' then please enter first column name in between you want to see the graph \n")
                column2 = input("Enter second column name:\n")
                plt.figure(figsize=(10, 6))
                plt.bar(df[column1], df[column2], color='lightgreen', edgecolor='black')
                plt.title(f'{column2} by Team')
                plt.xlabel(column1)
                plt.ylabel(column2)
                plt.xticks(rotation=45)
                plt.grid(axis='y', linestyle='--', alpha=0.5)
                plt.tight_layout()
                plt.show()

            case 2:
                column1 = input(
                    "You choose 'Line Chart' then please enter first numerical column name in between you want to see the graph \n")
                column2 = input("Enter second numerical column name:\n")
                plt.figure(figsize=(10, 6))
                plt.plot(df[column1], df[column2], marker='o', linestyle='-', color='green')
                plt.title(f'{column1} vs {column2}')
                plt.xlabel(column1)
                plt.ylabel(column2)
                plt.grid(True, linestyle='--', alpha=0.5)
                plt.tight_layout()
                plt.show()

            case 3:
                plt.figure(figsize=(10, 6))
                column1 = input(
                    "You choose 'Histogram' then please enter first column name in between you want to see the graph \n")
                column2 = input("Enter second column name:\n")
                plt.hist(df[column1], bins=20, alpha=0.6, label='Salary', color='skyblue', edgecolor='black')
                plt.hist(df[column2], bins=20, alpha=0.6, label='Bonus %', color='orange', edgecolor='black')
                plt.title(f'Histogram: {column1} vs {column2}')
                plt.xlabel('Value')
                plt.ylabel('Frequency')
                plt.legend()
                plt.grid(True, linestyle='--', alpha=0.5)
                plt.tight_layout()
                plt.show()

            case 4:
                column1 = input(
                    "You choose 'BoxPlot' then please enter first column name in between you want to see the graph \n")
                column2 = input("Enter second column name:\n")
                plt.figure(figsize=(8, 6))
                plt.boxplot([df[column1], df[column2]], labels=[column1, column2], patch_artist=True)
                plt.title(f'Boxplot of {column1} and {column2}')
                plt.ylabel('Value')
                plt.grid(True, linestyle='--', alpha=0.5)
                plt.tight_layout()
                plt.show()

            case 5:
                column1 = input(
                    "You choose 'ScatterPlot' then please enter first column name in between you want to see the graph \n")
                column2 = input("Enter second column name:\n")
                plt.figure(figsize=(8, 6))
                plt.scatter(df[column1], df[column2], color='teal', alpha=0.7, edgecolor='black')

                plt.title(f'Scatter Plot: {column2} vs {column1}')
                plt.xlabel(column2)
                plt.ylabel(column1)
                plt.grid(True, linestyle='--', alpha=0.5)
                plt.tight_layout()
                plt.show()

            case 6:
                print("You choose 'Heatmap'")

                numeric_cols = ['Salary', 'Bonus %']

                # Create correlation matrix
                corr_matrix = df[numeric_cols].corr()

                # Plot heatmap
                plt.figure(figsize=(10, 6))
                sns.heatmap(corr_matrix, annot=True, cmap='YlGnBu', fmt=".2f", linewidths=0.5)

                plt.title('Correlation Heatmap of Employee Features')
                plt.tight_layout()
                plt.show()

            case 7:

                team_counts = df['Team'].value_counts()
                # Plot pie chart
                plt.figure(figsize=(8, 8))
                plt.pie(team_counts, labels=team_counts.index, autopct='%1.1f%%', startangle=140,
                        colors=plt.cm.Set3.colors)
                plt.title('Employee Distribution by Team')
                plt.axis('equal')  # Equal aspect ratio makes the pie a circle
                plt.tight_layout()
                plt.show()

                # For gender distribution
                gender_counts = df['Gender'].value_counts()

                plt.figure(figsize=(6, 6))
                plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%',
                        colors=['#66b3ff', '#ff9999'], startangle=90)

                plt.title('Gender Distribution of Employees')
                plt.axis('equal')
                plt.tight_layout()
                plt.show()

            case 8:
                # Count employees per team
                team_counts = df['Team'].value_counts()

                # Plot treemap
                plt.figure(figsize=(10, 6))
                squarify.plot(sizes=team_counts.values, label=team_counts.index, alpha=0.8, color=plt.cm.Set3.colors)
                plt.title('Employee Distribution by Team (Treemap)')
                plt.axis('off')
                plt.tight_layout()
                plt.show()

                # Group by Team and sum Salary
                team_salary = df.groupby('Team')['Salary'].sum().sort_values(ascending=False)

                # Plot treemap
                plt.figure(figsize=(10, 6))
                squarify.plot(sizes=team_salary.values, label=team_salary.index, alpha=0.8,
                              color=plt.cm.Pastel1.colors)

                plt.title('Total Salary Distribution by Team (Treemap)')
                plt.axis('off')
                plt.tight_layout()
                plt.show()

            case _:
                print("please enter correct value")

    case _:
        print("please enter correct value")