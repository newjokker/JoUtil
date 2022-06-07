# -*- coding: utf-8  -*-
# -*- author: jokker -*-



from flask import Flask, request, make_response
from datetime import datetime
import os

app = Flask(__name__)

IMG_PATH = r"/home/ldq/del/20210718151436717.png"
IMG_DIR = r"\\192.168.3.80\数据\root_dir\json_img"


@app.route('/display/img/<string:filename>', methods=['GET'])
def display_img(filename):
    request_begin_time = datetime.today()
    print("request_begin_time", request_begin_time)
    if request.method == 'GET':
        image_data = open(IMG_PATH, "rb").read()
        response = make_response(image_data)
        response.headers['Content-Type'] = 'image/jpg'
        return response
    else:
        pass

@app.route('/display/uc/<string:uc>', methods=['GET'])
def display_uc(uc):
    request_begin_time = datetime.today()
    print("request_begin_time", request_begin_time)
    if request.method == 'GET':
        image_data = open(os.path.join(IMG_DIR, uc[:3], uc + '.jpg'), "rb").read()
        response = make_response(image_data)
        response.headers['Content-Type'] = 'image/jpg'
        return response
    else:
        pass


if __name__ == '__main__':

    # app.run(host='192.168.3.221', port=5001)
    app.run(host='127.0.0.1', port=5001)
