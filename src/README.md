# Deep learning for object detection 

Deep learning will be used for performing the task of 'handle' detection and 'door' detection.


### Experimentation

Two frameworks are being tested for running the object detection inference :
1. [TensorFlow] (https://github.com/tensorflow/models/tree/master/research/object_detection)
2. [OpenCV-Dnn] (https://docs.opencv.org/master/d2/d58/tutorial_table_of_content_dnn.html)

Tensorflow has both the training and the inferencing functionality whereas OpenCV-Dnn module 
supports only inference and requires a few extra steps for running the pretrained model.

Two models are being tested for the task:
1. [FRCNN[2]](https://arxiv.org/abs/1506.01497)
2. [SSD[1]](https://arxiv.org/abs/1512.02325)

| Pretrained Model             | Door | Handle |
|:----------------------------:|:----:|:------:|
| Tensorflow - FR-CNN - OIDv4  |   X  |    X   |
|    OpenCV - SSDV2 - OIDv4    |   X  |    O   |
|   Tf&OpenCV - SSDV2 - COCO   |   O  |        |

X = High accuracy    
O = Low accuracy

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

### References
#### Note : The relevant tutorial and model links for each of the task are in the .ipynb or .py files
1. Ren, Shaoqing, Kaiming He, Ross B. Girshick and Jian Sun. “Faster R-CNN: Towards Real-Time Object Detection with Region Proposal Networks.” IEEE Transactions on Pattern Analysis and Machine Intelligence 39 (2015): 1137-1149.
2. Liu, Weiwei, Dragomir Anguelov, Dumitru Erhan, Christian Szegedy, Scott E. Reed, Cheng-Yang Fu and Alexander C. Berg. “SSD: Single Shot MultiBox Detector.” ECCV (2016).
