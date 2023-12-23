# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import os
import numpy as np
import torch
import json
import random
import uuid
import torch.nn as nn
import torchvision.transforms as transforms
import torchvision.models as models
from PIL import Image
from JoTools.utils.FileOperationUtil import FileOperationUtil
import requests
from io import BytesIO
from JoTools.utils.JsonUtil import JsonUtil
# import pdb
from gevent import monkey
from gevent.pywsgi import WSGIServer
from flask import Flask, request, jsonify
import base64
import io
import argparse
from pymilvus import (
    connections,
    utility,
    FieldSchema, CollectionSchema, DataType,
    Collection,
)

# connect milvus
COLLECTION_NAME = "uc_milvus"
connections.connect("default", host="192.168.3.221", port="19530")
fields = [FieldSchema(name="uc", dtype=DataType.VARCHAR, is_primary=True, auto_id=False, max_length=7),
          FieldSchema(name="feature", dtype=DataType.FLOAT_VECTOR, dim=512)]
schema = CollectionSchema(fields, f"{COLLECTION_NAME} is a demo")
uc_milvus = Collection(COLLECTION_NAME, schema, consistency_level="Strong")
uc_milvus.load()
print("* load milvus success")

