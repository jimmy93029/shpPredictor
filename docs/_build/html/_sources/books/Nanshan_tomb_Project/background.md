# 背景知識補充

&emsp;
## 實驗素材: 南山公墓航拍圖
此次專案的實驗素材是來自於[南山公墓航拍圖](https://data.depositar.io/dataset/orthoimagery-nanshan-cemetery)。透過 Deep learning 
技術，我們期望將航拍圖的墓物件分布找出來，進而對其做其他分析。

由於公墓的分布又密又擠，導致物件的偵測有些難度。這也是此影像檔帶給我的挑戰之一

![img.png](../image/Nanshantomb.png)


&emsp;
## 物件偵測模型: [Yolo - NAS](https://docs.ultralytics.com/models/yolo-nas/) 
yolo - nas 推出於 2023 年 3 月，是一個建立在 yolo - v8 之上的物件偵測模型。它利用 Neural architecture search 的方法搜索出了
兼具準確率與 速度的模型，而且相比於其他 yolo 模型，它在不損失掉精準度的狀況下速度有明顯提升 (如下圖)。

![img.png](../image/yolo_nas_frontier.png)

### ps: Neural architecture search (NAS)
neural architecture search 旨在透過機器學習的方法搜索出最佳化的模型架構。以往模型的架構都是人手動調整出來的，所以產出的模型雖然效果
不錯，但是難以達到最精準的配置。然而透過 NAS 的方法，我們可以讓機器自己調整出最精準的模型。而此類常見的作法有 暴搜、
Reinforcement learning、gradiant-descent 等方法

&emsp;
## 語意分割模型: [SAM](https://docs.ultralytics.com/models/sam/) (segment - anything - model)
SAM　提出於 2023 年 4 月，是一個語意分割模型 (Semantic segmentation)。不只如此，它還是一個大型的基底模型 (foundation model) 
，因為訓練於擁有 10 億資料的 [SA-1B Dataset](https://ai.meta.com/datasets/segment-anything/)，使得它得精準度很高。

此外，SAM 也具有 zero-shot 的泛化能力。它配備了可用 prompt 當作 input 的功能，所以它能對不同任務做調整。
這樣的功能讓它作為一個很好的 foundation model

![img.png](../image/penguin.png)

&emsp;
## 資料處理平台: [Roboflow](https://roboflow.com/) 
Roboflow 是一個專供給於影像辨識的資料處理平台。它有好用的 annotation、prepoccessing、augmentation 功能，
以及它擁有相當快的資料傳輸速度，所以將它作為資料存放的平台是十分便利的。

而且它也造福群眾，撰寫了許多影像辨識模型的使用教學。shpPredictor 專案也參考了許多它的程式碼和文章

![img.png](../image/prepoccess.png)

