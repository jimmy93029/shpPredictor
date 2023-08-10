
## 問題描述
本專題想透過航拍影像檔去擷取各個墳墓的位置分布，並透過物件偵測的技術來完成此目標。

## 專題目標
1. (第一階段) [fine - tune 影像辨識的 model](https://github.com/jimmy93029/Nanshan_tomb_image_segmentation/blob/main/notebooks/yolo-nas_plus_SAM-(part1).ipynb)，並[製作 fine -tuning 需要的 training data](https://app.roboflow.com/wu-d4pdk/nanshang_tomb/2)

2. (第二階段) 將影像辨識的 bounding box 結果對接到 samgeo 的 SamGeo 物件中，並產生 tif 檔的 mask 

3. (第三階段) 將各個 mask 合併成圖層，轉成可供 QGIS 分析的 shp 檔

4. (第四階段) 將上述流程整合，上傳到 Github

5. (第五階段) 製作 jupyter book profile  

&emsp;
## 遇到的問題

*  **選擇合適的計算環境**

   * 發現 ASGCCA 雲端計算環境有 python 版本和 套件 conflict 的問題
   * 目前改用 google colab pro



* **選擇合適的影像辨識方法**

  * 發現 segment anything model 只專注於切割影像，並不能幫我們辨識墓物件的位置 
  * (思路1) 引用 Grounding DINO 來辨識物件位置
      >Grounding DINO 的 text prompt 不容易調整。
      >當 box_threshold (=0.30) 和 text_threshold(=0.15) 較低時，會將並非墓物件的物品納入 ( 像是建築容易被納入 )。
      >當兩者較高時，又容易使準確率較低 

  * (思路2) fine-tune SAM  
  
  * ==(目前)== 想[使用 YOLO-NAS 做 object detection](https://blog.roboflow.com/yolo-nas-how-to-train-on-custom-dataset/)，並[用 SAM 輸出 tif 檔的 mask](https://samgeo.gishub.org/examples/input_prompts/)


  
* **切割 tif 檔的理由與衍伸問題**

  * 為了讓計算環境 (colab pro) 可以跑得動 和提高影像辨識的準確度，我將大的 tif 切割成小的 tif 檔。
 
  * (問題 1) 但我發現將 小 tif 檔 放入 m.add_raster 時，小 tif 檔爆出 TileSourceError 的錯誤。 
    >   切割後的 tif 檔會有 "TileSourceError: File does not have a projected scale, so will not be opened via rasterio with a projection error" 的報錯，
    
     我懷疑是因為 tif 檔經裁切後資料遺失，而導致此問題
  * (問題 2) 在檔案交界處的墓物件會被分割，進而影響準確率。要怎麼解決這問題 ?
   -> 放大圖片讓模型更清楚地檢驗圖片，但同時也會增加被邊界分割的墓物件。這是一個 trade-off
   -> 其實讓模型能辨識 "被邊框切割的墓物件" 就行了

* **怎麼製備 fine-tune 用的 training data ?**
  -> 先將 tif 檔[裁切成小塊的 tif](https://github.com/jimmy93029/Nanshan_tomb_image_segmentation/blob/main/split_tif.py) ，再[轉成 jpg](https://github.com/jimmy93029/Nanshan_tomb_image_segmentation/blob/main/tif2jpg.py) 
  -> 再用 [Roboflow 來 label 資料](https://universe.roboflow.com/wu-d4pdk/nanshang_tomb)
  -> 依據 model 預測不足的物件再餵多一點資料 (像是我們的model 常誤判房屋上的水塔為墓物件，因此我多給它一些 Null 資料以提升其判斷 Null 的能力)
  
* **要怎麼 mask ( jpg檔 ) 轉換成 QGIS 可讀的 shp 檔** (預計)
   -> 首先要將 JPG -> TIFF ( 用  [Aspose.Words for Python via .NET](https://products.aspose.com/words/python-net/conversion/jpg-to-tiff/) 套件轉檔)
   -> 對 TIFF 做 georeference
   -> 再將 TIFF -> SHP ( 用 [samgeo.common.raster_to_shp()](https://samgeo.gishub.org/common/#samgeo.common.raster_to_shp) 轉檔)
   
  
