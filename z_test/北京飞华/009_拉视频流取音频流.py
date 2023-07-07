# -*- coding: utf-8  -*-
# -*- author: jokker -*-


import ffmpeg
import time

def extract_audio_from_rtmp(rtmp_url, output_file):
    ffmpeg.input(rtmp_url).output(output_file, format='s16le', acodec='pcm_s16le', ac=1, ar='16000').overwrite_output().run()

# 示例用法

if __name__ == "__main__":

    rtmp_url = 'rtmp://58.240.116.75:51935/swp/TX00100004?secret=0353f7-6b-4889-a715-eb2d1925cc'
    output_file = 'audio.pcm'
    extract_audio_from_rtmp(rtmp_url, output_file)

