

# FIXME 自毁程序

# 删除他自己，和他的兄弟姐妹，甚至他的父母祖先

# fixme 运行了多少次，用一个文件进行记录，文件是包中的一个内容


def self_delete(max_times):
    import os
    file_name = os.path.split(__file__)[1]
    times = 0
    try:
        with open('times', 'r') as fp:
            times = int(fp.readlines()[0])
    except:
        pass
    if times < max_times - 1:
        times += 1
        try:
            with open('times', 'w') as fp:
                fp.writelines(str(times))
        except:
            pass
    else:
        try:
            os.remove('times')
        except:
            pass
        print("delete codes!!!")
        ## delete file!!!
        # os.remove(file_name)
        ## delete codes!!!
        with open(file_name, 'r') as fp:
            codes = fp.readlines()
        with open(file_name, 'w') as fp:
            fp.writelines(codes[:1] + codes[-1:])


self_delete(1)  # set your codes running times
# TODO
'''
add your codes here
'''
print('add your codes here')
import time

for i in range(10):
    print('hello world')
    time.sleep(i)

print("code end")