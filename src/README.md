# Deep Learning for object detection 

|Model                         | Door | Handle |
|:----------------------------:|:----:|:------:|
| Tensorflow - FR-CNN - OIDv4  |   X  |    X   |
|    OpenCV - SSDV2 - OIDv4    |   X  |    O   |
|   Tf&OpenCV - SSDV2 - COCO   |   O  |        |

X = High accuracy    
O = Low accuracy

### Observations :

#### Dataset
* COCO dataset only has 'Door' class no 'Handles'
(http://cocodataset.org/#explore)

* OIDv4 has both 'Door' and 'Handles'
(https://storage.googleapis.com/openimages/web/index.html)

#### Model
* SSD is faster but is less accurate 
* FR-CNN is slow but gives a lot better bounding box and detects 
both the required classes.
* FR-CNN model is not compatible with OpenCV-DNN as few of the layer 
definitions are missing. 


#### Note : The relevant tutorial links for each of the task are in the .ipynb or .py files
