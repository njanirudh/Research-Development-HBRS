cd /home/anaras2s/anirudh/Github/Tensorflow/models/research

protoc object_detection/protos/*.proto --python_out=. 
export PYTHONPATH=$PYTHONPATH:`pwd`:`pwd`/slim

source /home/anaras2s/anaconda3/bin/activate /home/anaras2s/anaconda3/envs/tf-gpu-env
conda deactivate 
conda activate tf-gpu-env

# python /home/anaras2s/anirudh/Github/Tensorflow/models/research/object_detection/legacy/eval.py --pipeline_config_path=/home/anaras2s/anirudh/Dataset/DoorDetect-Dataset/Model/ssd_mobilenet_v2_oid_v4_2018_12_12/anirudh_pipeline.config --checkpoint_dir=/home/anaras2s/anirudh/Models/SSD_V2_OID --eval_dir=/home/anaras2s/waste/eval --alsologtostderr
python /home/anaras2s/anirudh/Github/Tensorflow/models/research/object_detection/legacy/eval.py --pipeline_config_path=/home/anaras2s/anirudh/Dataset/DoorDetect-Dataset/Model/faster_rcnn_inception_v2_coco_2018_01_28/anirudh_pipeline.config --checkpoint_dir=/home/anaras2s/anirudh/Models/FRCNN --eval_dir=/home/anaras2s/waste/eval_frcnn --alsologtostderr
