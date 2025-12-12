df = df[['content']]
df.rename(columns={'content': 'Ulasan'}, inplace=True)
df.to_csv('data_ulasan_feature_selection.csv', index=False)

total_ulasan = len(df)
print(f'Total data ulasan: {total_ulasan}')
