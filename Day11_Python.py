import pandas as pd

df = pd.read_excel(r'C:\Users\balaji\Desktop\Datasheet.xlsx')
print(df)
Finaldata = pd.DataFrame(df, columns=['Products', 'Price'])
print(Finaldata)


