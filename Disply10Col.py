import pandas as pd
sample_data = pd.read_csv('employee-compensation.csv')
print(sample_data.iloc[:10, :10])
