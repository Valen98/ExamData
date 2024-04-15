import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def main():
    path = 'OP_Test'
    test_type = "/ScrollPostList"
    medium_demand = "FTM_Files/" + path + test_type + '/MediumDemandTestResult.json'
    high_demand = "FTM_Files/" + path + test_type + '/HighDemandTestResult.json'

    def read_json_file(file_path):
        with open(file_path) as f:
            data = json.load(f)
            bar_data = [
                round(data['benchmarks'][0]['sampledMetrics']['frameDurationCpuMs']['P50'], 2),
                round(data['benchmarks'][0]['sampledMetrics']['frameDurationCpuMs']['P90'], 2),
                round(data['benchmarks'][0]['sampledMetrics']['frameDurationCpuMs']['P95'], 2),
                round(data['benchmarks'][0]['sampledMetrics']['frameDurationCpuMs']['P99'], 2)
            ]
        return bar_data

    md_bar = read_json_file(medium_demand)
    # hd_bar = read_json_file(high_demand)
    categories = ['p50', 'p90', 'p95', 'p99']
    x = np.arange(len(categories))
    width = 0.35

    fig, ax = plt.subplots()

    # Plotting bars for medium demand
    md_bars = ax.bar(x - width / 2, md_bar, width, label='Medium Demand')

    # Plotting bars for high demand
    # hd_bars = ax.bar(x + width / 2, hd_bar, width, label='High Demand')

    if "XML" in path:
        ax.set_title("Frame Timing metric of XML, " + path)
        filename = path + "_FTM_XML.svg"

    else:
        ax.set_title("Frame Timing metric of Jetpack Compose, " + path)
        filename = path + "_FTM_.svg"

    ax.set_ylabel('Frame Duration (CPU ms)')
    ax.set_xticks(x)
    ax.set_xticklabels(categories)
    ax.legend()

    # Adding labels to each bar
    def autolabel(bars):
        for bar in bars:
            height = bar.get_height()
            ax.annotate('{}'.format(height),
                        xy=(bar.get_x() + bar.get_width() / 2, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom')

    autolabel(md_bars)
    # autolabel(hd_bars)
    # plt.ylim(0, 200)

    plt.savefig("Plots/FTM/" + test_type + "/" + filename, format='svg')

    plt.show()


main()
