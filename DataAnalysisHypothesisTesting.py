import pandas as pd
import scipy.stats as stats
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def hypothesis_testing():
    # Load the CSV file
    df = pd.read_csv('employees.csv')
    df.dropna(inplace=True)

    # Grouping salaries by Team
    teams = df['Team'].unique()
    salary_groups = [df[df['Team'] == team]['Salary'] for team in teams]

    # Performing ANOVA (to check if at least one team differs significantly)
    anova_result = stats.f_oneway(*salary_groups)
    print(f"ANOVA Test Results: F-statistic = {anova_result.statistic}, p-value = {anova_result.pvalue}")

    # Conclusion
    if anova_result.pvalue < 0.05:
        print("Reject H₀: There is a significant difference in salaries among teams.")
    else: print("There is no significant difference in 'Salary' among 'Team'")

# hypothesis_testing()


# Independent T-Test (Salary by Gender)
def independent_t_test():
    df = pd.read_csv('employees.csv')
    df.dropna(inplace=True)

    # Boxplot for Salary Distribution by Gender
    sns.boxplot(x='Gender', y='Salary', data=df)
    plt.title('Salary Distribution by Gender')
    plt.show()

    # Independent T-Test
    male_salary = df[df['Gender'] == 'Male']['Salary']
    female_salary = df[df['Gender'] == 'Female']['Salary']

    t_stat, p_value = stats.ttest_ind(male_salary, female_salary)
    print(f"T-Test Results: t-statistic = {t_stat}, p-value = {p_value}")

    if p_value < 0.05:
        print("Reject H₀: There is a significant difference in salaries by gender.")
    else:
        print("Fail to reject H₀: No significant difference in salaries by gender.")

# independent_t_test()


# Independent T-Test (Salary by Team)
def independent_t_test1():
    df = pd.read_csv('employees.csv')
    df.dropna(inplace=True)

    # Boxplot for Salary Distribution by Gender
    sns.boxplot(x='Team', y='Salary', data=df)
    plt.title('Salary Distribution by Team')
    plt.show()

    # Independent T-Test
    marketing_salary = df[df['Team'] == 'Marketing']['Salary']
    finance_salary = df[df['Team'] == 'Finance']['Salary']
    client_services_salary = df[df['Team'] == 'Client Services']['Salary']
    legal_salary = df[df['Team'] == 'Legal']['Salary']
    product_salary = df[df['Team'] == 'Product']['Salary']
    engineering_salary = df[df['Team'] == 'Engineering']['Salary']
    business_development_salary = df[df['Team'] == 'Business Development']['Salary']
    human_resources_salary = df[df['Team'] == 'Human Resources']['Salary']
    sales_salary = df[df['Team'] == 'Sales']['Salary']
    distribution_salary = df[df['Team'] == 'Distribution']['Salary']


    t_stat, p_value = stats.ttest_ind(marketing_salary, finance_salary, client_services_salary, legal_salary,
                                      product_salary, engineering_salary, business_development_salary,
                                      human_resources_salary, sales_salary, distribution_salary)
    print(f"T-Test Results: t-statistic = {t_stat}, p-value = {p_value}")

    if p_value < 0.05:
        print("Reject H₀: There is a significant difference in salaries by gender.")
    else:
        print("Fail to reject H₀: No significant difference in salaries by gender.")

# independent_t_test1()

# Chi-Square Test (Team vs Gender)
def chi_square_test():


    df = pd.read_csv('employees.csv')
    df.dropna(inplace=True)

    # Creating contingency table
    contingency_table = pd.crosstab(df['Team'], df['Gender'])

    # Heatmap for visualization
    sns.heatmap(contingency_table, annot=True, fmt='d', cmap='coolwarm')
    plt.title('Gender Distribution Across Teams')
    plt.show()

    # Performing Chi-Square Test
    chi2, p, dof, expected = stats.chi2_contingency(contingency_table)
    print(f"Chi-Square Results: Chi2 Statistic = {chi2}, p-value = {p}")

    if p < 0.05:
        print("Reject H₀: There is a relationship between team and gender.")
    else:
        print("Fail to reject H₀: No significant relationship between team and gender.")

# chi_square_test()

# ANOVA (Salary Across Teams)
def anova_test():

    df = pd.read_csv('employees.csv')
    df.dropna(inplace=True)

    # Boxplot for Salary by Team
    sns.boxplot(x='Team', y='Salary', data=df)
    plt.title('Salary Differences Across Teams')
    plt.show()

    # ANOVA Test
    teams = df['Team'].unique()
    salary_groups = [df[df['Team'] == team]['Salary'] for team in teams]
    anova_result = stats.f_oneway(*salary_groups)

    print(f"ANOVA Test Results: F-statistic = {anova_result.statistic}, p-value = {anova_result.pvalue}")

    if anova_result.pvalue < 0.05:
        print("Reject H₀: Salaries differ significantly across teams.")
    else:
        print("Fail to reject H₀: No significant difference in salaries across teams.")

# anova_test()

# Correlation Test (Salary vs Bonus %)
def correlation_test():

    df = pd.read_csv('employees.csv')
    df.dropna(inplace=True)

    # Scatter Plot for Salary vs Bonus
    sns.scatterplot(x='Bonus %', y='Salary', data=df)
    plt.title('Correlation Between Bonus % and Salary')
    plt.show()

    # Pearson Correlation
    corr, p = stats.pearsonr(df['Bonus %'], df['Salary'])
    print(f"Correlation Results: Pearson Correlation = {corr}, p-value = {p}")

    if p < 0.05:
        print("Reject H₀: There is a significant correlation between salary and bonus.")
    else:
        print("Fail to reject H₀: No significant correlation.")

# correlation_test()

# Non-Parametric Test (Mann-Whitney U Test for Salary by Gender)
def non_parametric_test():

    df = pd.read_csv('employees.csv')
    df.dropna(inplace=True)

    # Violin Plot for Salary Distribution
    sns.violinplot(x='Gender', y='Salary', data=df)
    plt.title('Salary Distribution by Gender')
    plt.show()

    # Independent T-Test
    male_salary = df[df['Gender'] == 'Male']['Salary']
    female_salary = df[df['Gender'] == 'Female']['Salary']

    # Mann-Whitney U Test (for non-normal salary distribution)
    u_stat, p_value = stats.mannwhitneyu(male_salary, female_salary)
    print(f"Mann-Whitney U Test Results: U-statistic = {u_stat}, p-value = {p_value}")

    if p_value < 0.05:
        print("Reject H₀: There is a significant difference in salaries by gender.")
    else:
        print("Fail to reject H₀: No significant difference in salaries by gender.")


# non_parametric_test()