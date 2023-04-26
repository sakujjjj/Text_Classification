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




