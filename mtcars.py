import pandas as pd
df = pd.read_csv("C:\\Users\\mfite\\Documents\\mtcars.csv")
# print(df[['hp','model']].describe().unstack())
print(df.isna().any())