df.to_csv("C:/Users\GEETANJALI JENA/Downloads/python Dataset 2.csv", index-False)

27

28 Show a message

29 print("Dataset cleaned and saved as 'cleaned dataset.csv")

30 print(df)

31 print("Basic Statistics:")


32 print(df.describe())

33

34 35 sb.set(style="whitegrid")

36 (a) Histogram - Margin Percentage Distribution

37 plt.figure(figsize-(8,4))

38 sb.histplot(df('margin percentage'), bins 20, kde True, colors'block')

39 plt.title("Distribution of Hargin Percentage")

40 plt.xlabel("Nargin Percentage")

41 plt.ylabel("Mamber of Candidates")

42 plt.tight layout()

df

#1. Drop duplicate rows

df.drop duplicates (inplace=True)

82. Handle missing values

Fill 'month' with mode (most common value)

df['month']…




