import pandas as pd

df = pd.read_csv("C:\\Users\\mfite\\Documents\\school_data.csv")
# print(df[['reduced_lunch', 'school_rating']].groupby(['school_rating']).describe().unstack())
print(df[['reduced_lunch', 'school_rating']].corr())
