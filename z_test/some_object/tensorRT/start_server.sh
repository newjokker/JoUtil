#!/bin/bash

echo "start serve"
echo "---------------"

RTSP=${RTSP:-rtsp://admin:txkj@2021!@192.168.3.19:554/Streaming/Channels/101}
RTMP=${RTMP:-rtsp://192.168.3.99/live/1211}
W=${W:-1280}
H=${H:-720}
FPS=${FPS:-15}
PORT=${PORT:-1211}
GPUID=${GPUID:-0}

echo "port : $PORT"
echo "fps  : $FPS"
echo "w    : $W"
echo "h    : $H"
echo "rtsp : $RTSP"
echo "rtmp : $RTMP"
echo "gpuID : $GPUID"
echo "---------------"

cd /home/tensorRT/tensorrt_test
python3 /home/tensorRT/tensorrt_test/allflow.py --port $PORT --fps $FPS --w $W --h $H --rtsp "$RTSP" --rtmp "$RTMP" --gpuID $GPUID

echo "stop serve"


# docker run code
# docker run --gpus 'device=0'  -p 111:111 -v /home/ldq/tensorrt_logs:/home/tensorRT/tensorrt_test/logs -e PORT=111 -e FPS=15 -e W=1280 -e H=720 -e RTSP='rtsp://admin:txkj@2021!@192.168.3.19:554/Streaming/Channels/101' -e RTMP='rtsp://192.168.3.99/live/1211' -d tensorrt:v0.0.5 /home/tensorRT/tensorrt_test/start_server.sh

