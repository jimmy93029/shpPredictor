# 成果展示與分析

## mask 預測結果比較


### 原圖
```{figure} image/Nanshan2_original.png
---
scale: 50%
align: left
---
original
```
### 遮罩後的圖檔
```{figure} image/Nanshan2_on_mask.png
---
scale: 50%
align: left
---
masked
```

* 可以發現此模型幾乎將大部分墓物件都找出來了 (暗示著 模型的 recall 值很很不錯)，而且無關的建築物並未被納入 mask 中 (precision 很高)。
代表模型產出的結果其實很理想。這些圖片再轉成 shapefile 後將有很不錯的呈現結果

## model performance 分析
```{figure} image/performance.png
---
scale: 70%
align: left
---
performance
```


* 在製作 Model 時，我評估對我影響最大的是 false positive, 也就是"錯判成墓物件的其他物品"。所以為了避免這些東西的存在
我將 score_threshold 設為 0.6，目的就是為了讓 bounding box 判定的更嚴格。

* 當然 bounding box 圈的越嚴格，recall 值就有可能越低。所以在 performance 中可以看到 recall 值大約 0.7 ，而
precision 大約 0.9。這是意料之內的結果

