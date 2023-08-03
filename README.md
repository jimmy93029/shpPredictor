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

&emsp;
## 遇到的問題

*  選擇合適的計算環境

   * 發現 ASGCCA 雲端計算環境有 python 版本和 套件 conflict 的問題
   * 目前改用 google colab pro



* 選擇合適的影像辨識方法

  * 發現 segment anything model 只專注於切割影像，並不能幫我們辨識墓物件的位置 [[參]](https://github.com/jimmy93029/Nanshan_tomb_image_segmentation/blob/main/mask_generator_result.ipynb)
  * (思路1) 引用 Grounding DINO 來辨識物件位置[ [參]]((https://blog.roboflow.com/enhance-image-annotation-with-grounding-dino-and-sam/))

      >Grounding DINO 的 text prompt 不容易調整。
      >當 box_threshold (=0.30) 和 text_threshold(=0.15) 較低時，會將並非墓物件的物品納入 ( 像是建築容易被納入 )。
      >當兩者較高時，又容易使準確率較低 

  * (思路2) fine-tune SAM  
  
  * ==(目前)== 想[使用 YOLO-NAS 做 object detection](https://blog.roboflow.com/yolo-nas-how-to-train-on-custom-dataset/)，並[用 SAM 輸出 tif 檔的 mask](https://samgeo.gishub.org/examples/input_prompts/)


  
* 切割 tif 檔的理由與衍伸問題

  * 為了讓計算環境 (colab pro) 可以跑得動 和提高影像辨識的準確度，我將大的 tif 切割成小的 tif 檔。
 
  * (問題 1) 但我發現將 小 tif 檔 放入 m.add_raster 時，小 tif 檔爆出 TileSourceError 的錯誤。 [[參]](https://github.com/jimmy93029/Nanshan_tomb_image_segmentation/blob/main/automatic_mask_generator.ipynb)
    >   切割後的 tif 檔會有 "TileSourceError: File does not have a projected scale, so will not be opened via rasterio with a projection error" 的報錯，
    
     我懷疑是因為 tif 檔經裁切後資料遺失，而導致此問題
  * (問題 2) 將 小 tif 檔拼回去是否會影響 大 tif 檔的讀取 ? 或許檔案的拼接口會有斷層的情形 ?
