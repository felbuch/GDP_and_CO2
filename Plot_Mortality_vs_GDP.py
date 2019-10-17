import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv("https://media.githubusercontent.com/media/nickeubank/MIDS_Data/master/World_Development_Indicators/wdi_small_tidy_2015.csv")

data = data.loc[:,['Mortality rate, infant (per 1,000 live births)','GDP per capita (constant 2010 US$)','Country Name']]
plt.scatter(data.loc[:,'GDP per capita (constant 2010 US$)'],data.loc[:,'Mortality rate, infant (per 1,000 live births)'])
plt.xlabel("GDP per capita (constant 2010 US$)")
plt.ylabel("Mortality rate, infant (per 1,000 live births)")
plt.show()

