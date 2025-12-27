import pandas as pd

# Generate sample expense data
data = {
    'description': [
        'Coffee at Starbucks',
        'Monthly internet bill',
        'New shoes from Nike',
        'Uber ride to office',
        'Groceries at Walmart',
        'Dinner with friends',
        'Electricity bill',
        'Gas for car',
        'Subscription to Netflix',
        'Pharmacy purchase',
        'Rent payment',
        'Lunch meeting',
        'Train ticket',
        'Shopping at Zara',
        'Phone bill'
    ],
    'category': [
        'Food',
        'Utilities',
        'Shopping',
        'Transportation',
        'Food',
        'Food',
        'Utilities',
        'Transportation',
        'Entertainment',
        'Healthcare',
        'Housing',
        'Food',
        'Transportation',
        'Shopping',
        'Utilities'
    ]
}

df_expenses_sample = pd.DataFrame(data)

# Save the sample data to a CSV file that the next cell can read
df_expenses_sample.to_csv('expense_data.csv', index=False)

print("Generated a sample 'expense_data.csv' file.")

# Now, read the generated sample data into df_expenses
df_expenses = pd.read_csv('expense_data.csv')

print("\nFirst 5 rows of the expense DataFrame:")
print(df_expenses.head())

print("\nDataFrame Information for expense data:")
df_expenses.info()



