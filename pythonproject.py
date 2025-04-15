import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb

df = pd.read_csv("C:/Users/GEETANJALI JENA/Downloads/python Dataset 2.csv")

# 1. Drop duplicate rows
df.drop_duplicates(inplace=True)

# 2. Handle missing values

# Fill 'month' with mode (most common value)
df['month'].fillna(df['month'].mode()[0], inplace=True)

# Fill 'candidate_type', 'sex', 'party' with 'Unknown'
df['candidate_type'].fillna('Unknown', inplace=True)
df['sex'].fillna('Unknown', inplace=True)
df['party'].fillna('Unknown', inplace=True)

# Fill 'vote_share_percentage' and 'margin_percentage' with 0 (or you can use mean if preferred)
df['vote_share_percentage'].fillna(0, inplace=True)
df['margin_percentage'].fillna(0, inplace=True)

# Save the cleaned data (optional)
df.to_csv("C:/Users\GEETANJALI JENA/Downloads/python Dataset 2.csv", index=False)

# Show a message
print("Dataset cleaned and saved as 'cleaned_dataset.csv'")
print(df)
print("Basic Statistics:")
print(df.describe())


sb.set(style="whitegrid")
#(a) Histogram – Margin Percentage Distribution
plt.figure(figsize=(8,4))
sb.histplot(df['margin_percentage'], bins=20, kde=True, color='black')
plt.title("Distribution of Margin Percentage")
plt.xlabel("Margin Percentage")
plt.ylabel("Number of Candidates")
plt.tight_layout()
plt.show()

#(b) Pie Chart – Candidate Gender Proportion
gender_counts = df['sex'].value_counts()
plt.figure(figsize=(8,8))
plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=90, colors=sb.color_palette('pastel'))
plt.title("Gender Proportion of Candidates")
plt.axis('equal')
plt.tight_layout()
plt.show()

#(c) Scatter Plot – Valid Votes vs Turnout Percentage
plt.figure(figsize=(8,4))
sb.scatterplot(x='valid_votes', y='turnout_percentage', hue='sex', data=df, palette='Dark2', alpha=0.7)
plt.title("Valid Votes vs Turnout Percentage by Gender")
plt.xlabel("Valid Votes")
plt.ylabel("Turnout (%)")
plt.legend(title='Gender')
plt.tight_layout()
plt.show()

#(d) Line Plot – Top 10 Candidates by Votes
top_candidates = df.sort_values(by='votes', ascending=False).head(10)
plt.figure(figsize=(8,4))
sb.lineplot(x='candidate_name', y='votes', data=top_candidates, marker='o', sort=False, color='darkblue')
plt.xticks(rotation=45)
plt.title("Top 10 Candidates by Vote Count")
plt.xlabel("Candidate")
plt.ylabel("Votes")
plt.tight_layout()
plt.show()

#(e) Bar Plot – Average Vote Share per Party (Top 10)
top_parties_by_count = df['party'].value_counts().head(10).index
avg_vote_share = df[df['party'].isin(top_parties_by_count)].groupby('party')['vote_share_percentage'].mean().sort_values(ascending=False)

plt.figure(figsize=(10, 5))
sb.barplot(x=avg_vote_share.values, y=avg_vote_share.index, palette='magma')
plt.title("Average Vote Share (%) by Party (Top 10 by Count)")
plt.xlabel("Average Vote Share (%)")
plt.ylabel("Party")
plt.tight_layout()
plt.show()

#(f) Heatmap - Calculate the correlation matrix
numeric_cols = ['votes', 'valid_votes', 'turnout_percentage',
                'margin_percentage', 'vote_share_percentage', 'total_electors']

correlation_matrix = df[numeric_cols].corr()

plt.figure(figsize=(6,5))
sb.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5, square=True)
plt.title('Correlation Heatmap of Election Features')
plt.tight_layout()
plt.show()