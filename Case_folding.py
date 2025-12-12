df = pd.read_csv('data_ulasan_cleaning.csv')
df['Ulasan_case_folding'] = df['Ulasan_cleaning'].str.lower()
df.to_csv('data_ulasan_case_folding.csv', index=False)

total_ulasan = len(df)
print(f'Total data ulasan: {total_ulasan}')
