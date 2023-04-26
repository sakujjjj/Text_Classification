import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
df = pd.read_excel("文本分類範例.xlsx")
df = df.values.tolist()

corpus = [row[0] for row in df]
intents = [row[1] for row in df]
# print(corpus[:27])

feature_extractor = CountVectorizer(
    analyzer="word", ngram_range=(1, 2), binary=True, token_pattern=r'([a-zA-Z]+|\w)'
)

# 二元語法形式的向量
X = feature_extractor.fit_transform(corpus)

# b = len(feature_extractor.get_feature_names_out())
# print(b)


# 分類
INTENT_CLASSIFY_REGULARIZATION = "l2"
lr = LogisticRegression(
    penalty=INTENT_CLASSIFY_REGULARIZATION, class_weight='balanced')
lr.fit(X, intents)

# input
# input = ["查詢明天的降雨量"]
# input = ["明天會下雨嗎?"]
input = ["申請註冊帳號"]
X2 = feature_extractor.transform(input)
# print(len(X2.toarray()[0]))
# print(X2)
# print(type(X2))
# print(X2.nonzero())
# print(X2.nonzero()[1])
# print(len(X2.nonzero()[1]))
# print(type(X2.nonzero()[1]))

# all feature
feature_names = feature_extractor.get_feature_names_out()
# print(feature_names)
# print(feature_names[179])

# 抽取到的feature
# for index in X2.nonzero()[1]:
#     print(feature_names[index])

# 預測意圖
# lr 是一個已經訓練好的 logistic regression 分類模型
# 模型會使用已經學習到的特徵權重來預測輸入的文本屬於哪個分類。predict() 方法會返回一個代表預測分類的數值，比如分類編號或分類機率等，具體取決於模型的設計。
print(lr.predict(X2))


probs = lr.predict_proba(X2)[0]
for predict_intent, prob in sorted(zip(lr.classes_, probs), key=lambda x: x[1], reverse=True):
    print(predict_intent, prob)
