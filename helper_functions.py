‘‘’
本文件包含多个实用的函数，用于处理常见的数据操作任务。所有内容均由作者自己所写，包括实验课作业、项目需求、突发奇想等

包含的功能：
1、生成斐波那契数列
2、同时获取列表的最大值和最小值

’’’

‘‘‘
生成斐波那契数列
n:所需斐波那契数列长度

fibon_list：斐波那契数列
fibon_num：最后一位斐波那契数
’’’
def fibonacci_variant(n):
    x1, x2 = 1, 1
    fibon_list = []
    fibon_list.append(x1)
    fibon_list.append(x2)
    if n <= 2:
        return 1
    
    for _ in range(n - 2):
        if x1 > x2:
            x2 += x1
            fibon_list.append(x2)
        else:
            x1 += x2
            fibon_list.append(x1)
    
    fibon_num = max(x1,x2)
    return fibon_list, fibon_num

‘‘‘
同时寻找出列表的最大值和最小值
seq：目标列表

min：列表中最小值
max：列表中最大值
’’’

def find_min_max(seq):
    min = seq[0]
    max = seq[0]
    for i in seq:
        if i < min:
            min = i
        elif i > max:
            max = i
    return min,max








