import json
import math
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def main():
    path = "./androidProfiler_data.json"

    def read_json_file(file_path):
        with open(path) as f:
            return json.load(f)

    bar_width = 0.25

    cpu_bar_list = {}
    memory_bar_list = {}
    battery_bar_list = {}
    memory_bar_list_no_outliers = {}
    battery_bar_list_no_outliers = {}

    all_data = read_json_file(path)
    for data in all_data:
        print("\n", data)
        for categories in all_data[data]:

            match categories:
                case "CPU":
                    if 'noOutliers' not in data:
                        cpu_bar_list[data] = all_data[data][categories]
                case "battery":
                    if 'noOutliers' not in data:
                        battery_bar_list[data] = all_data[data][categories]
                    else:
                        battery_bar_list_no_outliers[data] = all_data[data][categories]
                case "memory":
                    if 'noOutliers' not in data:
                        memory_bar_list[data] = all_data[data][categories]
                    else:
                        memory_bar_list_no_outliers[data] = all_data[data][categories]

            mean = sum(all_data[data][categories]) / len(all_data[data][categories])
            variance = sum([((x - mean) ** 2) for x in all_data[data][categories]]) / len(all_data[data][categories])
            res = variance ** 0.5
            z = 1.96
            e = z * res / math.sqrt(len(all_data[data][categories]))
            print("Mean value of " + categories + ": m =", round(mean, 3))
            print("with category: " + categories + " E ", round(e, 3))

    all_plots = {
        "CPU": cpu_bar_list,
        "Memory": memory_bar_list,
        "Memory excluding semi-arbitrary outliers": memory_bar_list_no_outliers,
        "Current": battery_bar_list,
        "Current excluding semi-arbitrary outliers": battery_bar_list_no_outliers
    }

    print(all_plots)
    for title, plot in all_plots.items():
        for key, value in plot.items():
            while len(value) < 30:
                value.append(None)
        df = pd.DataFrame(plot)
        plt.figure(figsize=(15, 6))
        sns.boxplot(data=df, width=0.5)
        plt.title(title)
        plt.grid(True)
        filename = title.replace(" ", "_") + ".svg"
        plt.savefig("Plots/Calculation/" + filename, format='svg')
        plt.show()


main()
