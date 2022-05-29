import wget
import os

# ***********************************************************************************************************
# 0. Setup Paths
# ***********************************************************************************************************
# Variables od Pretrained models
CUSTOM_MODEL_NAME = 'my_ssd_mobnet'
PRETRAINED_MODEL_NAME = 'ssd_mobilenet_v2_fpnlite_320x320_coco17_tpu-8'
# link do Pretrained models (iz tega linka ga lahko snameš)
PRETRAINED_MODEL_URL = 'http://download.tensorflow.org/models/object_detection/tf2/20200711/ssd_mobilenet_v2_fpnlite_320x320_coco17_tpu-8.tar.gz'
TF_RECORD_SCRIPT_NAME = 'generate_tfrecord.py'
LABEL_MAP_NAME = 'label_map.pbtxt'

# Shrani vse mape poti v dictionary paths
paths = {
    'WORKSPACE_PATH': os.path.join('Tensorflow', 'workspace'),
    'SCRIPTS_PATH': os.path.join('Tensorflow', 'scripts'),
    'APIMODEL_PATH': os.path.join('Tensorflow', 'models'),
    'ANNOTATION_PATH': os.path.join('Tensorflow', 'workspace', 'annotations'),
    'IMAGE_PATH': os.path.join('Tensorflow', 'workspace', 'images'),
    'MODEL_PATH': os.path.join('Tensorflow', 'workspace', 'models'),
    'PRETRAINED_MODEL_PATH': os.path.join('Tensorflow', 'workspace', 'pre-trained-models'),
    'CHECKPOINT_PATH': os.path.join('Tensorflow', 'workspace', 'models', CUSTOM_MODEL_NAME),
    'OUTPUT_PATH': os.path.join('Tensorflow', 'workspace', 'models', CUSTOM_MODEL_NAME, 'export'),
    'TFJS_PATH': os.path.join('Tensorflow', 'workspace', 'models', CUSTOM_MODEL_NAME, 'tfjsexport'),
    'TFLITE_PATH': os.path.join('Tensorflow', 'workspace', 'models', CUSTOM_MODEL_NAME, 'tfliteexport'),
    'PROTOC_PATH': os.path.join('Tensorflow', 'protoc'),
    'HOME': os.path.join('C:', '\\', 'Users', 'janezv', 'Documents', 'IZOBRAZEVANJE doma', 'AI Umetna inteligenca', '2021-2022 Object Detection Tensor Flow')
}

# Files dictionary
files = {
    'PIPELINE_CONFIG': os.path.join('Tensorflow', 'workspace', 'models', CUSTOM_MODEL_NAME, 'pipeline.config'),
    'TF_RECORD_SCRIPT': os.path.join(paths['SCRIPTS_PATH'], TF_RECORD_SCRIPT_NAME),
    'LABELMAP': os.path.join(paths['ANNOTATION_PATH'], LABEL_MAP_NAME)
}

# Kreiraj vse mape in podmape zapisane v Dictionary paths
# mode
for path in paths.values():
    if not os.path.exists(path):
        if os.name == 'posix':
            # Linux-Python ukaz- ne vem, če dela
            os.makedirs(path)
        if os.name == 'nt':
            os.makedirs(path)

# ***********************************************************************************************************
# 1. Download TF Models Pretrained Models from Tensorflow Model Zoo and Install TFOD
# ********************************************************************************************************
os.system('pip install wget')
if not os.path.exists(os.path.join(paths['APIMODEL_PATH'], 'research', 'object_detection')):
    # Iz dictionary sestavi string spremenljivko git command (natejena tmp2string, direkt vrednost iz dictionary vrže napako)
    gitCommand = 'git clone https://github.com/tensorflow/models ' + \
        paths['APIMODEL_PATH']
    # izvedi git komando v CMD-ju
    os.system(gitCommand)

# Install Tensorflow Object Deteciton
if os.name == 'posix':
    print('ukazi za linux operacijski sistem')

if os.name == 'nt':
    # Download Prostocol Buffers uporablja jih tenserFlow https://developers.google.com/protocol-buffers
    url = "https://github.com/protocolbuffers/protobuf/releases/download/v3.15.6/protoc-3.15.6-win64.zip"
    wget.download(url)
    cmdCommand = 'move protoc-3.15.6-win64.zip ' + paths['PROTOC_PATH']
    os.system(cmdCommand)
    # zamenjaj pot v \Tensorflow\protoc in untaraj datoteko
    os.chdir(paths['PROTOC_PATH'])
    os.system('tar -xf protoc-3.15.6-win64.zip')
    os.environ['PATH'] += os.pathsep + \
        os.path.abspath(os.path.join(paths['PROTOC_PATH'], 'bin'))
    os.chdir(paths['HOME'])
    # Print the current working directory
    retval = os.getcwd()
    os.chdir('Tensorflow/models/research')
    cmdCommand = 'protoc object_detection/protos/*.proto --python_out=. && copy object_detection\\packages\\tf2\\setup.py setup.py && python setup.py build && python setup.py install'
    os.chdir(paths['HOME'])
    os.system(cmdCommand)
    retval = os.getcwd()
    os.chdir('Tensorflow/models/research/slim')
    os.system('pip install -e .')

    VERIFICATION_SCRIPT = os.path.join(
        paths['APIMODEL_PATH'], 'research', 'object_detection', 'builders', 'model_builder_tf2_test.py')
    cmdCommand = 'python '+VERIFICATION_SCRIPT
    rez = os.system(cmdCommand)
    print(rez)
