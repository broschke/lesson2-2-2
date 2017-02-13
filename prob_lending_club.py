import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats

loansData = pd.read_csv('https://github.com/Thinkful-Ed/curric-data-001-data-sets/raw/master/loans/loansData.csv')

loansData.dropna(inplace=True)

data = [i.split(',') for i in loansData]
column_names = data[0] # this is the first row
data_rows = data[1::] # these are all the following rows of data
df = pd.DataFrame(data_rows, columns=column_names)

print(column_names)

# df.boxplot(column='Amount.Requested')
# plt.show()

# df.hist(column='Amount.Funded.By.Investors')
# plt.show()

# plt.figure()
# graph = stats.probplot(df['Amount.Funded.By.Investors'], dist="norm", plot=plt)
# plt.show()
