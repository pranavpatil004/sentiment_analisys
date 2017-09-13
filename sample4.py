import pandas as pd

xl = pd.ExcelFile("voc.xlsx")
df = xl.parse("Sheet1")
df = df.sort(columns="Header Row")

writer = pd.ExcelWriter('output.xlsx')
df.to_excel(writer,sheet_name='Sheet1',columns=["Header Row"],index=False)
writer.save()