import os
import time
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

# conf_path = "/home/team3/Evaluation/hibench_copy.conf"
# conf_path = "/home/team3/github/HiBench/conf/hibench_copy.conf"
conf_path = "/home/team3/github/HiBench/conf/hibench.conf"

sh_prepare_path = "/home/team3/github/HiBench/bin/workloads/micro/wordcount/prepare/prepare.sh"
sh_run_path = "/home/team3/github/HiBench/bin/workloads/micro/wordcount/hadoop/run.sh"
report_path = "/home/team3/github/HiBench/report/hibench.report"
monitor_path = "/home/team3/github/HiBench/report/wordcount/hadoop/monitor.html"

# name of the parameter that you want to change
conf_scale = "hibench.scale.profile"
conf_mapper = "hibench.default.map.parallelism"
conf_reducer = "hibench.default.shuffle.parallelism"

para_scale_settings =   ["tiny","small"] # values that will be assigned to the changing scale
# options: tiny, small, large, huge, gigantic, bigdata
para_mapper_settings =  [8] # values that will be assigned to the changing mapper
para_reducer_settings = [4] # values that will be assigned to the changing reducer

# output_para_name = "Throughput(bytes/s)" # name of the output parameter that you want to fetch from the report
output_para_name = "Duration(s)"

monitor_cpu = "id=\"csv_cpu_overall\""
monitor_disk = "id=\"csv_diskio_overall\""
monitor_memory = "id=\"csv_memory_overall\""

cpu_stop = "id=\"csv_network_heatmap\""
disk_stop = "id=\"csv_memory_heatmap\""
memory_stop = "id=\"csv_procload_heatmap\""

exp_results = dict() # store the experiment results from for plotting
monitor_cpu_result = dict() # store the experiment cpu_results for plotting
monitor_disk_result = dict() # store the experiment disk_results for plotting
monitor_memory_result = dict() # store the experiment memory_results for plotting
speed_up = list()
efficiency = list()

# fetch results from monitor.html file and store into monitor_results
def get_monitor_result():
    with open(monitor_path, "r") as r_f:

        print("Successfully open monitor file.\n")
        flist=r_f.readlines()
        cpu_flag = 0
        disk_flag = 0
        memory_flag = 0

        for line in flist:
            # print(line)
            split = line.split()

            # 1. Read CPU OVERALL USAGE
            if (monitor_cpu in split):
                cpu_flag = 1
                continue

            if (cpu_stop in split):
                cpu_flag = 0
                continue

            if (cpu_flag == 1):
                # print("CPU:")
                if (line[(len(line)-7):(len(line)-1)] == "</pre>"):
                    line = line[0:(len(line)-7)]

                # TODO: add the whole line to monitor_cpu_result
                # print(line)

                continue


            # 2. Read DISKIO OVERALL USAGE
            if (monitor_disk in split):
                disk_flag = 1
                continue

            if (disk_stop in split):
                disk_flag = 0
                continue

            if (disk_flag == 1):
                # print("DISKO:")
                if (line[(len(line)-7):(len(line)-1)] == "</pre>"):
                    line = line[0:(len(line)-7)]

                # TODO: add the whole line to monitor_disk_result
                # print(line)
                continue   


            # 3. Read MEMORY OVERALL USAGE
            if (monitor_memory in split):
                memory_flag = 1
                continue

            if (memory_stop in split):
                memory_flag = 0
                continue

            if (memory_flag == 1):
                # print("MEMORY:")
                if (line[(len(line)-7):(len(line)-1)] == "</pre>"):
                    line = line[0:(len(line)-7)]

                # TODO: add the whole line to monitor_memory_result
                # print(line)
                continue

# perform the experiment multiple times
# each time, with a different parameter setting specified in para_settings
def run_experiment():
    #########################
    ####      Part1      ####
    #########################
    # modify parameters in the configuration file ()
    for i in para_scale_settings: # scale
        for j in para_mapper_settings: # mapper
            for k in para_reducer_settings: # reducer
                # modify parameters in the configuration file use para_settings
                # TODO: find parameter and modify it
                time.sleep(5)
                print(f"Current parameter settings [scale:] {i} [mapper:] {j} [reducer:] {k}\n")
                try:
                    with open(conf_path, "r+") as c_f:
                        print("Successfully open configuration file.\n")
                        flist=c_f.readlines()
                        flist[2]=conf_scale + "                 " + i + "\n"
                        flist[4]=conf_mapper + "         " + str(j) + "\n"
                        flist[7]=conf_reducer + "     " + str(k) + "\n"

                        c_f=open(conf_path,"w+")
                        c_f.writelines(flist)
                except FileNotFoundError:
                    print("File not found or cannot be opened!")

                #########################
                ####      Part2      ####
                #########################
                # invoke and execute shell file, including prepare.sh and run.sh
                try:
                    status1 = os.system("sh" + " " + sh_prepare_path)
                    status2 = os.system("sh" + " " + sh_run_path)
                    assert(status1 == 0 & status2 == 0) # successfully run the shell script
                    print("Finish execution!\n")
                except RuntimeError:
                    print("Execution failed!\n")

                # optional, wait for some time, maybe report is being generated
                print("Start waiting...\n")
                time.sleep(3) # can be changed
                print("Finish waiting...\n")

                #########################
                ####      Part3      ####
                #########################
                # fetch results from corresponding report file and store into exp_results
                try:
                    with open(report_path, "r") as r_f:
                        print("Successfully open report file.\n")
                        ouput_para_col_idx = -1 # col of corresponding output_para_name 
                        for line in r_f:
                            line = line.split()
                            # print(line)
                            if (output_para_name in line):
                                ouput_para_col_idx = line.index(output_para_name)
                                print(f"[Find out the parameter with idx {ouput_para_col_idx}]: {line[ouput_para_col_idx]} \n")
                        else: # end of file
                            if (ouput_para_col_idx != -1):
                                # add newly generated results into exp_results
                                # TODO: add back to results
                                exp_results[f"Current settings {i} {j} {k}"] = line[ouput_para_col_idx]
                except FileNotFoundError:
                    print("File not found or cannot be opened!\n")

                #########################
                ####      Part4      ####
                #########################
                # fetch results from monitor.html file and store into monitor_results
                try:
                    get_monitor_result()
                except FileNotFoundError:
                    print("File not found or cannot be opened!\n")

# use the exp_results to plot rectagular graphs
def plot_rect():
    print(exp_results)
    print("\n")
 
    # TODO: plot function
    labels = list(exp_results.keys())
    x = np.arange(len(labels)) # the label locations
    values = list(exp_results.values())
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width/2, values, width, label=output_para_name)

    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()
    ax.set_ylabel(output_para_name)
    ax.set_title("Experiment settings")

    def autolabel(rects):
        """Attach a text label above each bar in *rects*, displaying its height."""
        for rect in rects:
            height = rect.get_height()
            ax.annotate("{}".format(height),
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha="center", va="bottom")

    autolabel(rects1)
    fig.tight_layout()
    # plt.show()
    fig.savefig("/home/team3/Evaluation/evaluate.png", dpi = 1024)

def cal_speedup():
    single_node_exe_time = list(exp_results.values())[0]
    multi_nodes_exe_time = [x for x in list(exp_results.values())]
    speed_up = [ (float(single_node_exe_time) / float(i)) for i in multi_nodes_exe_time]
    print(speed_up)
    return speed_up

def cal_efficiency():
    for m in para_mapper_settings:
        efficiency = [(float(i) / float(m)) for i in speed_up]
    print(efficiency)
    return efficiency

# main function
def main():
    run_experiment()
    cal_speedup()
    cal_efficiency()
    plot_rect()
    print("All tasks finished!\n")

main()
