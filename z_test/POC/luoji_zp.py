'''
方案一：
数量上面先把单相三相分一下
直接卡各颜色种类个数，如果达标，直接给过

方案二：
考虑到会有下方出现误召回
对框的 左上角位置 加一个升序排序后 取前5（单相）  前min（10， 框的总数量），
挨个数颜色
单相限制两两成对
三相限制2*3或3*3   +n
'''

def convert_format():
    '''args:
    pred:输出结果
    
    return:
        color2num(dict)
        num of box
        box_list                 [[x_left,y_top,w,h 'color'], ...] (list(list))
    '''
    return

def disc_single_phase_1(color2num):
    target_color=[] #不确定要不要卡颜色

    num_of_double=0
    for k,v in color2num.items():
        # if k in target_color:
        if v>=2:
            num_of_double+=1
    
    return True if num_of_double==2 else False

def disc_three_phase_1(color2num):
    target_color=[] #不确定要不要卡颜色
    num_of_double=0
    for k,v in color2num.items():
        # if k in target_color:
        if v>=2:
            num_of_double+=1
    
    return True if num_of_double>=3 else False

def clean_boxList(box_list):
    '''基于假设，下方误检出来的框比他左上方的框高度上高出之上大半个框高，二正常不会
    '''
    box_list=sorted(box_list, lambda x:box_list[0])
    box_list_n=[box_list[0]]
    for i in range(1,len(box_list)):
        if abs(box_list[i][1]-box_list[i-1][1])> box_list[i-1][3]*0.7:
            continue
        else:
            box_list_n.append(box_list[i])
    return box_list_n

def disc_single_phase_2():
    #哥，你来吧，就是清洗过的框，从左往右数，限定颜色相同，最后得到，（2，2，n）组合
    #下面那个三相就是（2，2，2，n）或者（3，3，3，n）组合
    return

def disc_three_phase_2():
    return





def main(pred):
    #1、输出结果格式调整
    color2num, box_num, box_list=convert_format(pred)

    #2、单相、三相判断后进各自逻辑

    #2.1 我直接卡数量，》》》》但是是否需要限定颜色组成《《《
    if box_num<4:
        ans=False
    elif 4<=box_num<6:
        ans=disc_single_phase_1(color2num)
    else:
        ans=disc_three_phase_1(color2num)
    # return ans

    #2.2 排序数数量,单相数4-5个，三相数7-10个
    #因为下方会有误召回，所以对左上角位置做升序排序，将y大于前一个框的y+(h*2/3)的框踢出去不带他玩
    box_list=clean_boxList(box_list)

    if box_num<4:
        ans=False
    elif 4<=box_num<6:
        ans=disc_single_phase_2(box_list)
    else:
        ans=disc_three_phase_2(box_list)

    return ans

