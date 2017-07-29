import pandas as pd

s=pd.Series([0,1,4,9,16,25,36], name='squares')
print(s)
print(s.values)
print(s.index)
print(s[0])
print(s[2:4])
pop2014=pd.Series([100,99.3,95.5,93.5],index=['java','c','c++','python'])
print(pop2014)
print(pop2014.index)
print(pop2014[0])
print(pop2014['python'])
print(pop2014['c++':'python'])
print(pop2014.iloc[0:2])
print(pop2014.loc[:'c'])
pop2015=pd.Series({'java':100,'c++':99.4,'c':99.9,'python':96.5})
twoyr=pd.DataFrame({'2014':pop2014,'2015':pop2015})

twoyr['avg']=0.5*(twoyr['2014']+twoyr['2015'])
print(twoyr)


# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('pandas_simple.xlsx', engine='xlsxwriter')

# Convert the dataframe to an XlsxWriter Excel object.
twoyr.to_excel(writer, sheet_name='Sheet1')

# Close the Pandas Excel writer and output the Excel file.
writer.save()

