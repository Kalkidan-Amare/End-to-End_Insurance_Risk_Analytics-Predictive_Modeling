import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

def ab_testing(file_path):
    df = pd.read_csv(file_path)
    
    # Feature Engineering
    df['HasClaim'] = df['TotalClaims'] > 0
    df['Margin'] = df['TotalPremium'] - df['TotalClaims']
    
    results = []
    
    # 1. Risk differences across provinces (Chi-squared on HasClaim)
    # H0: No difference in claim frequency across provinces
    contingency_table = pd.crosstab(df['Province'], df['HasClaim'])
    chi2, p, dof, expected = stats.chi2_contingency(contingency_table)
    results.append(f"Hypothesis 1: Risk differences across provinces (Claim Frequency)")
    results.append(f"Chi2: {chi2}, p-value: {p}")
    if p < 0.05:
        results.append("Result: Reject Null Hypothesis (Significant difference)")
    else:
        results.append("Result: Fail to Reject Null Hypothesis (No significant difference)")
    results.append("-" * 30)

    # 2. Risk differences between zipcodes (PostalCode)
    # Since there are many zipcodes, we might group them or just test top ones?
    # Or use ANOVA if we treat risk as continuous (TotalClaims)?
    # Let's use ANOVA on TotalClaims for ZipCodes
    # H0: No difference in TotalClaims mean across ZipCodes
    # We'll filter for top 10 zipcodes to make it manageable or just run it
    top_zips = df['PostalCode'].value_counts().head(20).index
    df_top_zips = df[df['PostalCode'].isin(top_zips)]
    groups = [group['TotalClaims'].values for name, group in df_top_zips.groupby('PostalCode')]
    f_val, p_val = stats.f_oneway(*groups)
    results.append(f"Hypothesis 2: Risk differences between zipcodes (TotalClaims ANOVA)")
    results.append(f"F-stat: {f_val}, p-value: {p_val}")
    if p_val < 0.05:
        results.append("Result: Reject Null Hypothesis")
    else:
        results.append("Result: Fail to Reject Null Hypothesis")
    results.append("-" * 30)

    # 3. Margin difference between zipcodes
    # H0: No difference in Margin mean across ZipCodes
    groups_margin = [group['Margin'].values for name, group in df_top_zips.groupby('PostalCode')]
    f_val_m, p_val_m = stats.f_oneway(*groups_margin)
    results.append(f"Hypothesis 3: Margin differences between zipcodes (ANOVA)")
    results.append(f"F-stat: {f_val_m}, p-value: {p_val_m}")
    if p_val_m < 0.05:
        results.append("Result: Reject Null Hypothesis")
    else:
        results.append("Result: Fail to Reject Null Hypothesis")
    results.append("-" * 30)

    # 4. Risk difference between Women and Men
    # T-test on TotalClaims
    # H0: No difference in TotalClaims between Men and Women
    group_male = df[df['Gender'] == 'Male']['TotalClaims']
    group_female = df[df['Gender'] == 'Female']['TotalClaims']
    t_stat, p_val_g = stats.ttest_ind(group_male, group_female, equal_var=False)
    results.append(f"Hypothesis 4: Risk differences between Women and Men (T-test on TotalClaims)")
    results.append(f"T-stat: {t_stat}, p-value: {p_val_g}")
    if p_val_g < 0.05:
        results.append("Result: Reject Null Hypothesis")
    else:
        results.append("Result: Fail to Reject Null Hypothesis")
    results.append("-" * 30)

    # Save results
    with open('notebooks/ab_test_results.txt', 'w') as f:
        f.write("\n".join(results))
    
    print("\n".join(results))

if __name__ == "__main__":
    ab_testing('data/insurance_claims.csv')
