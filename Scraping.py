def scrape_google_play_reviews(app_id, num_reviews=100):
    reviews_list = []
    count = 0

    while count < num_reviews:
        try:
            result, _ = reviews(
                app_id,
                lang='id',
                country='id',
                sort=Sort.NEWEST,
                count=min(100, num_reviews - count)
            )
            reviews_list.extend(result)
            count += len(result)

            if len(result) < 100:
                break
        except Exception as e:
            print(f"Error: {e}")
            break

    return pd.DataFrame(reviews_list)

app_id = 'id.co.linebank'
num_reviews = 40000
df = scrape_google_play_reviews(app_id, num_reviews)
df.to_csv('data_ulasan.csv', index=False)
