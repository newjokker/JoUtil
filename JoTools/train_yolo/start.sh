#!/bin/bash


# test

export DEVICE=0
#export MODEL_TYPE=yolov5x
export MODEL_TYPE=yolov5s
export BATCH_SIZE=4
#export LABEL_LIST=Fnormal,fzc_broken
export LABEL_LIST=fzc,nc,xj,jyz,ring
export EPOCH=50
export PROJECT=/usr/yolo_train/runs_train
export IMAGE_SIZE=864

export TRAIN_UCD_NAME=docker\\tag_num_first
#export TRAIN_UCD_NAME=docker\\tag_gradient_first
export VAL_UCD_NAME=docker\\recommend_test


# don't change
export TRAIN_XML_DIR=/usr/yolo_train/xml_dir/train
export VAL_XML_DIR=/usr/yolo_train/xml_dir/val
export TRAIN_TXT_DIR=/usr/yolo_train/txt_dir/train
export VAL_TXT_DIR=/usr/yolo_train/txt_dir/val


if [ -d ${TRAIN_XML_DIR} ];then
rm -r ${TRAIN_XML_DIR}
mkdir -p ${TRAIN_XML_DIR}
fi

if [ -d ${VAL_XML_DIR} ];then
rm -r ${VAL_XML_DIR}
mkdir -p ${VAL_XML_DIR}
fi

if [ -d ${TRAIN_TXT_DIR} ];then
rm -r ${TRAIN_TXT_DIR}
mkdir -p ${TRAIN_TXT_DIR}
fi

if [ -d ${VAL_TXT_DIR} ];then
rm -r ${VAL_TXT_DIR}
mkdir -p ${VAL_TXT_DIR}
fi


#mkdir -p /usr/yolo_train/xml_dir/train
#mkdir -p /usr/yolo_train/xml_dir/val
#mkdir -p /usr/yolo_train/txt_dir/train
#mkdir -p /usr/yolo_train/txt_dir/val


# load ucd

rm /usr/yolo_train/train_ucd.json
rm /usr/yolo_train/val_ucd.json

/usr/lib/ucd_v1.3 load ${TRAIN_UCD_NAME} /usr/yolo_train/train_ucd.json
/usr/lib/ucd_v1.3 load ${VAL_UCD_NAME} /usr/yolo_train/val_ucd.json

# load img
/usr/lib/ucd_v1.3 save_cache /usr/yolo_train/train_ucd.json 10
/usr/lib/ucd_v1.3 save_cache /usr/yolo_train/val_ucd.json 10

# parse xml from ucd
/usr/lib/ucd_v1.3 parse_xml /usr/yolo_train/train_ucd.json ${TRAIN_XML_DIR}
/usr/lib/ucd_v1.3 parse_xml /usr/yolo_train/val_ucd.json ${VAL_XML_DIR}

# get txt from xml
python3 voc_to_yolo_txt.py --xml_dir ${TRAIN_XML_DIR}    --txt_dir ${TRAIN_TXT_DIR}   --label_list ${LABEL_LIST}
python3 voc_to_yolo_txt.py --xml_dir ${VAL_XML_DIR}      --txt_dir ${VAL_TXT_DIR}     --label_list ${LABEL_LIST}

# get yaml
python3 get_yaml.py --yaml_path /usr/yolo_train/train.yaml --label_list ${LABEL_LIST}

# train model
python train.py --data /usr/yolo_train/train.yaml --cfg "./models/${MODEL_TYPE}.yaml" --weights "./${MODEL_TYPE}.pt" --batch-size ${BATCH_SIZE}  --device ${DEVICE} --epochs ${EPOCH} --imgsz ${IMAGE_SIZE} --name tag_num_first



