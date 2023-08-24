# 程式碼重要資訊講解

以下將會提醒使用模型的注意事項，請詳閱以下說明
### (一) Training_object_detection_model_resultbook.ipynb
Training_object_detection_model_resultbook 中有以下程式碼需要注意

#### 1. 登入 Roboflow 並填上資料集
```{code-block}
%cd {HOME}

import roboflow
from roboflow import Roboflow

roboflow.login()

rf = Roboflow()

Project_name = "nanshang_tomb"  # 請登入 roboflow 並寫上您的資料集名稱 和 版本
Version = 10

project = rf.workspace().project(Project_name)
dataset = project.version(Version).download("yolov5")
```

* 請在 Project 中填入您所用的專案名稱，且在 Version 中填入您所要用得 roboflow 版本

#### 2. 填入 SCORE_THRSHOLD、 BATCH_SIZE、 MAX_EPOCHS
```{code-block}
MODEL_ARCH = 'yolo_nas_l'
MODEL_ARCH = 'yolo_nas_l'
BATCH_SIZE = 10
MAX_EPOCHS = 40
SCORE_THRSHOLD = 0.6
CHECKPOINT_DIR = f'{HOME}/checkpoints'
EXPERIMENT_NAME = project.name.lower().replace(" ", "_")
```
* SCORE_THRSHOLD 控制著模型的嚴格程度。該值越高 -> bounding box 的數量越少 -> 模型的 recall 值越低。 
最好調出最理想的 SCORE_THRSHOLD，以達到最高的 F1 值 

* MAX_EPOCHS 會影響模型運行時間和精準度，務必填妥

* BATCH_SIZE 會影響 Colab 中的 RAM 的使用大小。如果不幸 RAM 的使用量超出 Colab 限制，可以嘗試降低 BATCH_SIZE 大小 

#### 3. 訓練模型後務必將 checkpoint 資料夾的  average_model.pth 下載下來，此檔案將在下一份 workbook 中使用到

```{code-block}
import locale
locale.getpreferredencoding = lambda: "UTF-8"
%cp "/content/checkpoints/nanshang_tomb/average_model.pth" "/content/drive/MyDrive/project_NanShang/resources/average_modelv10.pth"
```
* 除了將資料載到本機，也可以使用以上程式碼將資料轉移到 google 雲端硬碟 (記得先連接雲端硬碟在執行此程式碼)

### (二) Predicting_mask_for_tifimage.ipynb
Predicting_mask_for_tifimage 中的 inputs 有 10 個嵾數要填妥，分別如下

```{code-cell} 
inputs = {
      # 模型權重
      "object_detection_model_checkpoint_path": "/content/drive/MyDrive/project_NanShang/resources/average_modelbest.pth",
      "sam_checkpoint_path": "/content/drive/MyDrive/project_NanShang/resources/sam_vit_h_4b8939.pth",

      #　dataset class 數目 和 照片來源檔案
      "num_classes": 2,
      "source_tiffile": "/content/drive/MyDrive/project_NanShang/resources/NanShang_Tomb_cp.tif",

      # 物件偵測精準度控制
      "confidence_threshold": 0.65,
      "tile_size": 700,

      # 照片經緯度資訊
      "top_left_lat": 22.97494,           # tif 檔左上角的緯度
      "top_left_lon": 120.19544,          # tif 檔左上角的經度
      "below_right_lat": 22.96717,         # tif 檔右下角的緯度
      "below_right_lon": 120.19775,        # tif 檔右下角的經度

      "device": 'cuda' if torch.cuda.is_available() else "cpu",
      "model_arch": 'yolo_nas_l',
      "sam_encoder_version": "vit_h",

}
```


#### 1. 模型權重
* "object_detection_model_checkpoint_path" : 在本欄位中，應填入從
Training_object_detection_model 所得到的 "average_model.pth" 檔案。
或許您當時已將檔案存到 google drive，那請您開啟 google drive，並填入該檔案之位置

* "sam_checkpoint_path" : 在本欄位中，應填入 segment-anything-model 的模型權重。或許您已從上方的程式碼下載檔案，
那請你將 "sam_vit_h_4b8939.pth" 地址複製到該位置

#### 2. dataset class 數目 和 照片來源檔案
* "num_classes" : 資料集中類別的數目

* "source_tiffile" : 欲分析的 tif 檔

#### 3. 物件偵測精準度控制
* "confidence_threshold" : confidence score 代表模型的嚴格程度，分數值越高代表模型判斷物件的嚴格程度越高

* "tile_size" : tile size 代表 tif 檔分割的圖片大小。要知道的是，圖片大小適中才能確保模型判斷準確。如果圖片太大那物件本身會太小而看不清楚
，反之如果圖片太小那物件本身會被切割成不好判讀的形狀。所以使用前請先測試適當大小在丟入模型

#### 4. 照片經緯度資訊
在將 mask 轉回 shp 檔時，我們會需要將 tif 檔 georefernce 成 geotiff。這時候我們就會需要 tif 檔的經緯度

* "top_left_lat" : tif 檔左上角的緯度

* "top_left_lon" : tif 檔左上角的經度

* "below_right_lat" : tif 檔右下角的緯度

* below_right_lon" : tif 檔右下角的經度



