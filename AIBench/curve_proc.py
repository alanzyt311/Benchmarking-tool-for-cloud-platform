import re
import numpy as np
import matplotlib.pyplot as plt
import csv
import pandas as pd

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
    # proc_num = [1, 2, 4, 8, 16, 32, 64, 128]
    batch_size = [10, 20, 40, 80, 160, 320, 640]

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

    mode = 3
    for row in res:
        # print(row)
        # if (row[0] == "proc_num"): continue

        if (row[0] == '1'):
            y1.append(float(row[mode]))
        elif (row[0] == '2'):
            y2.append(float(row[mode]))
        elif (row[0] == '4'):
            y4.append(float(row[mode]))
        elif (row[0] == '8'):
            y8.append(float(row[mode]))
        elif (row[0] == '16'):
            y16.append(float(row[mode]))
        elif (row[0] == '32'):
            y32.append(float(row[mode]))
        elif (row[0] == '64'):
            y64.append(float(row[mode]))
        elif (row[0] == '128'):
            y128.append(float(row[mode]))

    print(y1)
    print(y2)


    # proc_num = [1, 2, 4, 8, 16, 32]

    # for i in range(len(proc_num)):
    #     sy1.append(y1[0]/y1[i])
    # for i in range(len(proc_num)):
    #     sy2.append(y2[0]/y2[i])
    # for i in range(len(proc_num)):
    #     sy4.append(y4[0]/y4[i])
    # for i in range(len(proc_num)):
    #     sy8.append(y8[0]/y8[i])        
    # for i in range(len(proc_num)):
    #     sy16.append(y16[0]/y16[i])
    # for i in range(len(proc_num)):
    #     sy32.append(y32[0]/y32[i])
    # for i in range(len(proc_num)):
    #     sy64.append(y64[0]/y64[i])

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
    # plt.title('Throughput-Batch Size Diagram',fontsize=20)#标题，并设定字号大小
    plt.title('Execution Time-Batch Size Diagram',fontsize=20)#标题，并设定字号大小


    # plt.title('Speedup-Process Number Diagram',fontsize=20)#标题，并设定字号大小
    # plt.title('Efficiency-Process Number Diagram',fontsize=20)#标题，并设定字号大小

    # plt.xlabel(u'Process Number',fontsize=14)#设置x轴，并设定字号大小
    plt.xlabel(u'Batch Size (x1000)',fontsize=14)#设置x轴，并设定字号大小

    # plt.ylabel(u'Throughput (kb/s)',fontsize=14)#设置y轴，并设定字号大小
    plt.ylabel(u'Execution Time (ms)',fontsize=14)#设置y轴，并设定字号大小
    # plt.ylabel(u'Speedup',fontsize=14)#设置y轴，并设定字号大小
    # plt.ylabel(u'Efficiency',fontsize=14)#设置y轴，并设定字号大小





    #color：颜色，linewidth：线宽，linestyle：线条类型，label：图例，marker：数据点的类型
    plt.plot(batch_size,y1,color="slategrey",linewidth=1.5,linestyle=':',label='Proc=1', marker='o')
    plt.plot(batch_size,y2,color="purple",linewidth=1.5,linestyle='--',label='Proc=2', marker='+')
    plt.plot(batch_size,y4,color="dodgerblue",linewidth=1.5,linestyle='-.',label='Proc=4', marker='*')
    plt.plot(batch_size,y8,color="seagreen",linewidth=1.5,linestyle='-',label='Proc=8', marker='s')
    plt.plot(batch_size,y16,color="orange",linewidth=1.5,linestyle=':',label='Proc=16', marker='x')
    plt.plot(batch_size,y32,color="firebrick",linewidth=1.5,linestyle='--',label='Proc=32', marker='d')
    plt.plot(batch_size,y64,color="navy",linewidth=1.5,linestyle='-.',label='Proc=64', marker='h')
    plt.plot(batch_size,y128,color="deeppink",linewidth=1.5,linestyle=':',label='Proc=128', marker='p')



    # plt.plot(batch_size,sy1,color="slategrey",linewidth=2,linestyle=':',label='Batch=10000', marker='o')
    # plt.plot(batch_size,sy2,color="purple",linewidth=1,linestyle='--',label='Batch=20000', marker='+')
    # plt.plot(batch_size,sy4,color="dodgerblue",linewidth=1.5,linestyle='-.',label='Batch=40000', marker='*')
    # plt.plot(batch_size,sy8,color="seagreen",linewidth=1.5,linestyle='-',label='Batch=80000', marker='s')
    # plt.plot(batch_size,sy16,color="orange",linewidth=1.5,linestyle=':',label='Batch=160000', marker='x')
    # plt.plot(batch_size,sy32,color="firebrick",linewidth=1.5,linestyle='--',label='Batch=320000', marker='d')
    # plt.plot(batch_size,sy64,color="navy",linewidth=1.5,linestyle='-.',label='Batch=640000', marker='h')
    
    plt.legend(loc=2)#图例展示位置，数字代表第几象限

    plt.show()
    # plt.savefig("./time.png", dpi=300)