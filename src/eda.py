import pandas as pd
import numpy as np

def perform_eda(file_path):
    df = pd.read_csv(file_path)
    
    print("Data Shape:", df.shape)
    print("\nData Types:\n", df.dtypes)
    print("\nMissing Values:\n", df.isnull().sum())
    
    print("\nDescriptive Statistics:\n", df.describe())
    
    # Loss Ratio
    df['LossRatio'] = df['TotalClaims'] / df['TotalPremium']
    print("\nOverall Loss Ratio:", df['LossRatio'].mean())
    
    # Group by Province
    print("\nLoss Ratio by Province:\n", df.groupby('Province')['LossRatio'].mean())
    
    return df

if __name__ == "__main__":
    perform_eda('data/insurance_claims.csv')
