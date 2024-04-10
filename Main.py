import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def main():
    path = '30_OP_XML_Test'
    low_demand = "Startup_Files/" + path + '/LowDemandTestResult.json'
    medium_demand = "Startup_Files/" + path + '/MediumDemandTestResult.json'
    high_demand = "Startup_Files/" + path + '/HighDemandTestResult.json'

    # Read the JSON file
    with open(low_demand) as f:
        ld_data = json.load(f)
        ld_runs = ld_data['benchmarks'][0]['metrics']['timeToInitialDisplayMs']['runs']
        ld_low = ld_data['benchmarks'][0]['metrics']['timeToInitialDisplayMs']['minimum']
        ld_median = ld_data['benchmarks'][0]['metrics']['timeToInitialDisplayMs']['median']
        ld_max = ld_data['benchmarks'][0]['metrics']['timeToInitialDisplayMs']['maximum']
    with open(medium_demand) as f:
        md_data = json.load(f)
        md_runs = md_data['benchmarks'][0]['metrics']['timeToInitialDisplayMs']['runs']
        md_low = md_data['benchmarks'][0]['metrics']['timeToInitialDisplayMs']['minimum']
        md_median = md_data['benchmarks'][0]['metrics']['timeToInitialDisplayMs']['median']
        md_max = md_data['benchmarks'][0]['metrics']['timeToInitialDisplayMs']['maximum']
    with open(high_demand) as f:
        hd_data = json.load(f)
        hd_runs = hd_data['benchmarks'][0]['metrics']['timeToInitialDisplayMs']['runs']
        hd_low = hd_data['benchmarks'][0]['metrics']['timeToInitialDisplayMs']['minimum']
        hd_median = hd_data['benchmarks'][0]['metrics']['timeToInitialDisplayMs']['median']
        hd_max = hd_data['benchmarks'][0]['metrics']['timeToInitialDisplayMs']['maximum']

    # Create a DataFrame from the runs data
    df = pd.DataFrame({'LowDemand': ld_runs, 'MediumDemand': md_runs, 'HighDemand': hd_runs})

    # Plot the boxplot
    plt.figure(figsize=(8, 6))
    sns.boxplot(data=df, width=0.5)
    # Title for the boxplot depending on the UI
    if "XML" in path:
        plt.title('Boxplot of XML Startup time ' + path)
        filename = path + "_Boxplot_XML.png"
    else:
        plt.title('Boxplot of Jetpack Compose Startup Time ' + path)
        filename = path + "_Boxplot_Jetpack.png"
    plt.ylabel('Time (ms)')

    # Set the y-lim to be the high demand worst time + 1000.
    # Due to High demand always on our test have worse startup time.

    plt.ylim(
        1250,
        1900
    )
    plt.grid(True)
    plt.savefig("Plots/Startup_Plots/" + filename)

    plt.show()

    # Bar plot
    barWidth = 0.25
    fig = plt.subplots(figsize=(12, 8))

    lowBar = [ld_low, ld_median, ld_max]
    mediumBar = [md_low, md_median, md_max]
    highBar = [hd_low, hd_median, hd_max]

    br1 = np.arange(len(lowBar))
    br2 = [x + barWidth for x in br1]
    br3 = [x + barWidth for x in br2]

    plt.bar(br1, lowBar, color='r', width=barWidth, edgecolor='grey', label='Low Demand')
    plt.bar(br2, mediumBar, color='g', width=barWidth, edgecolor='grey', label='Medium Demand')
    plt.bar(br3, highBar, color='b', width=barWidth, edgecolor='grey', label='High Demand')

    # Title for the boxplot depending on the UI
    if "XML" in path:
        plt.xlabel("The startup time of XML " + path)
        filename = path + "_barChart_XML.png"

    else:
        plt.xlabel("The startup time of Jetpack Compose " + path)
        filename = path + "_barChart_Jetpack.png"

    plt.ylabel('Time (ms)')
    plt.xticks([r + barWidth for r in range(len(lowBar))], ["Min", "Median", "Max"])
    plt.legend()
    plt.savefig("Plots/Startup_Plots/" + filename)
    plt.show()


main()