
# todo 不同大小的模型运行排序问题


def order(l):
    for i in range(len(l)):
        for j in range(len(l)-i-1):
            if(l[i]<l[j+i+1]):
                tmp = l[i]
                l[i] = l[j+i+1]
                l[j + i + 1] = tmp
    return l

def solution(list):
    unit = []
    if(len(list)==0):
        return None
    elif(list[0]>maxValue):
        wasted.append(list[0])
        GlobalList.pop(0)
        return solution(GlobalList)
    else:
        left = maxValue - list[0]
        tmpList = []
        if(left in list[1:]):
            tmpList = list[list.index(left):]
        else:
            for i in range(len(list)-1):
                if(list[-i-1]<=left):
                    tmpList.append(list[-i-1])
        unit.append(list[0])
        index = 0
        while(len(tmpList) != 0 and index<len(tmpList) and tmpList[index]<=left):
            unit.append(tmpList[index])
            left -= tmpList[index]
            index+=1
        return unit

def main(list, maxV):
    print("原数组之前为：" + str(list))
    global GlobalList,maxValue,solved,wasted
    maxValue = maxV
    GlobalList = order(list)
    print("重新排序后为：" + str(GlobalList))
    tmpUnit = solution(GlobalList)
    while((tmpUnit)!=None):
        for unit in tmpUnit:
            GlobalList.pop(GlobalList.index(unit))
        solved.append(tmpUnit)
        tmpUnit = solution(GlobalList)
    print("最大值为 "+str(maxValue)+" 的情况下，推荐的组合为：" +str(solved))
    print("溢出的值包括："+str(wasted))

wasted = []
solved = []
GlobalList = []
maxValue = 0

main([10,9,5,4,2,2,2,1,3,5,6,7,6,5,4,3,25], 11)