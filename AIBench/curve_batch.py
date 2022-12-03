import re
import numpy as np
import matplotlib.pyplot as plt
import csv
import pandas as pd

def eff(ser, par, p):
    return 1 - (1/(ser+(par/p)))

filename = "res_w128.csv"
matter = [0, 2, 3]
with open(filename) as f:
    reader = csv.reader(f, delimiter=',')
    res = list(reader)
    # datadict = dict()

    # for row in res:
    #     # print(row)
    #     if (row[0] == "proc_num"): continue

    #     tmp = []
    #     for i in matter:
    #         tmp.append(float(row[i]))

    #     if (row[1] not in datadict.keys()):
    #         datadict[row[1]] = list()

    #     datadict[row[1]].append(tmp)

    # print(datadict)


    # batch_size = datadict.keys()
    proc_num = [1, 2, 4, 8, 16, 32, 64, 128]

    y1 = []
    y2 = []
    y4 = []
    y8 = []
    y16 = []
    y32 = []
    y64 = []
    y128 = []

    sy1 = []
    sy2 = []
    sy4 = []
    sy8 = []
    sy16 = []
    sy32 = []
    sy64 = []
    sy128 = []

    for row in res:
        # print(row)
        if (row[0] == "proc_num"): continue

        if (row[1] == '10000'):
            y1.append(float(row[3]))
        elif (row[1] == '20000'):
            y2.append(float(row[3]))
        elif (row[1] == '40000'):
            y4.append(float(row[3]))
        elif (row[1] == '80000'):
            y8.append(float(row[3]))
        elif (row[1] == '160000'):
            y16.append(float(row[3]))
        elif (row[1] == '320000'):
            y32.append(float(row[3]))
        elif (row[1] == '640000'):
            y64.append(float(row[3]))




    # proc_num = [1, 2, 4, 8, 16, 32]

    # for i in range(len(proc_num)):
    #     sy1.append(eff(y1[0], y1[i], proc_num[i]))
    # for i in range(len(proc_num)):
    #     sy2.append(eff(y2[0], y2[i], proc_num[i]))
    # for i in range(len(proc_num)):
    #     sy4.append(eff(y4[0], y4[i], proc_num[i]))
    # for i in range(len(proc_num)):
    #     sy8.append(eff(y8[0], y8[i], proc_num[i]))
    # for i in range(len(proc_num)):
    #     sy16.append(eff(y16[0], y16[i], proc_num[i]))
    # for i in range(len(proc_num)):
    #     sy32.append(eff(y32[0], y32[i], proc_num[i]))
    # for i in range(len(proc_num)):
    #     sy64.append(eff(y64[0], y64[i], proc_num[i]))

    # print(sy1)
    # print(sy2)
    # print(sy4)


    for i in range(len(proc_num)):
        sy1.append(y1[0]/y1[i])
    for i in range(len(proc_num)):
        sy2.append(y2[0]/y2[i])
    for i in range(len(proc_num)):
        sy4.append(y4[0]/y4[i])
    for i in range(len(proc_num)):
        sy8.append(y8[0]/y8[i])        
    for i in range(len(proc_num)):
        sy16.append(y16[0]/y16[i])
    for i in range(len(proc_num)):
        sy32.append(y32[0]/y32[i])
    for i in range(len(proc_num)):
        sy64.append(y64[0]/y64[i])

    # for i in range(len(proc_num)):
    #     sy1.append(y1[0]/y1[i]/proc_num[i])
    # for i in range(len(proc_num)):
    #     sy2.append(y2[0]/y2[i]/proc_num[i])
    # for i in range(len(proc_num)):
    #     sy4.append(y4[0]/y4[i]/proc_num[i])
    # for i in range(len(proc_num)):
    #     sy8.append(y8[0]/y8[i]/proc_num[i])        
    # for i in range(len(proc_num)):
    #     sy16.append(y16[0]/y16[i]/proc_num[i])
    # for i in range(len(proc_num)):
    #     sy32.append(y32[0]/y32[i]/proc_num[i])
    # for i in range(len(proc_num)):
    #     sy64.append(y64[0]/y64[i]/proc_num[i])

        # if (row[1] == '10000'):
        #     y1.append(float(row[2]))
        # elif (row[1] == '20000'):
        #     y2.append(float(row[2]))
        # elif (row[1] == '40000'):
        #     y4.append(float(row[2]))
        # elif (row[1] == '80000'):
        #     y8.append(float(row[2]))
        # elif (row[1] == '160000'):
        #     y16.append(float(row[2]))
        # elif (row[1] == '320000'):
        #     y32.append(float(row[2]))
        # elif (row[1] == '640000'):
        #     y64.append(float(row[2]))


    # print(y1)

    # sy1 = []
    # sy2 = []
    # sy4 = []
    # sy8 = []
    # sy16 = []
    # sy32 = []
    # sy64 = []
    # sy128 = []



    #读取数据
    
    plt.figure(figsize=(10,5))#设置画布的尺寸
    # plt.title('Execution Time-Process Number Diagram',fontsize=20)#标题，并设定字号大小
    plt.title('Speedup-Process Number Diagram',fontsize=20)#标题，并设定字号大小
    # plt.title('Efficiency-Process Number Diagram',fontsize=20)#标题，并设定字号大小
    plt.xlabel(u'Process Number',fontsize=14)#设置x轴，并设定字号大小
    # plt.ylabel(u'Throughput (kb/s)',fontsize=14)#设置y轴，并设定字号大小
    # plt.ylabel(u'Execution Time (ms)',fontsize=14)#设置y轴，并设定字号大小
    plt.ylabel(u'Speedup',fontsize=14)#设置y轴，并设定字号大小
    # plt.ylabel(u'Efficiency',fontsize=14)#设置y轴，并设定字号大小





    #color：颜色，linewidth：线宽，linestyle：线条类型，label：图例，marker：数据点的类型
    # plt.plot(proc_num,y1,color="slategrey",linewidth=1.5,linestyle=':',label='Batch=10000', marker='o')
    # plt.plot(proc_num,y2,color="purple",linewidth=1.5,linestyle='--',label='Batch=20000', marker='+')
    # plt.plot(proc_num,y4,color="dodgerblue",linewidth=1.5,linestyle='-.',label='Batch=40000', marker='*')
    # plt.plot(proc_num,y8,color="seagreen",linewidth=1.5,linestyle='-',label='Batch=80000', marker='s')
    # plt.plot(proc_num,y16,color="orange",linewidth=1.5,linestyle=':',label='Batch=160000', marker='x')
    # plt.plot(proc_num,y32,color="firebrick",linewidth=1.5,linestyle='--',label='Batch=320000', marker='d')
    # plt.plot(proc_num,y64,color="navy",linewidth=1.5,linestyle='-.',label='Batch=640000', marker='h')


    plt.plot(proc_num,sy1,color="slategrey",linewidth=2,linestyle=':',label='Batch=10000', marker='o')
    plt.plot(proc_num,sy2,color="purple",linewidth=1,linestyle='--',label='Batch=20000', marker='+')
    plt.plot(proc_num,sy4,color="dodgerblue",linewidth=1.5,linestyle='-.',label='Batch=40000', marker='*')
    plt.plot(proc_num,sy8,color="seagreen",linewidth=1.5,linestyle='-',label='Batch=80000', marker='s')
    plt.plot(proc_num,sy16,color="orange",linewidth=1.5,linestyle=':',label='Batch=160000', marker='x')
    plt.plot(proc_num,sy32,color="firebrick",linewidth=1.5,linestyle='--',label='Batch=320000', marker='d')
    plt.plot(proc_num,sy64,color="navy",linewidth=1.5,linestyle='-.',label='Batch=640000', marker='h')
    
    plt.legend(loc=3)#图例展示位置，数字代表第几象限

    plt.show()
    # plt.savefig("./time.png", dpi=300)