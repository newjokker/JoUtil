import re

# 定义读取日志文件的函数
def analyze_log(file_path):
    with open(file_path, 'r') as file:
        logs = file.readlines()

    # 用于存储每个步骤的时间记录
    timings = {}
    pattern_start = re.compile(r'info_with_timestamp\s+timestamp_start_(\w+)\s+->\s+([\d.]+)')
    pattern_end = re.compile(r'info_with_timestamp\s+timestamp_end_(\w+)\s+->\s+([\d.]+)')

    for line in logs:
        # 匹配start记录
        start_match = pattern_start.search(line)
        if start_match:
            # print(line)
            name = start_match.group(1).strip()
            timestamp_str = line.split('->')[-1].strip()
            timestamp = float(timestamp_str)
            
            # 记录开始时间
            if name not in timings:
                timings[name] = {'start': timestamp, 'durations': []}
            else:
                timings[name]['start'] = timestamp  # 更新开始时间

        # 匹配end记录
        end_match = pattern_end.search(line)
        if end_match:
            name = end_match.group(1).strip()
            timestamp_str = line.split('->')[-1].strip()
            timestamp = float(timestamp_str)

            # 如果有对应的开始时间，则计算时间差
            if name in timings and 'start' in timings[name]:
                start_time = timings[name]['start']
                duration = timestamp - start_time
                timings[name]['durations'].append(duration)
                # 清除已处理的记录
                del timings[name]['start']

    # 指定的排序顺序
    specified_order = ["detect", "loop", "run_dete", "calculate_hilbert", "classify", "filtfilt", "process_prpd_data", "filter_run"]

    # 根据指定的顺序排序
    sorted_timings = sorted(timings.items(), key=lambda x: specified_order.index(x[0]) if x[0] in specified_order else len(specified_order))

    # 输出每个步骤的平均耗时和总耗时
    for name, data in sorted_timings:
        if 'durations' in data:
            total_time = sum(data['durations'])
            average_time = total_time / len(data['durations']) if data['durations'] else 0
            print(f"{name:<30} 总耗时: {total_time:.15f} 秒, 平均耗时: {average_time:.15f} 秒, 统计个数: {len(data['durations'])} \n")
            # print(f"{name:<30} 总耗时: {total_time} 秒, 平均耗时: {average_time} 秒, 统计个数: {len(data['durations'])} \n")


if __name__ == "__main__":

    #FIXME: 支持多进程，增加 process id ，一样的 id 放在一起进行解析
    
    # TODO: 识别日志之间的嵌套关系，生成日志时间分析图


    # 使用示例
    analyze_log('/home/ldq/Code/SaturnVoiceData/app/test/log.log')
    # analyze_log('/home/ldq/Code/SaturnTools/test_data/log_true.log')

