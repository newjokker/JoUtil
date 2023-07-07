# -*- coding: utf-8  -*-
# -*- author: jokker -*-


import sounddevice as sd
import numpy as np
from pydub import AudioSegment


def play_pcm_file(pcm_file):
    # 从 PCM 文件中读取原始音频数据
    with open(pcm_file, 'rb') as f:
        pcm_data = f.read()

    # 将字节数据转换为 NumPy 数组
    pcm_array = np.frombuffer(pcm_data, dtype=np.int16)

    # 播放 PCM 音频数据
    sd.play(pcm_array, samplerate=16000)
    # sd.play(pcm_array, samplerate=48000)

    # 等待播放完成
    sd.wait()

def convert_m4a_to_pcm(m4a_file, pcm_file):
    # 读取 M4A 文件
    audio = AudioSegment.from_file(m4a_file, format='m4a')

    audio = audio.set_frame_rate(16000)

    # 将音频数据转换为原始 PCM 数据
    pcm_data = audio.raw_data

    # 保存为 PCM 文件
    with open(pcm_file, 'wb') as f:
        f.write(pcm_data)


if __name__ == "__main__":

    """
    1、识别关键字“用户同意换表”
    2、识别关键字“用户家中有电”
    （×）3、识别不文明用语：常规不文明用语的范畴
    
    """


    """
    * 关键词识别不可用 
    * （1）虽然可以自定义关键词，但是当识别语音较长时非常耗时，一秒的语音就要一秒的识别时间
    * （2）被是被的语音中不能有多余的词语，比如识别 “用户确定加重有电|没电” 当被识别的内容中有较多和被是被内容不相关的语音时，识别效果较差，[当语音中没有其他内容时，识别率尚可接受] 
    """



    # # 指定输入的 M4A 文件和输出的 PCM 文件
    # m4a_file = r"C:\Users\14271\Desktop\temp\test8.m4a"
    # pcm_file = r"C:\Users\14271\Desktop\temp\test8.pcm"
    #
    # # 调用转换函数
    # convert_m4a_to_pcm(m4a_file, pcm_file)


    # 指定要播放的 PCM 文件路径
    # pcm_file = r'C:\Users\14271\Desktop\temp\ddhghlj.pcm'
    pcm_file = r'C:\Users\14271\Desktop\temp\del.pcm'

    # 调用播放函数
    play_pcm_file(pcm_file)










