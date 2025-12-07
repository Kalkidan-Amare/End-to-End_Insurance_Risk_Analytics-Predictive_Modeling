import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta


def generate_data(num_rows=1000):
    np.random.seed(42)

    # Helper to generate dates
    def random_date(start, end):
        return start + timedelta(
            seconds=random.randint(0, int((end - start).total_seconds())))

    start_date = datetime(2014, 2, 1)
    end_date = datetime(2015, 8, 31)

    data = {
        'UnderwrittenCoverID': range(1, num_rows + 1),
        'PolicyID': np.random.randint(1000, 9999, num_rows),
        'TransactionMonth': [random_date(start_date, end_date) for _ in range(num_rows)],
        'IsVATRegistered': np.random.choice([True, False], num_rows),
        'Citizenship': np.random.choice(['South Africa', 'Other'], num_rows),
        'LegalType': np.random.choice(['Close Corporation', 'Sole Proprietor'], num_rows),
        'Title': np.random.choice(['Mr', 'Ms', 'Mrs', 'Dr'], num_rows),
        'Language': np.random.choice(['English', 'Afrikaans', 'Zulu'], num_rows),
        'Bank': np.random.choice(['Standard Bank', 'FNB', 'Absa'], num_rows),
        'AccountType': np.random.choice(['Current', 'Savings'], num_rows),
        'MaritalStatus': np.random.choice(['Married', 'Single', 'Divorced'], num_rows),
        'Gender': np.random.choice(['Male', 'Female'], num_rows),
        'Country': ['South Africa'] * num_rows,
        'Province': np.random.choice(['Gauteng', 'Western Cape', 'KwaZulu-Natal', 'Eastern Cape'], num_rows),
        'PostalCode': np.random.randint(1000, 9999, num_rows),
        'MainCrestaZone': np.random.choice(['Zone A', 'Zone B'], num_rows),
        'SubCrestaZone': np.random.choice(['Sub Zone 1', 'Sub Zone 2'], num_rows),
        'ItemType': ['Vehicle'] * num_rows,
        'Mmcode': np.random.randint(10000, 99999, num_rows),
        'VehicleType': np.random.choice(['Passenger', 'Light Commercial'], num_rows),
        'RegistrationYear': np.random.randint(2000, 2015, num_rows),
        'Make': np.random.choice(['Toyota', 'Volkswagen', 'Ford', 'BMW'], num_rows),
        'Model': np.random.choice(['Corolla', 'Polo', 'Ranger', '3 Series'], num_rows),
        'Cylinders': np.random.randint(4, 8, num_rows),
        'Cubiccapacity': np.random.randint(1000, 3000, num_rows),
        'Kilowatts': np.random.randint(50, 200, num_rows),
        'Bodytype': np.random.choice(['Sedan', 'Hatchback', 'SUV'], num_rows),
        'NumberOfDoors': np.random.randint(2, 5, num_rows),
        'VehicleIntroDate': [random_date(datetime(2000, 1, 1), datetime(2014, 1, 1)) for _ in range(num_rows)],
        'CustomValueEstimate': np.random.uniform(50000, 500000, num_rows),
        'AlarmImmobiliser': np.random.choice([True, False], num_rows),
        'TrackingDevice': np.random.choice([True, False], num_rows),
        'CapitalOutstanding': np.random.uniform(0, 200000, num_rows),
        'NewVehicle': np.random.choice([True, False], num_rows),
        'WrittenOff': np.random.choice([True, False], num_rows, p=[0.05, 0.95]),
        'Rebuilt': np.random.choice([True, False], num_rows, p=[0.02, 0.98]),
        'Converted': np.random.choice([True, False], num_rows, p=[0.01, 0.99]),
        'CrossBorder': np.random.choice([True, False], num_rows, p=[0.01, 0.99]),
        'NumberOfVehiclesInFleet': np.random.randint(1, 5, num_rows),
        'SumInsured': np.random.uniform(50000, 500000, num_rows),
        'TermFrequency': ['Monthly'] * num_rows,
        'CalculatedPremiumPerTerm': np.random.uniform(500, 3000, num_rows),
        'ExcessSelected': np.random.uniform(0, 5000, num_rows),
        'CoverCategory': ['Comprehensive'] * num_rows,
        'CoverType': ['Own Damage'] * num_rows,
        'CoverGroup': ['Comprehensive'] * num_rows,
        'Section': ['Motor'] * num_rows,
        'Product': ['Car Insurance'] * num_rows,
        'StatutoryClass': ['Class A'] * num_rows,
        'StatutoryRiskType': ['Risk A'] * num_rows,
        'TotalPremium': np.random.uniform(500, 3500, num_rows),
        'TotalClaims': np.random.choice([0, np.random.uniform(1000, 50000)], num_rows, p=[0.8, 0.2])  # 20% claim rate
    }

    # Adjust TotalClaims to be 0 if it was selected as 0
    claims = []
    for _ in range(num_rows):
        if random.random() < 0.2:
            claims.append(np.random.uniform(1000, 50000))
        else:
            claims.append(0.0)
    data['TotalClaims'] = claims

    df = pd.DataFrame(data)
    df.to_csv('data/insurance_claims.csv', index=False)
    print("Data generated successfully at data/insurance_claims.csv")


if __name__ == "__main__":
    generate_data()
