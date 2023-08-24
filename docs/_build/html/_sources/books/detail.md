# 程式碼重要資訊講解

## (一) Predicting_mask_for_tifimage.ipynb

### inputs
在 Predicting_mask_for_tifimage 的 inputs 中有 10 個嵾數要填妥，分別如以下

#### 模型權重
* "object_detection_model_checkpoint_path" : 在本欄位中，應填入從
Training_object_detection_model 所得到的 "average_model.pth" 檔案。
或許您當時已將檔案存到 google drive，那請您開啟 google drive，並填入該檔案之位置

* "sam_checkpoint_path" : 在本欄位中，應填入 segment-anything-model 的模型權重。或許您已從上方的程式碼下載檔案，
那請你將 "sam_vit_h_4b8939.pth" 地址複製到該位置

#### dataset class 數目 和 照片來源檔案
* "num_classes" : 資料集中類別的數目

* "source_tiffile" : 欲分析的 tif 檔

#### 物件偵測精準度控制
* "confidence_threshold" : confidence score 代表模型的嚴格程度，分數值越高代表模型判斷物件的嚴格程度越高

* "tile_size" : tile size 代表 tif 檔分割的圖片大小。要知道的是，圖片大小適中才能確保模型判斷準確。如果圖片太大那物件本身會太小而看不清楚
，反之如果圖片太小那物件本身會被切割成不好判讀的形狀。所以使用前請先測試適當大小在丟入模型

#### 照片經緯度資訊
在將 mask 轉回 shp 檔時，我們會需要將 tif 檔 georefernce 成 geotiff。這時候我們就會需要 tif 檔的經緯度

* "top_left_lat" : tif 檔左上角的緯度

* "top_left_lon" : tif 檔左上角的經度

* "below_right_lat" : tif 檔右下角的緯度

* below_right_lon" : tif 檔右下角的經度


### 步驟

