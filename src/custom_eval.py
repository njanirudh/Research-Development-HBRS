import functools
import os
import tensorflow as tf

from object_detection.builders import dataset_builder
from object_detection.builders import graph_rewriter_builder
from object_detection.builders import model_builder
from object_detection.legacy import evaluator
from object_detection.utils import config_util
from object_detection.utils import label_map_util

tf.logging.set_verbosity(tf.logging.INFO)

flags = tf.app.flags
FLAGS = flags.FLAGS

FLAGS.pipeline_config_path = "/home/nj/HBRS/RnD/Dataset/DoorDetect-Dataset/Model/YOLO_door/anirudh_pipeline.config"

print(FLAGS.pipeline_config_path)

configs = config_util.get_configs_from_pipeline_file(
        FLAGS.pipeline_config_path)
input_config = configs['eval_input_config']

def get_next(config):
    return dataset_builder.make_initializable_iterator(
        dataset_builder.build(config)).get_next()

create_input_dict_fn = functools.partial(get_next, input_config)
