import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

def statistical_data_analysis_normal_distribution():
    df = pd.read_csv('employees.csv')

    # Choose the numeric column to analyze
    column_name = 'Salary'
    data = df[column_name].dropna()

    # Calculate basic stats
    mean = np.mean(data)
    std = np.std(data)

    # Create the Normal Distribution curve
    x = np.linspace(min(data), max(data), 1000)
    normal_curve = (1 / (std * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mean) / std) ** 2)

    # Plot Histogram + Normal Distribution curve
    plt.figure(figsize=(10, 6))
    plt.hist(data, bins=30, density=True, alpha=0.6, color='skyblue', label='Histogram')
    plt.plot(x, normal_curve, color='red', linewidth=2, label='Normal Distribution')

    # Annotate
    plt.axvline(mean, color='black', linestyle='--', label=f'Mean: {mean:.2f}')
    plt.axvline(mean + std, color='green', linestyle='--', label=f'+1 Std: {mean + std:.2f}')
    plt.axvline(mean - std, color='green', linestyle='--', label=f'-1 Std: {mean - std:.2f}')

    # Labels and Title
    plt.title(f'Normal Distribution of {column_name.capitalize()}')
    plt.xlabel(column_name.capitalize())
    plt.ylabel('Bonus %')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# statistical_data_analysis_normal_distribution()

def statistical_data_analysis_binomial_distribution():

    df = pd.read_csv('employees.csv')

    df['high_bonus'] = (df['Bonus %'] > 10).astype(int)  # Creating a binary column: 1 if bonus > 10%, else 0
    binary_col = 'high_bonus'

    n = len(df)  # total number of trials
    k = df[binary_col].sum()  # number of successes (1s)
    p = k / n  # estimated probability of success

    print(f"Total Trials: {n}, Successes: {k}, Estimated Probability: {p:.2f}")

    x = np.arange(0, n + 1)    # Creating x range (0 to n) and PMF
    stats_pmf = stats.binom.pmf(x, n, p)

    # Plot PMF (Probability Mass Function)
    plt.figure(figsize=(10, 6))
    plt.plot(x, stats_pmf, color='red', label='Binomial PMF')
    plt.fill_between(x, stats_pmf, color='skyblue', alpha=0.6)
    plt.title(f'Binomial Distribution - {binary_col} (n={n}, p={p:.2f})')
    plt.xlabel('Number of Successes')
    plt.ylabel('Probability')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# statistical_data_analysis_binomial_distribution()

def statistical_data_analysis_poisson_distribution():
    df = pd.read_csv('employees.csv')

    # Simulate event counts using Poisson based on a fixed lambda
    df['bonus_events'] = np.random.poisson(lam=3, size=len(df))  # arbitrary lambda=3 analyze df['bonus_events'] using Poisson tools

    bonus_col = 'Bonus %'  # Use 'Bonus %' column
    lambda_bonus = df[bonus_col].mean()

    print(f"Mean Bonus % (used as λ): {lambda_bonus:.2f}")

    df['bonus_events'] = np.random.poisson(lam=lambda_bonus, size=len(df)) # Simulate Poisson-distributed bonus events for each employee

    k = np.arange(0, df['bonus_events'].max() + 1) # Plot Poisson PMF for this lambda
    poisson_pmf = stats.poisson.pmf(k, mu=lambda_bonus)

    plt.figure(figsize=(10, 6))
    plt.bar(k, poisson_pmf, color='cornflowerblue', edgecolor='black', label='Poisson PMF')
    plt.title(f'Poisson Distribution Based on Bonus % (λ = {lambda_bonus:.2f})')
    plt.xlabel('Number of Simulated Bonus Events')
    plt.ylabel('Probability')
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend()
    plt.tight_layout()
    plt.show()

    # Plot histogram of simulated 'bonus_events'
    plt.figure(figsize=(10, 6))
    plt.hist(df['bonus_events'], bins=range(0, df['bonus_events'].max() + 2), color='orange', edgecolor='black')
    plt.title('Histogram of Simulated Bonus Events')
    plt.xlabel('Bonus Events Count')
    plt.ylabel('Number of Employees')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# statistical_data_analysis_poisson_distribution()

def statistical_data_analysis_confidence_interval():
    df = pd.read_csv('employees.csv')

    df_cleaned = df.dropna(subset=['Salary']) # Drop rows where Salary is NaN
    print(f"Valid Salary entries: {df_cleaned['Salary'].count()}")  # Check how many valid values we have now

    cols = ['Salary', 'Bonus %']

    # Function to calculate CI
    def confidence_interval(series, confidence=0.95):
        n = len(series)
        mean = np.mean(series)
        std_err = stats.sem(series)  # Standard Error = std / sqrt(n)
        margin = std_err * stats.t.ppf((1 + confidence) / 2.0, df=n - 1)
        return mean, mean - margin, mean + margin

    # Print CI for each column
    for col in cols:
        mean, lower, upper = confidence_interval(df_cleaned[col])
        print(f"\n📈 {col} — 95% Confidence Interval:")
        print(f"Mean: {mean:.2f}")
        print(f"Interval: [{lower:.2f}, {upper:.2f}]")

    # visualize the confidence interval
    means = []
    lowers = []
    uppers = []

    for col in cols:
        mean, lower, upper = confidence_interval(df[col])
        means.append(mean)
        lowers.append(lower)
        uppers.append(upper)

    # x_pos = np.arrange(len(cols))
    error = [np.array(means) - np.array(lowers), np.array(uppers) - np.array(means)]

    plt.figure(figsize=(8, 5))
    plt.bar(cols, means, yerr=error, capsize=10, color='skyblue', edgecolor='black')
    plt.ylabel('Mean Value with 95% CI')
    plt.title('Confidence Intervals for Salary & Bonus %')
    plt.grid(True, axis='y', linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.show()

statistical_data_analysis_confidence_interval()