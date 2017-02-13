import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats

loansData = pd.read_csv('https://github.com/Thinkful-Ed/curric-data-001-data-sets/raw/master/loans/loansData.csv')

loansData.dropna(inplace=True)

loansData.boxplot(column='Amount.Requested')
plt.show()

loansData.hist(column='Amount.Requested')
plt.show()

plt.figure()
graph = stats.probplot(loansData['Amount.Requested'], dist="norm", plot=plt)
plt.show()


'''
Amount Requested data has a direct relationship with the amount founded data.
'''