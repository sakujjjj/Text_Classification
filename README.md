# 簡易的自動文本分類

* 使用Python中的Pandas, Scikit-learn等工具

* 將Excel檔案匯入成Pandas DataFrame資料結構。

* 使用Scikit-learn中的CountVectorizer模組將文本資料轉換成向量形式，並且使用二元語法形式的向量。

* 將轉換後的向量和對應的標籤(label)送入LogisticRegression模型中進行訓練。

* 將一個新的文本資料轉換成向量形式，並使用已經訓練好的模型對其進行預測。

* 並且輸出預測結果以及預測結果的機率，例如此次input = ["明天會下雨嗎?"]，所得到的預測為: ['天氣']，並得到預測結果機率94%。


### 預測意圖
`lr.predict(X2)`  
- lr 是一個已經訓練好的 logistic regression 分類模型會使用已經學習到的特徵權重來預測輸入的文本屬於哪個分類。
- predict() 方法會返回一個代表預測分類的數值，比如分類編號或分類機率等。 
   
例如此次`input = ["申請註冊帳號"]`  
`print(lr.predict(X2))`為`['會員']`

![image](https://user-images.githubusercontent.com/95430501/234512019-230786dc-3bb8-4888-b719-c4900dfcad79.png)


```
probs = lr.predict_proba(X2)[0]
for predict_intent, prob in sorted(zip(lr.classes_, probs), key=lambda x: x[1], reverse=True):
  print(predict_intent, prob)
```

- 對模型預測的結果進行排序，並輸出每一個預測結果的機率值。
- lr.classes_ 會返回模型中所有可能的分類標籤（例如，在文本分類中，可能的標籤可能是"正面"、"負面"或"中性"等）。
- lr.predict_proba(X2) 會返回在給定的輸入 X2 的情況下，模型分類為每個可能標籤的機率值。
- zip(lr.classes_, probs) 會把分類標籤和機率值配對，並以機率值降序排列。
- 最後，for 循環會遍歷每一個配對並進行輸出，以預測標籤和機率值作為輸出。  
  
例如此次`input = ["明天會下雨嗎?"]`  
所得到的預測為:  
![image](https://user-images.githubusercontent.com/95430501/234507280-4cd5fd56-16a7-4b58-8229-3626ba739727.png)

## References
- [sklearn.feature_extraction.text.CountVectorizer](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html)
- [簡單快速上手自然語言處理中的文本分類](https://www.tpisoftware.com/tpu/articleDetails/2013)  
- [分類特徵(Categorical Features)](https://ithelp.ithome.com.tw/articles/10205475)



