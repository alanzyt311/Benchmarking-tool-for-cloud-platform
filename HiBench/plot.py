import matplotlib
import matplotlib.pyplot as plt

# report_path = "/home/team3/Evaluation/linear/report/linear_mapre.report"
report_path = "./a/pca/pr_mapre.report"
# path to save the figure
save_path = "../a/pca"
# # values that will be assigned to the changing scale
# para_scale_settings = ["tiny", "small", "large", "huge", "gigantic"]
# # values that will be assigned to the changing mapper
# para_mapper_settings = [4]
# # values that will be assigned to the changing reducer
# para_reducer_settings = [4]
para_scale_settings = ["samll"]
para_mapper_settings = [1,2,3,4,8,12,16]
para_reducer_settings = [1]
# m1r1_time = 48.901
m1r2_time = 130.977

mapreducer = list()

# name of the output parameter that you want to fetch from the report
output_thro = "Throughput(bytes/s)"
output_dura = "Duration(s)"

datasize = list()
duration = list()
throughput = list()
speed_up = list()
efficiency = list()

def fetch_data():
    try:
        with open(report_path, "r") as r_f:
            flist = r_f.readlines()
            for line in flist:
                split = line.split()
                # print(split)
                if (("Type" in split) or (len(split) == 0)):
                    # skip first line and empty line
                    continue
                datasize.append(float(split[3]))
                duration.append(float(split[4]))
                throughput.append(float(split[5]))
    except FileNotFoundError:
        print("File not found or cannot be opened!\n")

def cal_speedup():
    single_node_exe_time = m1r2_time
    for i in range(0,7):
        speed_up.append(float(single_node_exe_time) / float(duration[i]))

def cal_efficiency():
    for i in range(0,7):
        efficiency.append(float(speed_up[i]) / float(para_mapper_settings[i]))

# generate the plot with mapper and reducer change
def plot_mapre():
    plt.rcParams['axes.labelsize'] = 12  # xy轴label的size
    plt.rcParams['xtick.labelsize'] = 5  # x轴ticks的size
    plt.rcParams['ytick.labelsize'] = 12  # y轴ticks的size
    # plt.rcParams['legend.fontsize'] = 12  # 图例的size

    # 设置柱形的间隔
    width = 0.3  # 柱形的宽度
    x1_list = []
    x2_list = []
    for i in range(len(para_mapper_settings)*len(para_reducer_settings)):
        x1_list.append(i)
        x2_list.append(i + width)

    # 创建图层/
    fig, ax1 = plt.subplots()

    # 设置左侧Y轴对应的figure
    # in the bar chart, x, y must be of the same length
    assert(len(x1_list) == len(duration))
    ax1.set_ylabel('Duration(s)')
    ax1.set_ylim(min(duration)*0.8, max(duration)*1.2)  # 设置纵坐标范围
    ax1.bar(x1_list, duration, width=width,
            color='lightseagreen', align='edge', label='Duration')

    ax1.set_xticklabels(ax1.get_xticklabels())  # 设置共用的x轴

    # 设置右侧Y轴对应的figure
    assert(len(x2_list) == len(throughput))
    ax2 = ax1.twinx()
    ax2.set_ylabel('Throughput(bytes/s)')
    ax2.set_ylim(min(throughput)*0.8, max(throughput)*1.1)  # 设置纵坐标范围
    ax2.bar(x2_list, throughput, width=width, color='tab:blue',
            align='edge', tick_label=mapreducer, label='Throughput')

    for tick in ax1.get_xticklabels():  # 将横坐标倾斜30度，纵坐标可用相同方法
        tick.set_rotation(30)

    # 图例
    ax1.legend(bbox_to_anchor=(1.05, 1.05), loc='upper left', borderaxespad=0.)
    ax2.legend(bbox_to_anchor=(1.05, 1.05), loc='lower left', borderaxespad=0.)
    plt.tight_layout()
    plt.savefig(f"{save_path}/mapre_r2.png", dpi=1024)
    # plt.show()


# generate the plot with scale changes
def plot_scale():
    plt.rcParams['axes.labelsize'] = 12  # xy轴label的size
    plt.rcParams['xtick.labelsize'] = 5  # x轴ticks的size
    plt.rcParams['ytick.labelsize'] = 12  # y轴ticks的size
    plt.rcParams['legend.fontsize'] = 10  # 图例的size

    # 设置柱形的间隔
    width = 0.3  # 柱形的宽度
    x1_list = []
    x2_list = []
    for i in range(len(para_scale_settings)):
        x1_list.append(i)
        x2_list.append(i + width)

    # 创建图层/
    fig, ax1 = plt.subplots()

    # 设置左侧Y轴对应的figure
    assert(len(x1_list) == len(duration))
    ax1.set_ylabel('Duration(s)')
    ax1.set_ylim(min(duration)*0.8, max(duration)*1.2)  # 设置纵坐标范围
    ax1.bar(x1_list, duration, width=width,
            color='lightseagreen', align='edge', label='Duration')
    ax1.set_xticklabels(ax1.get_xticklabels())  # 设置共用的x轴

    # 设置右侧Y轴对应的figure
    assert(len(x2_list) == len(throughput))
    ax2 = ax1.twinx()
    ax2.set_ylabel('Throughput(bytes/s)')
    ax2.set_ylim(min(throughput)*0.8, max(throughput)*1.1)  # 设置纵坐标范围
    ax2.bar(x2_list, throughput, width=width, color='tab:blue',
            align='edge', tick_label=para_scale_settings, label='Throughput')

    for tick in ax1.get_xticklabels():  # 将横坐标倾斜30度，纵坐标可用相同方法
        tick.set_rotation(30)

    # 图例
    ax1.legend(bbox_to_anchor=(1.05, 1.05), loc='upper left', borderaxespad=0.)
    ax2.legend(bbox_to_anchor=(1.05, 1.05), loc='lower left', borderaxespad=0.)
    plt.tight_layout()
    plt.savefig(f"{save_path}/scale_8_4.png", dpi=1024)
    # plt.show()


# generate the plot with mapper and reducer change
def plot_spe_eff():
    plt.rcParams['axes.labelsize'] = 12  # xy轴label的size
    plt.rcParams['xtick.labelsize'] = 5  # x轴ticks的size
    plt.rcParams['ytick.labelsize'] = 12  # y轴ticks的size
    # plt.rcParams['legend.fontsize'] = 12  # 图例的size

    # 设置柱形的间隔
    width = 0.3  # 柱形的宽度
    x1_list = []
    x2_list = []
    for i in range(len(para_mapper_settings)*len(para_reducer_settings)):
        x1_list.append(i)
        x2_list.append(i + width)

    # 创建图层/
    fig, ax1 = plt.subplots()

    # 设置左侧Y轴对应的figure
    # in the bar chart, x, y must be of the same length
    assert(len(x1_list) == len(speed_up))
    ax1.set_ylabel('Speed Up')
    ax1.set_ylim(min(speed_up)*0.8, max(speed_up)*1.2)  # 设置纵坐标范围
    ax1.bar(x1_list, speed_up, width=width,
            color='lightseagreen', align='edge', label='Speed Up')

    ax1.set_xticklabels(ax1.get_xticklabels())  # 设置共用的x轴

    # 设置右侧Y轴对应的figure
    assert(len(x2_list) == len(efficiency))
    ax2 = ax1.twinx()
    ax2.set_ylabel('Efficiency')
    ax2.set_ylim(min(efficiency)*0.8, max(efficiency)*1.1)  # 设置纵坐标范围
    ax2.bar(x2_list, efficiency, width=width, color='tab:blue',
            align='edge', tick_label=mapreducer, label='Efficiency')

    for tick in ax1.get_xticklabels():  # 将横坐标倾斜30度，纵坐标可用相同方法
        tick.set_rotation(30)

    # 图例
    ax1.legend(bbox_to_anchor=(1.05, 1.05), loc='upper left', borderaxespad=0.)
    ax2.legend(bbox_to_anchor=(1.05, 1.05), loc='lower left', borderaxespad=0.)
    plt.tight_layout()
    plt.savefig(f"{save_path}/SpeedUp_Efficiency.png", dpi=1024)
    # plt.show()


def main():
    fetch_data()
    cal_speedup()
    print(speed_up)
    cal_efficiency()
    print(efficiency)

    # create x axis for mapre plots
    for i in para_mapper_settings:
        for j in para_reducer_settings:
            mapreducer.append(f"m[{i}]-r[{j}]")

    plot_mapre()
    # plot_scale()
    plot_spe_eff()


main()