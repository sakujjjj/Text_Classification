import pandas as pd
df = pd.read_excel("文本分類範例.xlsx")
df = df.values.tolist()

corpus = [row[0] for row in df]
intents = [row[1] for row in df]
print(corpus)
