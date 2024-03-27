import json
import scipy.stats as stats
import numpy as np
import statsmodels.stats.multicomp as multi
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def main():
    path = 'Mac_Intel_XML_Test'
    low_demand = path + '/LowDemandTestResult.json'
    medium_demand = path + '/MediumDemandTestResult.json'
    high_demand = path + '/HighDemandTestResult.json'

    # Read the JSON file
    with open(low_demand) as f:
        ld_data = json.load(f)
        ld_runs = ld_data['benchmarks'][0]['metrics']['timeToInitialDisplayMs']['runs']
    with open(medium_demand) as f:
        md_data = json.load(f)
        md_runs = md_data['benchmarks'][0]['metrics']['timeToInitialDisplayMs']['runs']
    with open(high_demand) as f:
        hd_data = json.load(f)
        hd_runs = hd_data['benchmarks'][0]['metrics']['timeToInitialDisplayMs']['runs']

    # Create a DataFrame from the runs data
    df = pd.DataFrame({'LowDemand': ld_runs, 'MediumDemand': md_runs, 'HighDemand': hd_runs})

    # Plot the boxplot
    plt.figure(figsize=(8, 6))
    sns.boxplot(data=df, width=0.5)
    # Title for the boxplot depending on the UI
    if "XML" in path:
        plt.title('Boxplot of XML Startup time ' + path)
    else:
        plt.title('Boxplot of Jetpack Compose Startup Time ' + path)

    plt.ylabel('Time (ms)')

    # Set the y-lim to be the high demand worst time + 1000.
    # Due to High demand always on our test have worse startup time.
    plt.ylim(
        0,
        hd_data['benchmarks'][0]['metrics']['timeToInitialDisplayMs']['maximum'] + 1000
    )
    plt.grid(True)
    plt.show()


main()


