import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os


def create_visualizations(file_path):
    df = pd.read_csv(file_path)

    if not os.path.exists('notebooks/figures'):
        os.makedirs('notebooks/figures')

    # 1. Distribution of Total Premium
    plt.figure(figsize=(10, 6))
    sns.histplot(df['TotalPremium'], kde=True)
    plt.title('Distribution of Total Premium')
    plt.savefig('notebooks/figures/premium_distribution.png')
    plt.close()

    # 2. Total Claims by Province
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='Province', y='TotalClaims', data=df)
    plt.title('Total Claims by Province')
    plt.savefig('notebooks/figures/claims_by_province.png')
    plt.close()

    # 3. Correlation Matrix
    plt.figure(figsize=(12, 8))
    numeric_df = df.select_dtypes(include=['float64', 'int64'])
    sns.heatmap(numeric_df.corr(), annot=False, cmap='coolwarm')
    plt.title('Correlation Matrix')
    plt.savefig('notebooks/figures/correlation_matrix.png')
    plt.close()

    print("Visualizations saved to notebooks/figures/")


if __name__ == "__main__":
    create_visualizations('data/insurance_claims.csv')
