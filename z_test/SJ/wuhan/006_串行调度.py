
model_name_list = ['nc', 'fzc', 'kkx']

def exec_one_model(model_name, gpu_id):
    # todo 开启服务 cmd 在指定 GPU 上运行，等待 20s
    # todo 开启检测，检测完毕之后会在指定的文件夹中增加一个文件表明程序已经执行完毕
    pass

for model_name in model_name_list:
    # todo 下面几个是直接调度 cmd 所以几乎不花时间
    exec_one_model(model_name, gpu_id=0)
    exec_one_model(model_name, gpu_id=1)
    exec_one_model(model_name, gpu_id=2)

    # todo 监测上面的代码是不是都执行完了
    have_done_list = [0, 0, 0]
    while True:
        # todo 监测每一个子程序是否执行完，执行完会在一个文件夹中增加一个执行中止的文件
        if all(have_done_list):
            break








