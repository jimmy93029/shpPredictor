# 中研院暑期專案: ShpPredictor 介紹

工作日誌見: [暑期實習工作紀錄(下)](https://hackmd.io/@edy5wylvRnustuodZbspjw/HkT-7Kqjh)

專案規劃見: [南山公墓專案計畫: 使用 SAM 套件進行南山公墓航拍影像檔的墓物件辨識](https://hackmd.io/@edy5wylvRnustuodZbspjw/r1YvSNPo3)

&emsp;
## shpPredictor 專案目標
此專案目的是建立一個"自動產生地圖遮罩" 的方法。這項方法將節省地理分析人員產生空拍圖遮罩檔的時間。多出來的時間將有助於該人員進行決策

&emsp;
## shpPredictor 撰寫緣由
還記得在中研院的一堂課中我接觸到了 QGIS 軟體。
當時第一次學到 QGIS 的我，沒想到竟然經由步驟簡單的疊圖分析，就能從[地圖中嗅到許多資訊](https://hackmd.io/@edy5wylvRnustuodZbspjw/HycpQLK5n)
。自此我開始佩服起 QGIS 軟體的強大。

然而，QGIS 所使用的 shp 檔經常是手工製成，這樣的過程不僅耗人力也浪費時間。因此進行專案構想時我就想或許自己能為 QGIS 提供自己的一份力。
試圖引入 Deep Learning 的技術解決這問題

我將使用 Meta 提出的物件分割模型 SAM 去產生地圖遮罩，並用物件偵測模型 (Yolo -nas) 去辨識出墳墓位置。在產生墳墓位置的 jpg 檔後，
檔案將經由一系列檔案轉換、georeference 來變成 shp 檔。更多 shpPredictor 的解說可以到: [shpPredictor-jupyter-book](https://jimmy93029.github.io/shpPredictor/intro.html#) 中察看

&emsp;
## shpPredictor 如何取用
* 使用 shpPredictor 的方法有二
1. 使用 Predicting_mask_for_tifimage(on_local)。將 inputs 所需資料被妥後，可以進到 main.py 來產生 shp 檔
2. 使用 Training_object_detection_model_workbook.ipynb 和 Predicting_mask_for_tifimage.ipynb。可以將檔案上傳至 
google colab，已啟用 Colab 環境執行程式

請確認使用裝置有足夠 GPU。依據檔案大小，使用模型所需的 GPU 大小也不一 
 
