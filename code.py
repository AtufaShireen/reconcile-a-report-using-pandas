# --------------

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Code starts here
path
df=pd.read_csv(path)
df['state']=df['state'].apply(lambda x:x.lower())
df['total']=df['Jan']+df['Feb']+df['Mar']
sum_row = df[["Jan", "Feb", "Mar", "total"]].sum()
print(sum_row)
df_final=df.append(sum_row,ignore_index=True)
print(df_final.head())
# Code ends here


# --------------
import requests

# Code starts here
url='https://en.wikipedia.org/wiki/List_of_U.S._state_abbreviations'
response=requests.get(url)
df1=pd.read_html(response.content)[0]
df1=df1.iloc[11:,]
print('newww')
print(df1.head())
print('column name here')
df1.rename(columns=df1.iloc[0],inplace=True)
df1.drop(df1.index[0],inplace=True)
print(list(df1.columns.values))
df1['United States of America']=df1['United States of America'].apply(lambda x:x.strip())
print(df1['United States of America'])
# Code ends here


# --------------
df1['United States of America'] = df1['United States of America'].astype(str).apply(lambda x: x.lower())
df1['US'] = df1['US'].astype(str)

# Code starts here
mapping=df1.set_index('United States of America')['US'].to_dict()
print(mapping)
# df_final.insert(6, 'abbr')
df_final['abbr']=df_final['state'].map(mapping)

# Code ends here


# --------------
# Code stars here
df_mississipi=df_final[df_final['state'] == 'mississipi'].replace(np.nan, 'MS')
print(df_mississipi.head())
df_final.replace(df_final.iloc[6], df_mississipi, inplace=True)

df_tenessee=df_final[df_final['state'] == 'tenessee'].replace(np.nan, 'TN')
print(df_tenessee)
df_final.replace(df_final.iloc[10], df_tenessee, inplace=True)
# Code ends here


# --------------
# Code starts here

# Calculate the total amount
df_sub=df_final[["abbr", "Jan", "Feb", "Mar", "total"]].groupby("abbr").sum()
print(df_sub.shape)
# Add the $ symbol
formatted_df = df_sub.applymap(lambda x: "${:,.0f}".format(x))

# Code ends here


# --------------
# Code starts here
sum_row=df[["Jan", "Feb", "Mar","total"]].sum()
df_sub_sum=sum_row.transpose()
df_sub_sum=df_sub_sum.apply(lambda x:'$'+str(x))
print(sum_row.head())
final_table=formatted_df.append(df_sub_sum,ignore_index=True)
print(final_table.tail())
final_table.rename( index={'0':'Total'} )
# Code ends here


# --------------
# Code starts here
df_sub['total']=df['Jan']+df['Feb']+df['Mar']
df_sub['total'].plot.pie()
# Code ends here


