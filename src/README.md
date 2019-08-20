
|                              | Door | Handle |
|:----------------------------:|:----:|:------:|
| Tensorflow - FR-CNN - OIDv4  |   X  |    X   |
|    OpenCV - SSDV2 - OIDv4    |   X  |    O   |
|   Tf&OpenCV - SSDV2 - COCO   |   O  |        |


### Observations :

#### Dataset
* COCO dataset only has 'Door' class no 'Handles'
* OIDv4 has both 'Door' and 'Handles'

#### Model
* SSD is faster but is less accurate 
* FR-CNN is slow but gives a lot better bounding box and detects 
both the required classes.
* FR-CNN model is not compatible with OpenCV-DNN as few of the layer 
definitions are missing. 
