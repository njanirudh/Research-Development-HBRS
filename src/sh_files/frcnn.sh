g#!/bin/bash
#SBATCH --partition=gpu          # partition (queue)
#SBATCH --ntasks-per-node=32     # number of cores per node
#SBATCH --mem=64G                 # memory per node in MB (different units with suffix K|M|G|T)
#SBATCH --time=2-00:00:00              # total runtime of job allocation (format D-HH:MM:SS; first parts optional)
#SBATCH --output=frcnn_resnet_v1.%j.out    # filename for STDOUT (%N: nodename, %j: job-ID)
#SBATCH --error=frcnn_resnet_v1.%j.err     # filename for STDERR

# here comes the part with the description of the computational work, for example:
# load the OpenMPI environment

# load cuda
# module load cuda

cd /home/anaras2s/anirudh/Github/Tensorflow/models/research

protoc object_detection/protos/*.proto --python_out=. 
export PYTHONPATH=$PYTHONPATH:`pwd`:`pwd`/slim

source /home/anaras2s/anaconda3/bin/activate /home/anaras2s/anaconda3/envs/tf-gpu-env
conda deactivate 
conda activate tf-gpu-env

python /home/anaras2s/anirudh/Github/Tensorflow/models/research/object_detection/model_main.py --pipeline_config_path=/home/anaras2s/anirudh/Dataset/DoorDetect-Dataset/Model/faster_rcnn_inception_resnet_v2_atrous_oid_v4_2018_12_12/anirudh_pipeline.config --model_dir=/home/anaras2s/anirudh/Models/FRCNN --num_train_steps=100000 --sample_1_of_n_eval_examples=10 --alsologtostderr