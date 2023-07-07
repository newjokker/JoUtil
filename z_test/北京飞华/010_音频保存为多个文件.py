# -*- coding: utf-8  -*-
# -*- author: jokker -*-


import time
from ffmpeg import input as ffmpeg_input, output as ffmpeg_output


def save_audio_from_rtmp(rtmp_url, output_file_prefix):
    output_file = output_file_prefix + "_{}.pcm"

    # 初始化计时器
    start_time = time.time()
    duration = 5  # 保存音频的时间间隔（单位：秒）

    # 创建 ffmpeg 输入流
    input_stream = ffmpeg_input(rtmp_url)

    # 初始化计数器
    file_counter = 0
    elapsed_time = 0

    while True:
        # 创建新的输出文件名
        output_filename = output_file.format(file_counter)

        # 创建 ffmpeg 输出流
        output_stream = ffmpeg_output(input_stream, output_filename, format='s16le', acodec='pcm_s16le', ac=1, ar='16000')
        output_stream = output_stream.overwrite_output()

        # 运行 ffmpeg 命令
        output_stream.run()

        # 增加文件计数器
        file_counter += 1

        # 计算已经过去的时间
        elapsed_time += duration

        # 等待直到达到下一个保存时间点
        sleep_time = start_time + elapsed_time - time.time()
        if sleep_time > 0:
            time.sleep(sleep_time)

        # 重新开始计时
        start_time = time.time()



if __name__ == "__main__":

    rtmp_url = 'rtmp://58.240.116.75:51935/swp/TX00100004?secret=0353f7-6b-4889-a715-eb2d1925cc'
    output_file = 'audio'
    save_audio_from_rtmp(rtmp_url, output_file)

