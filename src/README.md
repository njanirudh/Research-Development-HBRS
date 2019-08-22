# Deep learning for object detection 

Deep learning will be used for performing the task of 'handle' detection and 'door' detection.

--------
### Experimentation

Two common frameworks are being tested for running the object detection inference :
1. [TensorFlow](https://github.com/tensorflow/models/tree/master/research/object_detection)
2. [OpenCV-DNN](https://docs.opencv.org/master/d2/d58/tutorial_table_of_content_dnn.html)

Tensorflow has both the training and the inferencing functionality whereas OpenCV-DNN module 
supports only inference and requires a [few extra steps](https://github.com/opencv/opencv/wiki/TensorFlow-Object-Detection-API) for running the pretrained model.

Two models are being tested for the task:
1. [FRCNN](https://arxiv.org/abs/1506.01497)[2]
2. [SSD](https://arxiv.org/abs/1512.02325)[1]

Qualitative comparison for the different combinations of the 
inference engine and the model have been done below: 

|Model + Dataset     |  I.E      | Door | Handle |
|:------------------:|:---------:|:----:|:------:|
| FR-CNN + OIDv4     |   Tf      |   X  |    X   |
| FR-CNN + COCO      |   Tf      |   X  |    -   |
| SSDV2  + OIDv4     |   Tf      |   X  |    X   |
| SSDV2  + COCO      |   Tf      |   X  |    -   |
|                    |           |      |        |
| FR-CNN + OIDv4     |   OpenCV  |   X  |    O   |
| FR-CNN + COCO      |   OpenCV  |   O  |    -   |
| SSDV2  + OIDv4     |   OpenCV  |   X  |    O   |
| SSDV2  + COCO      |   OpenCV  |   O  |    -   |
    
I.E = Inference engine    
'-'  = Not available/Possible    
X = High accuracy    
O = Low accuracy

--------
### Observations :

#### Dataset
* [COCO dataset](http://cocodataset.org/#explore) only has 'Door' class no 'Handles'

* [OIDv4](https://storage.googleapis.com/openimages/web/index.html) has both 'Door' and 'Handles'

#### Model
* SSD is faster but is less accurate 
* FR-CNN is slow but gives a lot better bounding box and detects 
both the required classes.
* FR-CNN model is not compatible with OpenCV-DNN as few of the layer 
definitions are missing. 

--------
### References
#### Note : The relevant documentation and model links for each of the task are in the .ipynb or .py files
1. Ren, Shaoqing, Kaiming He, Ross B. Girshick and Jian Sun. “Faster R-CNN: Towards Real-Time Object Detection with Region Proposal Networks.” IEEE Transactions on Pattern Analysis and Machine Intelligence 39 (2015): 1137-1149.
2. Liu, Weiwei, Dragomir Anguelov, Dumitru Erhan, Christian Szegedy, Scott E. Reed, Cheng-Yang Fu and Alexander C. Berg. “SSD: Single Shot MultiBox Detector.” ECCV (2016).
