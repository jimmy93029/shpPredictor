# Nanshan_tomb_image_segmentation
Nanshan_tomb_image_segmentation

![image](https://github.com/jimmy93029/Nanshan_tomb_image_segmentation/assets/107825203/ac9f5518-d541-4ca0-a3de-bbf53d48d32e)

## 問題描述
本專題想透過航拍影像檔去擷取各個墳墓的位置分布，並透過物件偵測的技術來完成此目標。

## 專題目標
1. (第一階段) 利用 Grounding DINO + segment anything model 製作出小影像檔的 mask 

2. (第二階段) 將各個小影像檔合併成大圖，產出墓物件已遮罩的 png 檔

3. (第三階段) 將各個 mask 合併成圖層，並轉成可供 QGIS 分析的 shp 檔

4. (第四階段) 將上述流程整合，上傳到 Github

5. (第五階段) 製作 jupyter book profile  

## 遇到的問題

*  選擇合適的計算環境

   * 發現 ASGCCA 雲端計算環境有 python 版本和 套件 conflict 的問題
   * 目前改用 google colab pro


* 選擇合適的影像辨識方法

  * [發現 segment anything model 只專注於切割影像，並不能幫我們辨識墓物件的位置](https://github.com/jimmy93029/Nanshan_tomb_image_segmentation/blob/main/mask_generator_result.ipynb)
  * (思路1) 引用 [Grounding DINO 來辨識物件位置](https://blog.roboflow.com/enhance-image-annotation-with-grounding-dino-and-sam/)
  * (思路2) fine-tune SAM  
  
* 切割後的 tif 檔會有 "TileSourceError: File does not have a projected scale, so will not be opened via rasterio with a projection" error," 的問題
  * 為了讓計算環境 (colab pro) 可以跑得動 和提高影像辨識的準確度，我將大的 tif 切割成小的 tif 檔。但我發現將 小 tif 檔匯入 segment-geospatial 套件時，小 tif 檔疑似發生資料遺失的問題
