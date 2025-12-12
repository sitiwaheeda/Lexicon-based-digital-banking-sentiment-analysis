import pandas as pd
import ast

df = pd.read_csv('/work/data_ulasan_normalisasi.csv')

# Custom lexicon
slank_word_dict = {
    "agak": "sedikit", "pas": "saat", "nggak": "tidak", "kagak": "tidak", "kgk": "tidak",
    "tdk": "tidak", "gak": "tidak", "ga": "tidak", "gk": "tidak", "egk": "tidak", "enggak": "tidak",
    "jd": "jadi", "cpt": "cepat", "sdh": "sudah", "bisa": "dapat", "tf": "transfer", "e wallet": "e_wallet",
    "bs": "dapat", "bsa": "dapat", "recommend": "rekomendasi", "bagis": "bagus", "top up": "top_up",
    "recomended": "rekomendasi", "recommended": "rekomendasi", "rekomendasi": "rekomendasi",
    "lelet": "lama", "lambat": "lama", "lola": "lama", "buruk": "jelek", "busuk": "jelek",
    "rumit": "sulit", "ribet": "sulit", "repot": "sulit", "susah": "sulit", "sh": "sih",
    "mantul": "bagus", "mantap": "bagus", "ok": "bagus", "oke": "bagus", "cs": "customer_service",
    "gw": "saya", "gue": "saya", "w": "saya", "q": "saya", "sy": "saya", "aq": "saya",
    "gua": "saya", "lu": "kamu", "lo": "kamu", "u": "kamu", "km": "kamu", "kmu": "kamu",
    "loe": "kamu", "yg": "yang", "jg": "juga", "trs": "terus", "dgn": "dengan",
    "utk": "untuk", "spy": "supaya", "skrg": "sekarang", "sgt": "sangat", "krn": "karena",
    "hrs": "harus", "tp": "tapi", "tpi": "tapi", "td": "tadi", "dr": "dari", "dll": "dan lain lain",
    "dsb": "dan sebagainya", "lg": "lagi", "byk": "banyak", "kyk": "seperti",
    "kyak": "seperti", "kayak": "seperti", "udh": "sudah", "udah": "sudah", "keren": "bagus",
    "lemot": "lama", "apk": "aplikasi", "mantab": "bagus", "mantaps": "bagus", "mantapz": "bagus"
}

def normalize_custom(tokens):
    return [slank_word_dict.get(token, token) for token in tokens]

def convert_to_list(text):
    if isinstance(text, str):
        try:
            return ast.literal_eval(text)
        except (ValueError, SyntaxError):
            return text.split()
    return text

df['Ulasan_normalisasi'] = df['Ulasan_normalisasi'].apply(convert_to_list)
df['Ulasan_normalisasi'] = df['Ulasan_normalisasi'].apply(normalize_custom)
df.to_csv('data_ulasan_normalisasi_final.csv', index=False)

print(f'Total data ulasan: {len(df)}')
